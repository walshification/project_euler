ENV := $(CURDIR)/env


shell:
	$(ENV)/bin/ipython

test:
	$(ENV)/bin/coverage erase
	$(ENV)/bin/coverage run --rcfile=setup.cfg -m unittest discover
	$(ENV)/bin/coverage report --rcfile=setup.cfg
	$(ENV)/bin/coverage html --rcfile=setup.cfg; touch htmlcov

test-watch:
	$(ENV)/bin/sniffer

deps: env
	$(ENV)/bin/pip install -r requirements.txt

env:
	$(shell which python) -m venv $(ENV)


.PHONY: env
