#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suffix_tree import GeneralisedSuffixTree

# s1 = u'mississippi'
# s2 = u'sippissi'

s1 = u'一寸光阴一寸金';
s2 = u'寸金难买寸光阴';
stree = GeneralisedSuffixTree([s1,s2]) 

for shared in stree.sharedSubstrings(2):
    print '-'*70
    for (seq,start,stop) in shared:
       print seq, 
       print '['+str(start)+':'+str(stop)+']',
       ss = stree.sequences[seq][start:stop]
       print ss.encode('utf-8'),
       at = stree.sequences[seq][:start]+\
                    '{'+stree.sequences[seq][start:stop]+'}'+\
                    stree.sequences[seq][stop:]
       print at.encode('utf-8')
print '='*70 
