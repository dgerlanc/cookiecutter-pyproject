#!/usr/bin/env python

from setuptools import setup

import versioneer

setup(
    name="{{ cookiecutter.project_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    packages=["{{ cookiecutter.project_slug }}"],
    python_requires=">={{ cookiecutter.python_version }}",
    tests_require=["pytest"]
)
