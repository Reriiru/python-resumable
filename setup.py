#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='python_resumable',
      version='0.1.2',
      description='Hook for working with resumable.js',
      author='Igor Velme <ivelmey@gmail.com>, Andrey Kasatov',
      author_email='ivelmey@gmail.com',
      license='MIT',
      keywords='resumablejs',
      install_requires=['natsort'],
      python_requires='>=3',
      long_description=long_description,
      url='https://github.com/Reriiru/python-resumable',

      package_data={
        '': ['*.txt', '*.rst', '*.md'],
      },

      packages=find_packages(),
)
