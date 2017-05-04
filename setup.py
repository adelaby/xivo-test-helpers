#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2015-2016 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup
from setuptools import find_packages

VERSION = '0.1.7'

setup(
    name='xivo-test-helpers',
    version=VERSION,

    description='XiVO test helpers',

    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',

    url='http://wazo.community',

    packages=find_packages(),
    install_requires=['docker'],
    download_url='https://github.com/wazo-pbx/xivo-test-helpers/tarball/{}'.format(VERSION),
)
