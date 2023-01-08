#!/usr/bin/env python3

#import os
#from argparse import ArgumentParser

import re
import lxml.etree as ET # if not installed: /opt/python/3.9.7/bin/python3 -m pip install lxml

###!!! We will want to take the file names as command line arguments.
fname_tfile = 'cmpr9410_001.t' # gunzipped; at present we do not need the other files (.a, .m, .w); /net/data/pdt-c-1.0/data/PDT/pml/tamw/train-1 contains the gzipped files
fname_wfile = 'cmpr9410_001.w' # needed to sanity-check the word forms later when adding to UD

# We will have to provide the namespace when referring to elements.
ns = '{http://ufal.mff.cuni.cz/pdt/pml/}'

# Read the w-file and remember word forms for all word ids.
forms = {}
w_file = ET.parse(fname_wfile)
for w in w_file.findall('//' + ns + 'w'):
    wid = re.sub(r"^w-", '', w.get('id'))
    for child in w:
        if child.tag == ns + 'token':
            forms[wid] = child.text
            break

t_file = ET.parse(fname_tfile)

# Find all elements <lex.rf> in the PML namespace.
for lex_rf in t_file.findall('//' + ns + 'lex.rf'):
    wid = re.sub(r"^a#a-", '', lex_rf.text)
    form = '__UNKNOWN__'
    if wid in forms:
        form = forms[wid]
    # The parent element is <a> (groups all lex and aux references to a-tree).
    # The grandparent element is <LM> (list member of the list <children>, i.e., the element corresponding to a t-node).
    grandparent_element = lex_rf.getparent().getparent()
    for child in grandparent_element:
        if child.tag == ns + 'functor':
            print("%s\t%s\t%s" % (wid, child.text, form))
