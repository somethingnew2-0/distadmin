# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import distadmin
version = distadmin.__version__

setup(
    name='distadmin',
    version=version,
    author='',
    author_email='peter@drifty.com',
    packages=[
        'distadmin',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['distadmin/manage.py'],
)