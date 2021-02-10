---
layout: research
title: Legal Research
permalink: /research/
---

## Legal Research

Recently, there has been an increasing interest in legal data mining tools and applications around the world. 
For Open Legal Data, we focus mainly on two areas: 
(1) Finding and Providing Legal Documents and 
(2) Text Mining on Legal Documents.

Our general approach is described in the following research paper:  
[Towards an Open Platform for Legal Information; In Proceedings of the ACM/IEEE Joint Conference on Digital Libraries (JCDL 2020).](https://ostendorff.org/assets/pdf/ostendorff2020b.pdf)


#### Finding and Providing Legal Documents

The Free Law Project is a California non-profit public benefit corporation.
The Free Law Project (and its service CourtListener) selfdeclared
its mission to be "to provide free, public, and permanent
access to primary legal materials on the Internet for educational,
charitable, and scientific purposes to the benefit of the general public
and the public interest" [^1]. 
Online distribution of the opinions occurs through their CourtListener project. 
CourtListener.com aims to ease this problem by providing a free and open source platform for the aggregation, organization, search and retrieval of legal documents.
CourtListener.com seeks to collect and freely distribute
online all United States court opinions, both state and federal, both
historical and current.

Frosterus et al. [^2] present how they transferred the Finnish
government web service Finlex to a Linked Open Data Service for
Finnish law and related judicial documents. 
The original Finlex service made already documents openly available. However, the data
was provided only as traditional XML schema without considering
the Linked Data principles. They show how to model legislation
and court decisions in RDF. They demonstrate the usefulness of
linked open data for content producers, application developers and
data analysts.

In summary, there exist successful data collection efforts of legal
documents across the world. However, in Germany, there is a clear
gap.

#### Text Mining on Legal Documents

Aletras et al. [^3] present that NLP and ML techniques can be
used to predict decisions of the European Court of Human Rights.
They build a SVM model that predicts the decisions with a accuracy
of 79% on average. As features sole textual representations of the
case, i. e., N-grams, and topics, are used. As data source, Aletras et
al. [^3] rely on a small sub-set of 80-250 cases that were available for a
particular articles of the European Convention on Human Rights.
Lippi et al. [^4] automatically evaluate terms of services of online
platforms that is another resource of legal documents that is
ubiquitous available.


#### References


[^1]: Michael Lissner: CourtListener.com: A platform for researching and staying abreast of the latest in the law. (2010).

[^2]: Matias Frosterus, Jouni Tuominen, and Eero Hyvönen: Facilitating Re-use of Legal Data in Applications - Finnish Law as a Linked Open Data Service. Legal Knowledge and Information Systems: JURIX 2014: The Twenty-Seventh Annual Conference (2014), 115–124.

[^3]: Nikolaos Aletras, Dimitrios Tsarapatsanis, Daniel Preotiuc-Pietro, Vasileios Lampos: Predicting judicial decisions of the European Court of Human Rights: a Natural Language Processing perspective. PeerJ Computer Science 2: e93 (2016)

[^4]: Marco Lippi, Przemyslaw Palka, Giuseppe Contissa, Francesca Lagioia, Hans-
Wolfgang Micklitz, Giovanni Sartor, and Paolo Torroni: CLAUDETTE: an
Automated Detector of Potentially Unfair Clauses in Online Terms of Service.
arXiv (2018).
