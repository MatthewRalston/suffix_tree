# README

## Install
```bash
python setup.py install
```

## Usage

To build a simple suffix tree:

```python
from suffix_tree import SuffixTree
stree = SuffixTree('mississippi') 
```

You can now traverse the tree through a number of iterators: `leaves, innerNodes, preOrderNodes, and postOrderNodes`, that traverses all leaves, all inner nodes, all nodes in pre- and post-order, respectively:

```python
>>> for l in stree.leaves:
...     print l.pathLabel
...
mississippi$
ississippi$
issippi$
ippi$
i$
ssissippi$
ssippi$
sissippi$
sippi$
ppi$
pi$
$
```

The string representation of the tree is accessed as below:

```python
>>> stree.string
u'mississippi$'
```


A generalised suffix tree — a suffix tree representing a set of strings — can be constructed using the GeneralisedSuffixTree class:
```python
from suffix_tree import GeneralisedSuffixTree
sequences = ['mississippi','sippissi']
stree = GeneralisedSuffixTree(sequences)
```

In addition to the functionality of the simple suffix tree, the generalised suffix tree has a function for extracting all shared substrings of the set of strings, or all shared substrings of a given minimal length

```python
>>>for shared in stree.sharedSubstrings():
       print '-'*70
       for seq,start,stop in shared:
           print seq, '['+str(start)+':'+str(stop)+']',
           print sequences[seq][start:stop],
           print sequences[seq][:start]+'|'+sequences[seq][start:stop]+'|'+sequences[seq][stop:]
----------------------------------------------------------------------
0 [1:5] issi m|issi|ssippi
0 [4:8] issi miss|issi|ppi
1 [4:8] issi ispp|issi|
----------------------------------------------------------------------
0 [1:3] is m|is|sissippi
0 [4:6] is miss|is|sippi
1 [4:6] is ispp|is|si
1 [0:2] is |is|ppissi
----------------------------------------------------------------------

```
