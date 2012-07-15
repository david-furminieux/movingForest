#!/usr/bin/python
from setuptools import setup, find_packages
setup(
    name = "MovingForest",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
#    scripts = [],
#
#    # Project uses reStructuredText, so ensure that the docutils get
#    # installed or upgraded on the target machine
    install_requires = ['antlr_python_runtime==3.1.3'],
#
#    package_data = {
#        # If any package contains *.txt or *.rst files, include them:
#        '': ['*.txt', '*.rst'],
#        # And include any *.msg files found in the 'hello' package, too:
#        'hello': ['*.msg'],
#    },
#
    # metadata for upload to PyPI
    author = "David G.R.C Furminieux",
    #author_email = "",
    description = "MovingForest: a Tree Stream processing System",
    license = "LGPL",
    #keywords = "",
    #url = "http://example.com/HelloWorld/",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)

                                                                                                            