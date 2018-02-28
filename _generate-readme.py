#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import tmep


def path(*path_segments):
    return os.path.join(os.getcwd(), *path_segments)


def open_file(*path_segments):
    file_path = path(*path_segments)
    open(file_path, 'w').close()
    return open(file_path, 'a')


header = open(path('README_header.rst'), 'r')
readme = open_file('README.rst')
sphinx = open_file('doc', 'source', 'functions.rst')

sphinx_header = (
    'Functions\n',
    '=========\n',
    '\n',
    '.. code-block:: text\n',
    '\n',
)

for line in sphinx_header:
    sphinx.write(str(line))


for line in header:
    readme.write(line)

function_docs = tmep.doc.Doc().get()

readme.write('\n')

for line in function_docs.split('\n'):
    #indented_line = '    ' + line.decode('utf-8')
    readme.write(line + '\n')
    sphinx.write(line + '\n')


readme.close()
sphinx.close()
