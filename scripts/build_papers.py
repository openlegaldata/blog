# /// script
# requires-python = ">=3.10"
# dependencies = ["bibtexparser==1.4.3", "pyyaml>=6"]
# ///
"""Build _data/papers.yml from the oldp-citations BibTeX files.

The research page (research.md) lists papers that cite or use Open Legal
Data. The BibTeX entries live in https://github.com/openlegaldata/oldp-citations
(bib/*.bib); this script turns them into a YAML map keyed by citekey, so the
Liquid templates can look papers up with site.data.papers[key].

Which topic a paper belongs to, the topic order and the notes for the
language-model highlight are curated by hand in _data/research_topics.yml.
The script checks that file against the bib entries and fails when a paper is
not assigned to exactly one topic (or listed under `hidden`), so new
citations are not silently left off the page.

Usage (from the repo root, oldp-citations checked out next to it):

    uv run scripts/build_papers.py
    uv run scripts/build_papers.py --bib-dir ../oldp-citations/bib --check
"""

import argparse
import glob
import os
import re
import sys
import urllib.parse

import bibtexparser
import yaml
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARXIV_RE = re.compile(r"arXiv:(\d{4}\.\d{4,5})", re.I)


def clean(text: str) -> str:
    """Collapse whitespace and drop leftover BibTeX braces."""
    return " ".join(text.replace("{", "").replace("}", "").split())


def authors(raw: str, limit: int = 3) -> str:
    names = [n.strip() for n in re.split(r"\s+and\s+", clean(raw)) if n.strip()]
    others = any(n.lower() == "others" for n in names)
    names = [n for n in names if n.lower() != "others"]
    out = []
    for n in names:
        if "," in n:
            last, first = [p.strip() for p in n.split(",", 1)]
            n = f"{first} {last}".strip()
        out.append(n)
    if len(out) > limit or (others and out):
        return ", ".join(out[:limit]) + " et al."
    return ", ".join(out[:-1]) + (" and " if len(out) > 1 else "") + out[-1] if out else ""


def venue(e: dict) -> str:
    kind = e["ENTRYTYPE"]
    if kind == "phdthesis":
        return clean(f"PhD thesis, {e['school']}" if e.get("school") else "PhD thesis")
    if kind == "mastersthesis":
        label = clean(e.get("type", "Master's thesis"))
        return f"{label}, {clean(e['school'])}" if e.get("school") else label
    text = clean(e.get("journal") or e.get("booktitle") or e.get("publisher") or "")
    if ARXIV_RE.search(text):
        return "arXiv"
    return text


def link(e: dict, title: str) -> str:
    if e.get("doi"):
        return "https://doi.org/" + e["doi"].strip()
    m = ARXIV_RE.search(e.get("journal", "") + " " + e.get("eprint", ""))
    if m:
        return "https://arxiv.org/abs/" + m.group(1)
    if e.get("url"):
        return e["url"].strip()
    return "https://scholar.google.com/scholar?q=" + urllib.parse.quote(f'"{title}"')


def load_entries(bib_dir: str, extra_bib: str) -> dict:
    entries = {}
    paths = sorted(glob.glob(os.path.join(bib_dir, "*.bib")))
    if not paths:
        sys.exit(f"no .bib files in {bib_dir} (pass --bib-dir)")
    for path in [*paths, extra_bib]:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        with open(path, encoding="utf-8") as fh:
            for e in bibtexparser.load(fh, parser=parser).entries:
                if e["ID"] in entries:
                    sys.exit(f"duplicate citekey {e['ID']} in {path}")
                entries[e["ID"]] = e
    return entries


def build(entries: dict) -> dict:
    papers = {}
    for key, e in entries.items():
        title = clean(e.get("title", ""))
        papers[key] = {
            "title": title,
            "authors": authors(e.get("author", "")),
            "year": int(e["year"]) if e.get("year", "").isdigit() else None,
            "venue": venue(e),
            "url": link(e, title),
        }
    return dict(sorted(papers.items(), key=lambda kv: (-(kv[1]["year"] or 0), kv[0])))


def check(papers: dict, topics_path: str) -> list[str]:
    with open(topics_path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    seen: dict[str, str] = {}
    errors = []
    for topic in cfg["topics"]:
        for item in topic["papers"]:
            key = item["key"] if isinstance(item, dict) else item
            if key not in papers:
                errors.append(f"{topic['id']}: unknown citekey {key}")
            if key in seen:
                errors.append(f"{key} is in both {seen[key]} and {topic['id']}")
            seen[key] = topic["id"]
    for key in cfg.get("hidden", []):
        if key in seen:
            errors.append(f"{key} is hidden but listed in {seen[key]}")
        seen[key] = "hidden"
    errors += [f"{k} is not assigned to a topic" for k in papers if k not in seen]
    for key in cfg.get("not_citing", []):
        if key not in papers or seen.get(key, "hidden") == "hidden":
            errors.append(f"not_citing: {key} is not shown in any topic")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--bib-dir", default=os.path.join(ROOT, "..", "oldp-citations", "bib"))
    ap.add_argument("--extra-bib", default=os.path.join(ROOT, "scripts", "extra_papers.bib"),
                    help="papers that use Open Legal Data but do not cite our paper")
    ap.add_argument("--topics", default=os.path.join(ROOT, "_data", "research_topics.yml"))
    ap.add_argument("--out", default=os.path.join(ROOT, "_data", "papers.yml"))
    ap.add_argument("--check", action="store_true", help="only validate, do not write")
    args = ap.parse_args()

    papers = build(load_entries(args.bib_dir, args.extra_bib))
    errors = check(papers, args.topics)
    for err in errors:
        print("ERROR", err, file=sys.stderr)
    if not args.check:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write("# Generated by scripts/build_papers.py from oldp-citations. Do not edit.\n")
            yaml.safe_dump(papers, fh, allow_unicode=True, sort_keys=False, width=1000)
        print(f"wrote {len(papers)} papers to {os.path.relpath(args.out, ROOT)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
