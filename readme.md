# easybill_rest (py-ebrest)
[![Generic badge](https://img.shields.io/badge/Version-0.1.5-important.svg)]()
[![Generic badge](https://img.shields.io/badge/coverage-97%25-success.svg)]()
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-ebrest.svg)
![GitHub](https://img.shields.io/github/license/bolZer/py-ebrest.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/py-ebrest.svg)

`easybill_rest` is a library to work with the easybill REST API (https://www.easybill.de/api/) written in Python.

All Resources except are available.

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