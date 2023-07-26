test:
	pytest

build:
	python setup.py sdist

build_and_upload:
	python setup.py sdist && twine upload dist/*

static_type_checker:
	mypy --ignore-missing-imports ./easybill_rest/resources/ ./easybill_rest/__init__.py ./easybill_rest/helper.py

lint:
	pylint ./easybill_rest --rcfile=./pylint.rc

fix:
	autopep8 --in-place --aggressive --aggressive --recursive ./easybill_rest/
