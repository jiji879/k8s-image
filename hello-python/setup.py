#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='hello-python',  # 此处填写包名
    package_dir={'': '.'},
    packages=find_packages('.'),
    install_requires=[
        'tornado'
    ],
)
