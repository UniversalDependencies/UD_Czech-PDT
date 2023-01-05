#!/usr/bin/env python3
# Takes a list of pairs of PDT node id and functor, extracted from the t-layer of PDT.
# Reads a CoNLL-U file with data converted from PDT to UD. Looks for nodes listed in
# the functor file. If found, adds the functor to the MISC column of the node.
# Writes the modified CoNLL-U file.

from udapi.block.read.conllu import Conllu
import re

###!!! We will want to take the file names as command line arguments.
fname_functors = 'not-to-release/functors.txt' # node ids and functors extracted from t-trees in PDT
fname_udin = 'cs_pdt-ud-train-c.conllu' # PDT converted to UD (or a part of it)
fname_udout = 'output.conllu' # the same file enhanced with functors where node ids match

# Read the list of node ids and functors extracted from the t-layer of PDT.
# Store it in a dictionary.
dict = {}
f = open(fname_functors)
for line in f:
    # For some reason, the script preparing the functors added spaces around the tab.
    (id, functor) = line.rstrip().split(" \t ")
    # a#a-cmpr9410-001-p2s1w2
    m = re.match(r"^a#a-(.+)w([0-9]+)$", id)
    if m:
        sentid = m.group(1)
        wordid = m.group(2)
        if not sentid in dict:
            dict[sentid] = {}
        dict[sentid][wordid] = functor
    else:
        print("WARNING: Cannot parse node id '%s'" % id)
    if not re.match(r"^[A-Z]+$", functor):
        print("WARNING: Unexpected format of functor '%s'" % functor)

# Read the CoNLL-U file, add functors to recognized nodes, and write it again.
reader = Conllu(files=fname_udin)
documents = reader.read_documents()
###!!! At present we can only save one document at a time. If there are multiple
###!!! documents, the latter documents will overwrite the former.
if len(documents) > 1:
    print("WARNING: There are %d documents but only the last one will be saved." % len(documents))
for d in documents:
    for b in d.bundles:
        root = b.get_tree()
        sid = root.sent_id
        if sid in dict:
            # We assume that the low-level tokenization has not changed, that is,
            # the number and order of tokens is the same as in the original PDT.
            # However, if there are multi-word tokens ('abychom, kdybychom, tys...'),
            # we must stick to the token index, rather than word/node ord.
            nodes = root.descendants
            wids = []
            wid = 1
            for node in nodes:
                wids[node.ord] = str(wid)
                if not node.multiword_token or node == node.multiword_token.words[-1]:
                    wid += 1
            for node in nodes:
                wid = wids[node.ord]
                if wid in dict[sid]:
                    node.misc['Functor'] = dict[sid][wid]
    ###!!! If there are multiple documents in the input file, only the last one will survive on output.
    d.store_conllu('output.conllu') ### možná nahoře neimportovat reader, ale rovnou Document a vytvořit ho konstruktorem (filename=, viz dokumentace)
