test:
	poetry run tox

install:
	poetry install

# https://github.com/python-poetry/poetry/issues/34#issuecomment-1054626460
install_editable:
	pip install -e .

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
