ENV := $(CURDIR)/env


shell:
	$(ENV)/bin/ipython

test:
	$(ENV)/bin/coverage erase
	$(ENV)/bin/coverage run --rcfile=setup.cfg -m unittest discover
	$(ENV)/bin/coverage report --rcfile=setup.cfg
	$(ENV)/bin/coverage html --rcfile=setup.cfg; touch htmlcov
	$(ENV)/bin/flake8

test-watch:
	$(ENV)/bin/sniffer

deps: env
	$(ENV)/bin/pip install -r requirements/base.txt
	$(ENV)/bin/pip install -r requirements/dev.txt

ci-deps:
	pip install -r requirements/base.txt

ci-test:
	coverage run --rcfile=setup.cfg -m unittest discover
	coverage report
	flake8

env:
	$(shell which python) -m venv $(ENV)

clean:
	rm -rf env



.PHONY: env, shell, test, test-watch, deps, ci-deps, ci-test
