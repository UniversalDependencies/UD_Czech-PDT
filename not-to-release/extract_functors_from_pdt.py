#!/usr/bin/env python3

#import os
#import re
#from argparse import ArgumentParser
#from collections import defaultdict

import lxml.etree as ET

t_file = ET.parse('./Sample/cmpr9410_001.t')

for lex_rf in t_file.findall('//{http://ufal.mff.cuni.cz/pdt/pml/}lex.rf'):
    #print(lex_rf.text)
    parent_element = lex_rf.getparent().getparent()
    for child in parent_element:
        if child.tag == '{http://ufal.mff.cuni.cz/pdt/pml/}functor':
            print(lex_rf.text, '\t', child.text)
# check words in UD and PDT
