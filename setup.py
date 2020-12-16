#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author   : lisztomania
# @Date     : 2020/12/16 19:33
# @Software : PyCharm
# @Version  : Python 3.9.1
# @Project  : LimitFunc
# @FileName : setup.py
# @Function :
import setuptools

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='LimitFunc',
    version='0.0.1',
    author='lisztomania',
    author_email='lisztomania@vip.qq.com',
    description='limit function args type',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lisztomania-Zero/LimitFunc',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
