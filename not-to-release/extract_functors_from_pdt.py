#!/usr/bin/env python3

#import os
#from argparse import ArgumentParser

import lxml.etree as ET # if not installed: /opt/python/3.9.7/bin/python3 -m pip install lxml

###!!! We will want to take the file names as command line arguments.
fname_tfile = 'cmpr9410_001.t' # gunzipped; at present we do not need the other files (.a, .m, .w); /net/data/pdt-c-1.0/data/PDT/pml/tamw/train-1 contains the gzipped files

t_file = ET.parse(fname_tfile)

# Find all elements <lex.rf> in the PML namespace.
for lex_rf in t_file.findall('//{http://ufal.mff.cuni.cz/pdt/pml/}lex.rf'):
    # The parent element is <a> (groups all lex and aux references to a-tree).
    # The grandparent element is <LM> (list member of the list <children>, i.e., the element corresponding to a t-node).
    grandparent_element = lex_rf.getparent().getparent()
    for child in grandparent_element:
        if child.tag == '{http://ufal.mff.cuni.cz/pdt/pml/}functor':
            print("%s\t%s" % (lex_rf.text, child.text))

###!!! check words in UD and PDT
