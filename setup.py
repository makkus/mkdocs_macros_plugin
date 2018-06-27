# --------------------------------------------
# Setup file for the package
#
# Laurent Franceschetti (c) 2018
# --------------------------------------------

import os
from setuptools import setup, find_packages


def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-macros-plugin',
    version='0.0.1',
    description="Unleash the power of MkDocs with macros and variables",
    long_description=read_file('README.md'),
    keywords='mkdocs python markdown macros',
    url='www.settlenext.com',
    author='Laurent Franceschetti',
    author_email='info@settlenext.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=0.17',
        'repackage',
        'jinja2',
        'mkdocs'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'macros = macros.plugin:MacrosPlugin'
        ]
    }
)