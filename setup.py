#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='runehistory',
    version='0.0.1',
    description='RuneHistory CLI application to pull player highscores',
    author='Jim Wright',
    author_email='jmwri93@gmail.com',
    packages=find_packages(),
    install_requires=[
        'cement>=2.10.0,<2.11',
        'requests>=2.18,<3'
    ],
    entry_points={
        'console_scripts': [
            'runehistory=runehistory.cli.app:run'
        ],
    },
)

