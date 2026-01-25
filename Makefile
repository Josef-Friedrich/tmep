# test:
# 	poetry run tox

# install:
# 	poetry install

# # https://github.com/python-poetry/poetry/issues/34#issuecomment-1054626460
# install_editable:
# 	pip install -e .

# update:
# 	poetry lock
# 	poetry install

# build:
# 	poetry build

# publish:
# 	poetry build
# 	poetry publish

# docs:
# 	poetry run tox -e docs
# 	xdg-open docs/_build/index.html

# pin_docs_requirements:
# 	pip-compile --output-file=docs/requirements.txt docs/requirements.in pyproject.toml

# .PHONY: test install update build publish docs pin_docs_requirements

all: test format docs lint type_check

test:
	uv run --isolated --python=3.8 pytest
	uv run --isolated --python=3.9 pytest
	uv run --isolated --python=3.10 pytest
	uv run --isolated --python=3.11 pytest
	uv run --isolated --python=3.12 pytest
	uv run --isolated --python=3.13 pytest

test_quick:
	uv run --isolated --python=3.12 pytest

install: update

install_editable: install
	uv pip install --editable .

update:
	uv sync --upgrade

build:
	uv build

publish:
	uv build
	uv publish

format:
	uv run ruff check --select I --fix .
	uv run ruff format

docs:
	uv run --isolated readme-patcher
	rm -rf docs/_build
	uv tool run --isolated --from sphinx --with . --with sphinx_rtd_theme sphinx-build -W -q docs docs/_build
	xdg-open docs/_build/index.html

pin_docs_requirements:
	uv run pip-compile --strip-extras --output-file=docs/requirements.txt docs/requirements.in pyproject.toml

lint:
	uv run ruff check

type_check:
	uv run mypy src/tmep tests

.PHONY: test install install_editable update build publish format docs lint pin_docs_requirements
