import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
# html_theme = 'alabaster'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

project = u'tmep'
copyright = u'2016, Josef Friedrich'
author = u'Josef Friedrich'
version = u'0.0.3'
release = u'0.0.3'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = []
htmlhelp_basename = 'tmepdoc'

latex_elements = {
     'papersize': 'a4paper',
     'pointsize': '11pt',
}

latex_documents = [
    (master_doc, 'tmep.tex', u'tmep Documentation',
     u'Josef Friedrich', 'manual'),
]

man_pages = [
    (master_doc, 'tmep', u'tmep Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'tmep', u'tmep Documentation',
     author, 'tmep', 'Template and Macros Expansion for Path names.',
     'Miscellaneous'),
]
