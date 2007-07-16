docs:
	epydoc --name="python-graph" --url="http://code.google.com/p/python-graph/" --html -o docs graph/*

edit:
	gedit graph/*.py

clean:
	rm graph/*.pyc

example:
	python example.py
