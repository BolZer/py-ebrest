# easybill_rest (py-ebrest)
[![Generic badge](https://img.shields.io/badge/Version-0.3.0-important.svg)]()
[![Generic badge](https://img.shields.io/badge/coverage-97%25-success.svg)]()
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/easybill_rest.svg)
[![Generic badge](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Build Status](https://travis-ci.com/BolZer/py-ebrest.svg?branch=master)](https://travis-ci.com/BolZer/py-ebrest)

`easybill_rest` is a library to work with the easybill REST API (https://www.easybill.de/api/) written in Python.

All Resources are available.

The library supports only the `Bearer` Authentication and calls the API only
through `HTTPS`.

```bash
pip install easybill_rest
```


## Usage

```Python
from easybill_rest import Client


client = Client("API-KEY")
result = client.documents().get_document("2")

# Returns the document model. Therefore a field "title" is included in the dict.
print(result['title'])

```