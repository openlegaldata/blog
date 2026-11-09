---
layout: page
title: Research
permalink: /research/
---
{% assign paper_count = site.data.papers.size | minus: site.data.research_topics.hidden.size| minus: site.data.research_topics.not_citing.size %}

## Legal Research

Open Legal Data started as a research project and is built for research: the
court decisions, laws and citations are available as
[open datasets]({{ '/open-data/#datasets' | relative_url }}), through a
[REST API]({{ '/open-data/#api' | relative_url }}) and through an
[MCP server]({{ '/open-data/#mcp' | relative_url }}) for AI assistants.
Our approach is described in
[Towards an Open Platform for Legal Information]({{ site.links.paper_doi }})
(JCDL 2020, [arXiv]({{ site.links.paper_arxiv }})).

Since then, Open Legal Data has been cited in **{{ paper_count }} papers**:
it is part of the training data of open language models, the basis of new
legal datasets and benchmarks, and used in work on legal search, question
answering, citation analysis and legal NLP.

{% include research_topics.html %}

### Missing a paper?

The list is generated from
[openlegaldata/oldp-citations]({{ site.links.citations }}). If you use Open
Legal Data in your research and your paper is missing, open a pull request
there or write to [{{ site.email }}](mailto:{{ site.email }}).

### Cite Open Legal Data {#cite}

If you use the platform, the API or the datasets, please cite our paper:

<div class="cite-box" markdown="1">

```bibtex
@inproceedings{ostendorff2020oldp,
  author    = {Ostendorff, Malte and Blume, Till and Ostendorff, Saskia},
  title     = {Towards an Open Platform for Legal Information},
  booktitle = {Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020},
  series    = {JCDL '20},
  year      = {2020},
  pages     = {385--388},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3383583.3398616},
}
```

</div>
