---
layout: post
title: "Open Legal Data releases dataset of 100,000 German court decisions and 444,000 citations"
categories: research
author: Malte
language: en
---

Our initiative has made a large dataset of Germany court decisions and the corresponding citation network publicly 
available to help the community to development new techniques for processing legal text. 
As far as we know there is no similar dataset for German court decisions yet. 
Having no data available, limits the opportunities for researchers and start-ups likewise. 
With the release of the dataset, Open Legal Data hopes to foster both areas, especially in Germany.

All decisions are anonymized by the responsible court and have additional meta data, e.g. date and decision type.
Citation were automatically extracted with our [Legal Reference Extraction](https://github.com/openlegaldata/legal-reference-extraction) 
tool that is also freely available under an Open Source license.  

We are excited to see what the community can achieve with the dataset. 
Feel free to share your results with us or to contact us if you have any questions.

### Download

- [German court decisions](https://static.openlegaldata.io/dumps/de/2019-02-19_oldp_cases.json.gz) (json.gz: 772M)
- [Citation network](https://static.openlegaldata.io/dumps/de/refs/refs.csv.gz) (csv.gz: 4.4M)


### What can you do with the data?

One of the principals of Open Data is, that you should release data and let the people decide what to do with it.
However, if you are not creative enough, just have a look at our examples:

- [Citation analysis](https://github.com/openlegaldata/oldp-notebooks/blob/master/notebooks/references.ipynb): 
    What cites what?
- [Citation network visualization](http://openlegaldata.io/de/citation-network.html): 
    An inactive plot where you can zoom and click on each nodes.
- [Litigation value extraction](https://github.com/openlegaldata/oldp-notebooks/blob/master/notebooks/litigation_value.ipynb): 
    Extract information from the raw text
- [Learning a Predictive N-Gram Model](https://github.com/openlegaldata/oldp-notebooks/blob/master/notebooks/ngram_model.ipynb)

### What is in the data?

In the following we presents some statistics on the dataset so you can a quick overview of its content:

#### Court decisions

```
> SELECT COUNT(*) FROM cases_case;
+----------+
| COUNT(*) |
+----------+
|   104763 |
+----------+

> SELECT YEAR(`date`), COUNT(*) FROM cases_case GROUP BY YEAR(`date`) ORDER BY COUNT(*) DESC LIMIT 15;
+--------------+----------+
| YEAR(`date`) | COUNT(*) |
+--------------+----------+
|         2015 |    16430 |
|         2016 |    15249 |
|         2014 |    15180 |
|         2017 |     9117 |
|         2013 |     7597 |
|         2012 |     7358 |
|         2010 |     7221 |
|         2018 |     7100 |
|         2011 |     6339 |
|         2009 |     2529 |
|         2008 |     2127 |
|         2006 |     1986 |
|         2007 |     1976 |
|         2005 |     1761 |
|         2004 |     1617 |
+--------------+----------+

> SELECT s.name, COUNT(*) FROM cases_case c INNER JOIN courts_court cc ON c.court_id = cc.id INNER JOIN courts_state s ON cc.state_id = s.id GROUP BY cc.state_id ORDER BY COUNT(*) DESC LIMIT 15;
+----------------------------+----------+
| name                       | COUNT(*) |
+----------------------------+----------+
| Bundesrepublik Deutschland |    31267 |
| Nordrhein-Westfalen        |    22782 |
| Baden-Württemberg          |    15245 |
| Rheinland-Pfalz            |     8142 |
| Niedersachsen              |     6661 |
| Sachsen-Anhalt             |     5569 |
| Schleswig-Holstein         |     4057 |
| Mecklenburg-Vorpommern     |     3751 |
| Hamburg                    |     2526 |
| Saarland                   |     2226 |
| Europäische Union          |     2115 |
| Bayern                     |      405 |
| Sachsen                    |       17 |
+----------------------------+----------+
```

#### Citations

``` 
$ wc -l refs.csv 
444034 refs.csv
```

What law books are cited most often?

![What law books are cited most often?]({{ "/assets/img/ref_law_books.png" | relative_url }})

Citing states


![Citing states]({{ "/assets/img/ref_case_states.png" | relative_url }})


### Update

For more recent dumps, please refer to this link: [https://static.openlegaldata.io/dumps/de/](https://static.openlegaldata.io/dumps/de/)

