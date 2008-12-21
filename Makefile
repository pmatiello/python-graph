none:

install: docs
	./setup.py develop -m

egg: docs
	./setup.py bdist_egg

docs: graph/*.py
	epydoc -v --no-frames --no-sourcecode --name="python-graph" --url="http://code.google.com/p/python-graph/" --no-private --html --css misc/epydoc.css -o docs graph/*.py

edit: graph/*.py
	gedit graph/__init__.py &
	gedit graph/*.py &
	
pypi: docs
	./setup.py bdist_egg upload
	
rpm: docs
	./setup.py bdist_rpm

clean: .
	rm -rf docs
	rm -rf dist
	rm -rf build
	rm -rf python_graph.egg-info
	rm graph/*.pyc
	rm graph/*/*.pyc
	rm -rf dist/*.egg
