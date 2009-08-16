# python-graph
# Makefile


# Module directories

CORE_DIR="core/"
DOT_DIR="dot/"
TESTS_DIR="_tests/"
PYTHONPATH="`pwd`/core:`pwd`/dot"


# General

nothing:

install: install-core

egg: egg-core

docs: docs-core


# Core
install-core:
	cd ${CORE_DIR} && ./setup.py install

egg-core: clean
	cd ${CORE_DIR} && ./setup.py bdist_egg


# Docs
docs: cleanpyc
	rm -rf docs
	epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--no-private --html --css misc/epydoc.css -o docs */pygraph/*.py \
		*/pygraph/algorithms/*py */pygraph/algorithms/heuristics/*.py \
		*/pygraph/algorithms/filters/* */pygraph/readwrite/* */pygraph/classes/*.py


# Tests
tests:
	export PYTHONPATH=${PYTHONPATH} && cd ${TESTS_DIR} && python testrunner.py

# Cleaning

cleanpyc:
	find . -name *.pyc -exec rm {} \;

clean: cleanpyc
	rm -rf */docs
	rm -rf */dist
	rm -rf */build
	rm -rf */*.egg-info
	rm -f */examples/*.png


# Phony rules

.PHONY: clean cleanpyc docs-core