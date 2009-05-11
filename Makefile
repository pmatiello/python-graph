none:

install:
	./setup.py install

egg: clean
	./setup.py bdist_egg

docs: cleanpyc
	rm -rf docs
	epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--no-private --html --css misc/epydoc.css -o docs graph/*.py \
		graph/algorithms/*py graph/algorithms/heuristics/*.py \
		graph/algorithms/filters/* graph/classes/*.py

test:
	./setup.py test

cleanpyc:
	rm -f graph/*.pyc
	rm -f graph/*/*.pyc
	rm -f graph/*/*/*.pyc
	rm -f tests/*.pyc

clean: cleanpyc
	rm -rf docs
	rm -rf dist
	rm -rf build
	rm -rf python_graph.egg-info

.PHONY: clean cleanpyc docs