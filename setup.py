#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (  # type: ignore
    setup,
    find_packages,
)

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0,<7.0",  # Core testing package
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
    ],
    "fuzz": [  # `fuzz` GitHub Action job uses this
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
    ],
    "lint": [
        "black>=20.8b1,<21.0",  # auto-formatter and linter
        "mypy>=0.800,<1.0",  # Static type analyzer
    ],
    "doc": [
        "Sphinx>=3.4.3,<4",  # Documentation generator
        "sphinx_rtd_theme>=0.1.9,<1",  # Readthedocs.org theme
        "towncrier>=19.2.0, <20",  # Generate release notes
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "setuptools-scm",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["fuzz"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["release"]
    + extras_require["dev"]
)

# NOTE: This comes after the previous so we don't have double dependencies
extras_require["fuzz"] = extras_require["test"] + extras_require["fuzz"]

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="<PYPI_NAME>",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="""<PYPI_NAME>: <SHORT_DESCRIPTION>""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/<REPO_NAME>",
    include_package_data=True,
    install_requires=[],  # NOTE: Add 3rd party libraries here
    python_requires=">=3.6,<4",
    extras_require=extras_require,
    py_modules=["<MODULE_NAME>"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"<MODULE_NAME>": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
