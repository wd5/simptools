# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.6'

setup(
    version=VERSION,
    packages=find_packages(),
    name='simptools',
    author='Razzhivin Alexander',
    author_email='admin@httpbots.com',
    description='Simptools is a suit with useful functions for daily usage',
    url='http://github.com/RANUX/simptools',
    license = 'LGPL',
    platforms=['any'],
    include_package_data=True,
    install_requires = ['requests',],
    test_suite='tests',
    tests_require=['nose', 'testfixtures','py-moneyed>=0.3', 'Flask']
)
