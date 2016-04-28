#!/bin/env python

from distutils.core import setup, Extension

_suffix_tree = Extension('_suffix_tree',['python_bindings.c',
                                         'suffix_tree.c'])

setup(name="suffix_tree",
      version="2.2",
      description="""
      A python suffix tree (for easy algorithmic prototyping) with Unicode support.
      """,

      author="Dell Zhang",     author_email="dell.z@ieee.org",
      maintainer="Dell Zhang", maintainer_email="dell.z@ieee.org",
      contact="Dell Zhang",    contact_email="dell.z@ieee.org",
      url='http://researchonsearch.blogspot.com/2010/05/suffix-tree-implementation-with-unicode.html',

      scripts=[],
      py_modules=["suffix_tree"],
      ext_modules=[_suffix_tree],
      )
