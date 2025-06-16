#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pathlib import Path

version_path = Path(__file__).parent / "karton/utils/__version__.py"
version_info = {}
exec(version_path.read_text(), version_info)

setup(
    name="karton-utils",
    version=version_info["__version__"],
    url="https://github.com/cocoapuck/karton-utils/",
    description="Runs utils scan on files with Karton",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    namespace_packages=["karton"],
    packages=["karton.utils"],
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'karton-utils=karton.utils:Utils.main'
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)