import setuptools
from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="easybill_rest",
    author="Jan Noehles (bolZer)",
    include_package_data=True,
    author_email="noehles@easybill.de",
    description="easybill_rest is a library to work with the easybill REST API (https://www.easybill.de/api/)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BolZer/py-ebrest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.11.0',
    version="0.4.0",
    install_requires=[
            "requests",
    ],
    extras_require={
        'dev': [
            "coverage<5",
            "wheel",
            "pytest<8",
        ]
    }
)
