#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='fileoperations_python',
      version='1.1.1',
      description='Basic file manipulations for python',
      author='Sertan Senturk',
      license='agpl 3.0',
      author_email='contact@sertansenturk.com',
      url='https://github.com/sertansenturk/fileoperations_python',
      packages=find_packages(exclude=["test"])
)
