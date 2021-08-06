test:
	nosetests

build:
	python setup.py sdist

build_and_upload:
	python setup.py sdist && twine upload dist/*

