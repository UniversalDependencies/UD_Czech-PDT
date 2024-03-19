# Summary

The Czech-PDT UD treebank is based on the Prague Dependency Treebank – Consolidated 1.0
(PDT-C), created at the Charles University in Prague.


# Introduction

The treebank consists of 87,907 sentences (1.5 M tokens) and its domain is
mainly newswire, reaching also to business and popular scientific articles
from the 1990s. The treebank is licensed under the terms of
[CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)
and its original (non-UD) version can be downloaded from
[http://hdl.handle.net/11234/1-3185](http://hdl.handle.net/11234/1-3185).

The morphological and syntactic annotation of the Czech UD treebank is created
through a conversion of PDT data. The conversion procedure has been designed by
Dan Zeman and implemented in Treex.


# Acknowledgments

We wish to thank all of the contributors to the original PDT annotation effort,
including Eduard Bejček, Eva Hajičová, Jan Hajič, Pavlína Jínová,
Václava Kettnerová, Veronika Kolářová, Marie Mikulová, Jiří Mírovský,
Anna Nedoluzhko, Jarmila Panevová, Lucie Poláková, Magda Ševčíková,
Jan Štěpánek, and Šárka Zikánová.

## References

* Jan Hajič, Eduard Bejček, Jaroslava Hlaváčová, Marie Mikulová, Milan Straka,
  Jan Štěpánek, and Barbora Štěpánková. 2020. Prague Dependency Treebank –
  Consolidated 1.0.
  In: Proceedings of the 12th Conference on Language Resources and Evaluation
  (LREC 2020), Marseille, France, pp. 5208-5218.
  https://aclanthology.org/2020.lrec-1.641.pdf

* Eduard Bejček, Eva Hajičová, Jan Hajič, Pavlína Jínová, Václava Kettnerová,
  Veronika Kolářová, Marie Mikulová, Jiří Mírovský, Anna Nedoluzhko,
  Jarmila Panevová, Lucie Poláková, Magda Ševčíková, Jan Štěpánek,
  and Šárka Zikánová. 2013. Prague Dependency Treebank 3.0,
  LINDAT/CLARIN digital library at Institute of Formal and Applied Linguistics,
  Charles University in Prague,
  http://hdl.handle.net/11858/00-097C-0000-0023-1AAF-3.

* Eduard Bejček, Jarmila Panevová, Jan Popelka, Pavel Straňák, Magda Ševčíková,
  Jan Štěpánek, and Zdeněk Žabokrtský. 2012. Prague Dependency Treebank 2.5 –
  a revisited version of PDT 2.0.
  In: Proceedings of the 24th International Conference on Computational
  Linguistics (Coling 2012), Mumbai, India, pp. 231-246.
  http://www.aclweb.org/anthology/C/C12/C12-1015.pdf


# Domains and Data Split

NOTE: Earlier releases of the treebank had four training data files. This was
due to Github restrictions on file size. We have now re-joined the training
files in the official release package (beginning with UD v1.3), so there is
just one training file as in all other languages, and it is named
cs-ud-train.conllu. The four files in previous releases corresponded to the
four sources of the original texts; the sources may still be distinguished,
if desirable, by the prefixes of sentence ids. All of them are newspapers, but

* l (ln) and m (mf) are mainstream daily papers (news, commentaries, but also
  sports results and TV programs)
* c (cmpr) is a business weekly
* v (vesm) contains popular scientific articles (the hardest to parse: long
  sentences and unusual vocabulary)

The dev and test sets contain all four sources and their size is proportional
to the sizes of the respective training parts.


## Source of annotations

This table summarizes the origins and checking of the various columns of the CoNLL-U data.

| Column | Status |
| ------ | ------ |
| ID     | Sentence segmentation and (surface) tokenization was automatically done and then hand-corrected; see [PDT documentation](http://ufal.mff.cuni.cz/pdt2.0/doc/pdt-guide/en/html/ch02.html). Splitting of fused tokens into syntactic words was done automatically during PDT-to-UD conversion. |
| FORM   | Identical to Prague Dependency Treebank 3.0 form. |
| LEMMA  | Manual selection from possibilities provided by morphological analysis: two annotators and then an arbiter. PDT-to-UD conversion stripped from lemmas the ID numbers distinguishing homonyms, semantic tags and comments; this information is preserved as attributes in the MISC column. |
| UPOS   | Converted automatically from XPOS (via [Interset](https://ufal.mff.cuni.cz/interset)), from the semantic tags in PDT lemma, and occasionally from other information available in the treebank; human checking of patterns revealed by automatic consistency tests. |
| XPOS   | Manual selection from possibilities provided by morphological analysis: two annotators and then an arbiter. |
| FEATS  | Converted automatically from XPOS (via Interset), from the semantic tags in PDT lemma, and occasionally from other information available in the treebank; human checking of patterns revealed by automatic consistency tests. |
| HEAD   | Original PDT annotation is manual, done by two independent annotators and then an arbiter. Automatic conversion to UD; human checking of patterns revealed by automatic consistency tests. |
| DEPREL | Original PDT annotation is manual, done by two independent annotators and then an arbiter. Automatic conversion to UD; human checking of patterns revealed by automatic consistency tests. |
| DEPS   | Generated from the basic UD tree and additional annotation from the original PDT. |
| MISC   | Information about token spacing taken from PDT annotation. Lemma / word sense IDs, semantic tags and comments on meaning moved here from the PDT lemma. Some other annotation from PDT, such as coreference and functors (for parts of the corpus). |

The original PDT has four layers of annotation: word layer, morphological layer,
analytical (surface-syntactic) layer, and tectogrammatical (deep-syntactic) layer;
they are also referred to as w-, m-, a-, and t-layer. Until UD release 2.11, the
conversion was based only on the first three layers. From release 2.12 on, the
conversion procedure also uses information from the t-layer. Note that this layer
of annotation is not available for the entire treebank but only for a part of it.
Sentences for which the t-layer was available can be recognized by the sentence-
level comment "Tectogrammatical annotation available." Some attributes specific
to the t-layer are ported to the MISC column of the CoNLL-U file:

* Functor ... The tectogrammatical functor of this node w.r.t. its parent in the
  t-tree. It often corresponds to the parent in the UD tree but it is not always
  the case.
* Entity ... Coreference annotation in the [CorefUD](https://ufal.mff.cuni.cz/corefud)
  format. While the format could be also used for named entity annotation, named
  entities are annotated only if it is needed for coreference.
* Bridging ... Annotation of bridging relations in the CorefUD format.

Furthermore, conversion of syntactic annotation may occasionally differ from what
it would look like without the tectogrammatical input. This is especially true of
the enhanced dependency graph.


# Changelog

* 2024-05-15 v2.14
* 2024-??-?? CorefUD 1.2
  * Improved distinction between adverbial predicates (with copula) and adverbial modifiers.
  * Coreference annotation: If a bracket is in mention span, the paired bracket is added too, if possible.
  * More restrictive use of orphans and empty nodes: Not in non-verbal coordinated sentences.
  * Fixed crossing coreference mentions.
  * Fixed treatment of "by" in aux/cop chains.
  * Improved form and position of abstract predicates in gapping.
* 2023-11-15 v2.13
  * Removed NumValue from all Czech UD treebanks.
  * Pseudo-existential "být" with oblique/adverbial modifiers changed to copula.
* 2023-05-15 v2.12
  * Source data switched from PDT 3.0 to PDT-C 1.0.
    * Underlying text data is the same.
    * Changed some aspects of lemmatization, including LId and other attributes in MISC.
    * Somewhat different XPOS tag set.
    * UD features: now all verbs have Aspect; minor changes at various other places.
    * Foreign words are now systematically tagged X (previously, many of them had descriptive UPOS tags).
  * The tectogrammatical (t-) layer of source annotation is now used for documents for which it is available.
    * Sentences converted with the help of t-layer have the comment "Tectogrammatical annotation available."
    * There are more enhanced dependency relations and empty nodes.
    * The MISC column contains CorefUD-style annotation of coreference (now also in the UD release).
    * The MISC column contains tectogrammatical functors.
  * Temporary fix of double subjects (second subject converted to dep).
    In the long run, the cause should be found and fixed upstream.
  * Added the enhanced relation subtype nsubj:xsubj.
* 2023-??-?? CorefUD 1.1
  * Removed superfluous empty nodes #Rcp, #Cor, #QCor.
  * Removed empty nodes depending on the artificial 0:root.
  * "Bych/bys/by/bychom/byste" in MWTs no longer breaks mention spans.
  * Improved guessing of pronominal forms for empty nodes.
  * Functors added also to non-empty nodes.
* 2022-05-15 v2.10
  * Added VerbForm=Part|Voice=Pass to long forms of passive participles.
  * Added VerbForm=Vnoun to verbal nouns.
  * The verb 'být' is now AUX in all contexts.
  * Merged PRON/DET 'sám', 'samý'.
* 2022-04-06 CorefUD 1.0
  * Fixed bug: Distinction between clauses and nominals.
  * Fixed bug: Gapping empty nodes vs. coreference empty nodes.
* 2021-05-15 v2.8
  * Fixed bug: SpaceAfter=No should not occur at the end of paragraph.
  * "§" is now SYM instead of NOUN.
  * Fixed recognition of clauses with passive participles (ADJ).
* 2021-03-11 CorefUD 0.1
  * First release of the coreference annotation together with UD morphology and syntax in the CorefUD collection.
  * Unlike the main releases for UD, CorefUD uses the tectogrammatical layer of PDT and does not include the PDT sentences that lack this layer.
* 2020-11-15 v2.7
  * Fixed bug: question marks were replaced by asterisks.
  * Adjusted treatment of double lemmas like "m`metr".
* 2020-05-15 v2.6
  * Genitive, dative and instrumental nominals are now considered oblique.
  * Added enhanced relations with case information.
  * Added enhanced relations around relative clauses.
  * Added enhanced external subjects in control verb constructions.
  * Added empty nodes to enhanced graphs (but orphans are just converted to dep).
* 2019-05-15 v2.4
  * Modified conversion: nouns do not have objects.
  * Fixed punctuation attachment.
  * Fixed "a to", "to jest" and other expressions.
* 2018-11-15 v2.3
  * Bug fix: conditional "by" should be attached as 'aux', not 'aux:pass'.
  * Flat name structures extended to titles and occupations.
  * Added LDeriv for passive participles (the infinitive of the source verb).
* 2018-04-15 v2.2
  * Repository renamed from UD_Czech to UD_Czech-PDT.
  * Added enhanced representation of dependencies propagated across coordination.
    The distinction of shared and private dependents is derived deterministically from the original Prague annotation.
  * Fixed computation of the LDeriv MISC attribute.
* 2017-11-15 v2.1
  * Retagged pronouns “každý” and “kterýžto”.
  * Prepositional objects are now “obl:arg” instead of “obj”.
  * Instrumental phrases for demoted agents in passives are now “obl:agent”.
* 2017-03-01 v2.0
  * Converted to UD v2 guidelines.
  * Reconsidered PRON vs. DET. Extended PronType and Poss.
  * Improved advmod vs. obl distinction.
  * L-participles are verbs, other participles are adjectives.
  * Removed style flags from lemmas.
* 2016-05-15 v1.3
  * Fixed adverbs that were attached as nmod; correct: advmod.
  * Copulas with clausal complements are now heads.
  * Improved conversion of AuxY.
  * Relation of foreign prepositions changed to foreign.
* 2015-11-15 v1.2
  * Conversion procedure rewritten again (may result in minor differences in
    borderline cases)
  * Only one “root” relation per tree now enforced; some bugs around root fixed
  * The “name” relation goes now always left-to-right (in UD 1.1 it was family-
    to-given name)
  * Fixed bug with numeral-noun swapping that destroyed coordinations of
    numbers and caused the “conj” relation to go right-to-left
  * Fixed minor bugs around subordinating conjunctions
  * Changed dependency relation of reflexive pronouns attached to inherently
    reflexive verbs from compound:reflex to expl
  * Applied heuristics to distinguish at least some iobj from dobj
  * Fixed bugs around xcomp (future infinitives and subjects attached to
    controlled verbs)
* 2015-05-15 v1.1
  * Conversion procedure completely rewritten
  * Improved heuristics to distinguish DET and PRON
  * Improved treatment of comparative complements (conjunctions “než” and “jako”)
  * Remaining lemma extensions moved from LEMMA to MISC



<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v1.0
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: news reviews nonfiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Zeman, Daniel; Hajič, Jan
Contributing: elsewhere
Contact: zeman@ufal.mff.cuni.cz
===============================================================================
</pre>
