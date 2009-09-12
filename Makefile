# python-graph
# Makefile


# Module directories -------------------------------------------------

CORE_DIR="core/"
DOT_DIR="dot/"
TESTS_DIR="tests/"
DOCS_DIR="docs/"
TEMP="temp/"
PYTHONPATH="`pwd`/core:`pwd`/dot"


# General ------------------------------------------------------------

nothing:

install: install-core

egg: egg-core

docs: docs-core


# Core ---------------------------------------------------------------

install-core:
	cd ${CORE_DIR} && ./setup.py install

egg-core: clean
	cd ${CORE_DIR} && ./setup.py bdist_egg


# Docs ---------------------------------------------------------------

docs: cleanpyc
	rm -rf ${DOCS_DIR} ${TEMP}
	mkdir -p ${TEMP}
	cp -R --remove-destination ${CORE_DIR}/pygraph ${TEMP}
	cp -R --remove-destination ${DOT_DIR}/pygraph/readwrite ${TEMP}/pygraph/
	epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--no-private --html --css misc/epydoc.css -o docs ${TEMP}/pygraph/*.py \
		${TEMP}/pygraph/algorithms/*py \
		${TEMP}/pygraph/algorithms/heuristics/*.py \
		${TEMP}/pygraph/algorithms/filters/* \
		${TEMP}/pygraph/readwrite/* \
		${TEMP}/pygraph/classes/*.py
		rm -rf ${TEMP}


# Tests --------------------------------------------------------------

test:
	export PYTHONPATH=${PYTHONPATH} && cd ${TESTS_DIR} && python testrunner.py

tests: test


# Cleaning -----------------------------------------------------------

cleanpyc:
	find . -name *.pyc -exec rm {} \;

clean: cleanpyc
	rm -rf ${DOCS_DIR}
	rm -rf */dist
	rm -rf */build
	rm -rf */*.egg-info
	rm -f */examples/*.png


# Phony rules --------------------------------------------------------

.PHONY: clean cleanpyc docs-core
