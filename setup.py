#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: zhaofan
# Mail: damo120@vip.qq.com
# Created Time:  2021-1-21 21:30:00
#############################################


from setuptools import setup, find_packages

setup(
    name = "pyinfura",
    version = "0.0.1",
    keywords = ("pip", "infura","pyinfura", "infurapi", "pyinfurapi",'eth'),
    description = "easy to use infura api for eth",
    long_description = '',
    license = "MIT Licence",

    url = "https://github.com/index9-44/easymethod.git",
    author = "yizhang",
    author_email = "944057541@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)