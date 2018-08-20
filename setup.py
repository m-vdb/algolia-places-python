#!/usr/bin/env python

from setuptools import setup, find_packages


VERSION = '0.1'


setup(
    name='algolia-places-python',
    version=VERSION,
    description='Algolia Places Python (unofficial)',
    author='Maxime Vdb',
    author_email='me@maxvdb.com',
    packages=find_packages(),
    install_requires=['requests'],
    license="MIT",
    keywords="algolia places python api sdk",
    url='https://github.com/m-vdb/algolia-places-python',
    download_url='https://github.com/m-vdb/algolia-places-python/archive/v{}.tar.gz'.format(VERSION),
    project_urls={
        "Source Code": "https://github.com/m-vdb/algolia-places-python",
    }
)
