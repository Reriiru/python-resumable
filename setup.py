#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='python_resumable',
      version='0.1.0',
      description='Hook for working with resumable.js',
      author='Igor Velme <ivelmey@gmail.com>, Andrey Kasatov',
      author_email='ivelmey@gmail.com',
      license='MIT',
      keywords='resumablejs',
      install_requires=['natsort'],
      python_requires='>=3',
      url='https://github.com/Reriiru/python-resumable',
      packages=find_packages(),
      )
