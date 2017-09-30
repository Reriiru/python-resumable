#!/usr/bin/env python

from distutils.core import setup

setup(name='python_resumable',
      version='0.1.0',
      description='Hook for working with resumable.js',
      author='Igor Velme <ivelmey@gmail.com>, Andrey Kasatov',
      author_email='ivelmey@gmail.com',
      license='MIT',
      keywords='resumablejs',
      install_requires=['natsort'],
      url='',
      package_dir={
          'python_resumable': 'python_resumable',
          'python_resumable.models': 'python_resumable/models'
      },
      packages=['python_resumable', 'python_resumable.models'],
      )
