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

sdist: clean sdist-core sdist-dot
	rm -rf dist
	mkdir dist
	cp */dist/* dist


# Core ---------------------------------------------------------------

install-core:
	cd ${CORE_DIR} && ./setup.py install

sdist-core: clean
	cd ${CORE_DIR} && ./setup.py sdist


# Dot ----------------------------------------------------------------

install-dot:
	cd ${DOT_DIR} && ./setup.py install

sdist-dot: clean
	cd ${DOT_DIR} && ./setup.py sdist


# Docs ---------------------------------------------------------------

docs: cleanpyc
	rm -rf ${DOCS_DIR} ${TEMP}
	mkdir -p ${TEMP}
	cp -R --remove-destination ${CORE_DIR}/pygraph ${TEMP}
	cp -Rn --remove-destination ${DOT_DIR}/pygraph/readwrite ${TEMP}/pygraph/
	epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--inheritance listed --no-private --html \
		--graph classtree \
		--css misc/epydoc.css -o docs ${TEMP}/pygraph/*.py \
		${TEMP}/pygraph/algorithms/*py \
		${TEMP}/pygraph/algorithms/heuristics/*.py \
		${TEMP}/pygraph/algorithms/filters/* \
		${TEMP}/pygraph/readwrite/* \
		${TEMP}/pygraph/classes/*.py \
		${TEMP}/pygraph/mixins/*.py
		rm -rf ${TEMP}


# Tests --------------------------------------------------------------

test:
	export PYTHONPATH=${PYTHONPATH} && cd ${TESTS_DIR} && python testrunner.py

test3:
	export PYTHONPATH=${PYTHONPATH} && cd ${TESTS_DIR} && python3 testrunner.py

tests: test


# Cleaning -----------------------------------------------------------

cleanpyc:
	find . -name *.pyc -exec rm {} \;

clean: cleanpyc
	rm -rf ${DOCS_DIR}
	rm -rf */dist
	rm -rf */build
	rm -rf */*.egg-info
	rm -rf dist


# Phony rules --------------------------------------------------------

.PHONY: clean cleanpyc docs-core
