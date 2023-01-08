#!/usr/bin/env python3
# Takes a list of pairs of PDT node id and functor, extracted from the t-layer of PDT.
# Reads a CoNLL-U file with data converted from PDT to UD. Looks for nodes listed in
# the functor file. If found, adds the functor to the MISC column of the node.
# Writes the modified CoNLL-U file.

from udapi.block.read.conllu import Conllu
import re

###!!! We will want to take the file names as command line arguments.
fname_functors = 'functors.txt' # node ids and functors extracted from t-trees in PDT
fname_udin = '../cs_pdt-ud-train-c.conllu' # PDT converted to UD (or a part of it)
fname_udout = 'output.conllu' # the same file enhanced with functors where node ids match

# Read the list of node ids and functors extracted from the t-layer of PDT.
# Store it in a dictionary.
dict = {}
forms = {} # only for sanity check
f = open(fname_functors)
for line in f:
    (id, functor, form) = line.rstrip().split("\t")
    forms[id] = form
    # cmpr9410-001-p2s1w2
    m = re.match(r"^(.+)w([0-9]+)$", id)
    if m:
        sentid = m.group(1)
        wordid = m.group(2)
        if not sentid in dict:
            dict[sentid] = {}
        dict[sentid][wordid] = functor
    else:
        print("WARNING: Cannot parse node id '%s'" % id)
    if not re.match(r"^[A-Z1-3]+$", functor):
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
            # More precisely, we assume that the word ids from PDT form a sequence
            # and correspond to our node ids (ords). This is in general quite risky
            # because the only guarantee about the PDT ids is that they are unique.
            # Multi-word tokens 'abych', 'abys', 'aby', 'abychom', 'abyste',
            # 'kdybych', 'kdybys', 'kdyby', 'kdybychom', 'kdybyste' might work
            # because they used to be split in PDT 1.0 and the word id of the
            # following word skips one position. But there are other types of
            # MWT in UD, and there might be other traps in PDT ids.
            nodes = root.descendants
            wids = [str(0)]
            wid = 1
            for node in nodes:
                wids.append(str(wid))
                ###!!! Here we should adjust the wid mapping to the fact that PDT
                ###!!! does not have MWTs. However, since some of them actually
                ###!!! existed as MWT in PDT 1.0, the adjustment would put us off!
                #if not node.multiword_token or node.ord == node.multiword_token.words[-1].ord:
                wid += 1
            for node in nodes:
                wid = wids[node.ord]
                if wid in dict[sid]:
                    node.misc['Functor'] = dict[sid][wid]
                    fullwid = sid+'w'+wid
                    node.misc['PDTId'] = fullwid
                    # Sanity check of the word form.
                    if fullwid in forms:
                        if node.form != forms[fullwid]:
                            print("WARNING: The UD form '%s' does not match the PDT form '%s' of the word id '%s'." % (node.form, forms[fullwid], fullwid))
                    else:
                        print("WARNING: Missing PDT form of the word id '%s'" % (fullwid))
    ###!!! If there are multiple documents in the input file, only the last one will survive on output.
    d.store_conllu('output.conllu') ### možná nahoře neimportovat reader, ale rovnou Document a vytvořit ho konstruktorem (filename=, viz dokumentace)
