docs: graph/*.py
	epydoc -v --no-frames --name="python-graph" --url="http://code.google.com/p/python-graph/" --html -o docs graph/*.py

edit: graph/*.py
	gedit graph/*.py &

clean: graph/*.pyc
	rm graph/*.pyc

example: example.py
	python example.py
