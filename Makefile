# python-graph
# Makefile

# Module directories
CORE_DIR="python-graph-core/"
DOT_DIR="python-graph-dot/"

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

docs-core: cleanpyc
	cd ${CORE_DIR} && rm -rf docs
	cd ${CORE_DIR} && epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--no-private --html --css misc/epydoc.css -o docs pygraph/*.py \
		pygraph/algorithms/*py pygraph/algorithms/heuristics/*.py \
		pygraph/algorithms/filters/* pygraph/readwrite/* pygraph/classes/*.py

test-core:
	cd ${CORE_DIR} && cd tests && python testrunner.py


# Cleaning

cleanpyc:
	rm -f */pygraph/*.pyc
	rm -f */pygraph/*/*.pyc
	rm -f */pygraph/*/*/*.pyc
	rm -f */tests/*.pyc

clean: cleanpyc
	rm -rf */docs
	rm -rf */dist
	rm -rf */build
	rm -rf */*.egg-info
	rm -f */examples/*.png

# Phony rules
.PHONY: clean cleanpyc docs-core