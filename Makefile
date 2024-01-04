test:
	poetry run tox

install:
	poetry install

update:
	poetry lock
	poetry install

build:
	poetry build

publish:
	poetry build
	poetry publish

docs:
	poetry run tox -e docs
	xdg-open docs/_build/index.html

pin_docs_requirements:
	pip-compile --output-file=docs/requirements.txt docs/requirements.in pyproject.toml

.PHONY: test install update build publish docs pin_docs_requirements
