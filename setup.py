#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='QuizzGame',
    version='1.0',
    author='ad-713',
    license='MIT',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=[
        'colorama>=0.4.4',
    ],
    entry_points={
        'console_scripts': [
            'quiz-game=quiz_code.main:main',
        ],
    },
)