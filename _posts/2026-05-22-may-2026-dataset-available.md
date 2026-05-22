---
layout: post
title: "May 2026 Dataset Available: 423,941 Court Decisions, 113,537 Laws, 7,438,459 Citations"
categories: research
author: Malte
language: en
---

We just published a fresh snapshot of the [Open Legal Data](https://de.openlegaldata.io)
corpus to the Hugging Face Hub. The 2026-05-20 dump covers every
available record in the platform: **423,941 German court
decisions**, **113,537 laws** across
**7,058 law books**, and the
**7,438,459 citation edges** between them. All three
datasets are versioned per dump date, public, and load directly with
the 🤗 `datasets` library.

This is the first release after long time of inactivity. Expect more updates soon. Join us on [Discord](https://discord.gg/WCy3aq25ZF) to contribute to the project.

## Datasets

| Dataset | Rows | Hub link |
| --- | --- | --- |
| Court decisions | 423,941 | [`openlegaldata/court-decisions-germany`](https://huggingface.co/datasets/openlegaldata/court-decisions-germany) |
| Laws            | 113,537  | [`openlegaldata/laws-germany`](https://huggingface.co/datasets/openlegaldata/laws-germany) |
| Citation graph  | 7,438,459  | [`openlegaldata/legal-citation-graph-germany`](https://huggingface.co/datasets/openlegaldata/legal-citation-graph-germany) |

Each dataset is published as three configs:

- `dump-20260520` — the full snapshot
- `dump-20260520-10k` — random sample of 10,000 rows (seed=42)
- `dump-20260520-1k` — random sample of 1,000 rows (seed=42; strict subset of the 10k)

The 1k and 10k subsets are intended for quick exploration; both
preserve the full schema and processing pipeline so prototypes scale
to the full corpus without code changes.

## Loading the data

```python
from datasets import load_dataset

# Full court decisions corpus
cases = load_dataset(
    "openlegaldata/court-decisions-germany",
    name="dump-20260520",
    split="train",
)
print(cases[0]["markdown_content"][:200])

# Small subsample for exploration
sample = load_dataset(
    "openlegaldata/court-decisions-germany",
    name="dump-20260520-1k",
    split="train",
)
```

Each court decision carries both the original HTML in `content` and a
clean Markdown rendering in `markdown_content`. Reference markers
extracted with [`legal-reference-extraction`](https://github.com/openlegaldata/legal-reference-extraction)
are attached as a JSON string in `reference_markers`. Laws follow the
same `content` + `markdown_content` convention; references are a flat
denormalised table of slug-based edges (no internal database IDs).

## What's in the data

### Court decisions (423,941)

By year:

| Year | Decisions |
| --- | --- |
| 2026 | 2,793 |
| 2025 | 19,793 |
| 2024 | 23,076 |
| 2023 | 24,381 |
| 2022 | 19,671 |
| 2021 | 15,797 |
| 2020 | 15,982 |
| 2019 | 14,766 |
| 2018 | 19,392 |
| 2017 | 22,119 |

By state:

| State | Decisions |
| --- | --- |
| Nordrhein-Westfalen | 168,057 |
| Bundesrepublik Deutschland | 56,361 |
| Hessen | 27,427 |
| Niedersachsen | 27,262 |
| Baden-Württemberg | 24,757 |

By level of appeal:

| Level of appeal | Decisions |
| --- | --- |
| Oberlandesgericht | 67,410 |
| Bundesgericht | 56,361 |
| Landgericht | 33,949 |
| Amtsgericht | 13,495 |

### Laws (113,537 sections across 7,058 books)

Largest law books by section count:

| Law book | Sections |
| --- | --- |
| BGB | 2,538 |
| ZPO | 1,091 |
| BinSchStrO 2012 | 718 |
| SGB 5 | 691 |
| HGB | 690 |
| StPO | 685 |
| StGB | 557 |
| FamFG | 527 |
| AO 1977 | 503 |
| SGB 6 | 501 |

### Citation graph (7,438,459)

By source side:

| Source side | Edges |
| --- | --- |
| Case | 7,008,351 |
| Law | 430,108 |

By target side:

| Target side | Edges |
| --- | --- |
| Law | 6,787,718 |
| Case | 650,741 |

Most-cited law books:

| Cited law book | Citations |
| --- | --- |
| VwGO | 938,514 |
| BGB | 936,118 |
| ZPO | 904,301 |
| Grundgesetz | 436,856 |
| SGG | 276,904 |
| EStG | 242,478 |
| StGB | 183,537 |
| StPO | 150,072 |
| FGO | 134,509 |
| ArbGG | 110,398 |

## Usage ideas

- **Citation analysis** — the
  [`openlegaldata/legal-citation-graph-germany`](https://huggingface.co/datasets/openlegaldata/legal-citation-graph-germany)
  dataset is a slug-keyed edge list you can join straight back to the
  court-decision and laws datasets with pandas / DuckDB / Polars.
- **Legal text generation / retrieval** — `markdown_content` is clean
  enough to feed directly to tokenisers; the 1k subset is ideal for
  pipeline prototyping.
- **Court-by-court analyses** — every decision carries court metadata
  (`court.name`, `court.jurisdiction`, `court.level_of_appeal`, etc.)
  so you can filter or group without joins.

The older notebooks under
[`openlegaldata/oldp-notebooks`](https://github.com/openlegaldata/oldp-notebooks)
still work and show end-to-end examples of citation extraction,
litigation-value extraction, and n-gram modelling on the corpus.

## Licensing

In Germany, acts, statutory instruments, official decrees and official
notices, as well as decisions (including court decisions) and official
head notes of decisions do not enjoy copyright protection (UrhG § 5).
The collection and metadata are released under the
[Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/).

## Citation

If you use these datasets, please cite our
[research paper](https://arxiv.org/abs/2005.13342):

```bibtex
@inproceedings{ostendorff2020oldp,
  author    = {Ostendorff, Malte and Blume, Till and Ostendorff, Saskia},
  title     = {Towards an Open Platform for Legal Information},
  year      = {2020},
  isbn      = {9781450375856},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3383583.3398616},
  booktitle = {Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020},
  pages     = {385--388},
  series    = {JCDL '20},
}
```

Questions, ideas or bugs? Join us on
[Discord](https://discord.gg/WCy3aq25ZF) or open an issue on the
[oldp](https://github.com/openlegaldata/oldp) repo.
