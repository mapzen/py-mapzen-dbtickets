#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.dbtickets',
    namespace_packages=['mapzen', 'mapzen.dbtickets'],
    version='0.01',
    description='Simple Python wrapper for talking to a ticket server',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-dbtickets',
    install_requires=[
        'mysql.connector',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-utils/releases/tag/v0.01',
    license='BSD')
