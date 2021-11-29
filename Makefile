test:
	nosetests

build:
	python setup.py sdist

build_and_upload:
	python setup.py sdist && twine upload dist/*

lint:
	pylint ./easybill_rest

fix:
	autopep8 --in-place --aggressive --aggressive --recursive ./easybill_rest/*.py
