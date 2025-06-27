.PHONY: install install-dev lint format run clean

install:
	pip install -e .

install-dev:
	pip install -e .[dev]

lint:
	ruff check src
	pyright src

format:
	black src

run:
	python -m HeatHaiku

clean:
	rm -rf build/
	rm -rf .ruff_cache
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -delete