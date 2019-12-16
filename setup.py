#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

extras_require = {
    "test": [
        "pytest>=4.6.3,<5.0.0",
        "pytest-xdist>=1.30.0,<2",
        "pytest-asyncio>=0.10.0,<1.0.0",
        "factory-boy>=2.12.0,<3.0.0",
        "p2pclient",
        "pexpect"
    ],
    "lint": [
        "flake8==3.7.9",  # flake8 is not semver: it has added new warnings at minor releases
        "isort==4.3.21",
        "mypy==0.740",  # mypy is not semver: it has added new warnings at minor releases
        "mypy-protobuf==1.15",
        "black==19.3b0",
        "flake8-bugbear>=19.8.0,<20",
        "docformatter>=1.3.1,<2",
    ],
    "doc": [
        "Sphinx>=2.2.1,<3",
        "sphinx_rtd_theme>=0.4.3,<=1",
        "towncrier>=19.2.0, <20",
    ],
    "dev": [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
        "setuptools>=36.2.0",
        "tox>=3.13.2,<4.0.0",
        "eth_utils"
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
)

fastecdsa = [
      # No wheels defined for Windows (for fastecdsa), using a modded version (of 1.7.5) that includes the right
      # libraries to build a wheel with.
      # Fixme: remove section when fastecdsa has released a windows-compatible wheel (win32 and win_amd64)
      # Fixme: See the following issues;
      # Fixme: https://github.com/libp2p/py-libp2p/issues/363
      # Fixme: https://github.com/AntonKueltz/fastecdsa/issues/11
      "fastecdsa@git+https://github.com/shadowjonathan/fastecdsa-any@51164b711e955e81bdbc8a7b49aa81239b38ad78"
      " ;platform_system=='Windows'",

      # Wheels are provided for these platforms.
      "fastecdsa==1.7.5;platform_system!='Windows'",
]


with open("./README.md") as readme:
    long_description = readme.read()


install_requires = [
    "pycryptodome>=3.9.2,<4.0.0",
    "base58>=1.0.3,<2.0.0",
    "pymultihash>=0.8.2",
    "multiaddr>=0.0.8,<0.1.0",
    "rpcudp>=3.0.0,<4.0.0",
    "lru-dict>=1.1.6",
    "protobuf>=3.10.0,<4.0.0",
    "coincurve>=10.0.0,<11.0.0",
    "pynacl==1.3.0",
    "dataclasses>=0.7, <1;python_version<'3.7'",
    "async_generator==1.10",
]


# NOTE: Some dependencies break RTD builds. We can not install system dependencies on the
# RTD system so we have to exclude these dependencies when we are in an RTD environment.
readthedocs_is_building = os.environ.get("READTHEDOCS", False)
if not readthedocs_is_building:
    install_requires.extend(fastecdsa)


setup(
    name="libp2p",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.1.4",
    description="libp2p implementation written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="The Ethereum Foundation",
    maintainer_email="snakecharmers@ethereum.org",
    url="https://github.com/libp2p/py-libp2p",
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.6,<4",
    extras_require=extras_require,
    py_modules=["libp2p"],
    license="MIT/APACHE2.0",
    zip_safe=False,
    keywords="libp2p p2p",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    platforms=["unix", "linux", "osx"],
)
