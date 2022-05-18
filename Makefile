PHONY: help clean install

venv: ## Create virtual environment for Python dependencies
	python -m venv .venv

install: venv ## Install requirements into venv
	(source $(CURDIR)/.venv/bin/activate; \
	pip install -r requirements.txt;)

clean: ## Remove build artifacts
	./pyclean.sh
	rm -rf htmlcov/
	rm -rf .venv/

help: ## Show help for commands with help comments.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
