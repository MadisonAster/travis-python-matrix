import os
from setuptools import setup

def readme():
    with open('README.md', 'r') as file:
        filetext = file.read()
    return filetext
setup(
    name='travis-python-matrix',
    version='0.0.3',
    description='Test Matrix for Travis and cibuildwheel.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    python_requires='>2.7.0',
    url='https://github.com/MadisonAster/travis-python-matrix',
    author='Madison Aster',
    author_email='info@MadisonAster.com',
    license='LGPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            #'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            ],

    keywords='travis cibuildwheel matrix',
    package_dir = {'': ''},
    packages=['TestPackage'],
)