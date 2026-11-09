# Open Legal Data

This is our international landing page [www.openlegaldata.io](https://openlegaldata.io/), built with Jekyll
(Ruby 4.0, Jekyll 4.4). GitHub Actions builds it on every push to `master` and publishes `_site` to the `gh-pages`
branch; pull requests are built but not deployed.

## Run locally

```bash
bundle install
bundle exec jekyll serve          # http://localhost:4000
bundle exec jekyll build          # static site in _site
```

Without a local Ruby, use Docker:

```bash
docker run --rm -it -p 127.0.0.1:4000:4000 -u $(id -u):$(id -g) \
  -e HOME=/tmp -e BUNDLE_PATH=/site/vendor/bundle -v $PWD:/site -w /site \
  ruby:4.0 sh -c 'bundle install && bundle exec jekyll serve --host 0.0.0.0 --force_polling'
```

Dependencies are pinned in `Gemfile.lock`. Upgrade with `bundle update` and check the build.

## Content

- `_layouts/home.html`: homepage (hero, numbers strip, info boxes). The page frame and colours are the oldp theme
  in `_sass/_base.scss`; the content elements are styled in `_sass/_landing.scss`.
- `open-data.md`: datasets, REST API and MCP server. `research.md`: research papers. `about.md`: project and
  call for contributors (`/team/` redirects here).
- `_config.yml` → `links`: platform, API, MCP, Hugging Face, Discord URLs used across the site.
- `_data/stats.yml`: rounded corpus numbers ("+400,000") for the homepage and data page. Raise them only when the corpus passes the next step; exact numbers go in the release blog post.

### Research papers

The research page lists papers citing Open Legal Data from
[oldp-citations](https://github.com/openlegaldata/oldp-citations):

- `_data/papers.yml` is generated from the BibTeX files, do not edit it by hand.
- `_data/research_topics.yml` assigns every paper to a topic. The `llm` topic is the highlight of language models
  trained on Open Legal Data: list a paper there only if its full text says our data is part of the training data
  or corpus.
- `scripts/extra_papers.bib` holds papers that use our data without citing our paper. List them under `not_citing`
  in `research_topics.yml` so they are shown but not counted as citations.

After adding citations to oldp-citations (checked out next to this repo):

```bash
uv run scripts/build_papers.py --bib-dir ../oldp-citations/bib
```

The script fails and names the citekeys that are not assigned to a topic; add them to `research_topics.yml` and
run it again.

## Analytics

Self-hosted, cookieless Matomo at matomo.openlegaldata.io, configured like the tracker on de.openlegaldata.io
(`_includes/matomo.html`). It is only rendered in production builds (`JEKYLL_ENV=production`, set in CI) and
while `matomo_site_id` in `_config.yml` is not empty. The privacy page describes it.

## License

- Code: MIT
- Content: [CC 4.0 Attribution](https://creativecommons.org/licenses/by/4.0/)
