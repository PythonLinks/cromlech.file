# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.1'

install_requires = [
    'setuptools',
    'zope.component',
    'zope.interface',
    'zope.schema',
    'zope.size',
    ]

tests_require = [
    ]

setup(name='cromlech.file',
      version=version,
      description="A file representation core package for Cromlech",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Cromlech File',
      author='The Dolmen Team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech'],
      include_package_data=True,
      extras_require={'test': tests_require},
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
