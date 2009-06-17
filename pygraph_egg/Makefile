none:

install:
	./setup.py install

egg: clean
	./setup.py bdist_egg

docs: cleanpyc
	rm -rf docs
	epydoc -v --no-frames --no-sourcecode --name="python-graph" \
		--url="http://code.google.com/p/python-graph/" \
		--no-private --html --css misc/epydoc.css -o docs pygraph/*.py \
		pygraph/algorithms/*py pygraph/algorithms/heuristics/*.py \
		pygraph/algorithms/filters/* pygraph/readwrite/* pygraph/classes/*.py

test:
	./setup.py test

cleanpyc:
	rm -f pygraph/*.pyc
	rm -f pygraph/*/*.pyc
	rm -f pygraph/*/*/*.pyc
	rm -f tests/*.pyc

clean: cleanpyc
	rm -rf docs
	rm -rf dist
	rm -rf build
	rm -rf python_graph.egg-info
	rm -f examples/*.png

.PHONY: clean cleanpyc docs