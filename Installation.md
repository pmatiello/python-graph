## Automated Install (with Distribute) ##

The Distribute package provides a utility called **easy\_install** which greatly simplifies the process of installing python-graph. If the easy\_install command is not available on your system refer to the section **Installing Distribute** before continuing.

```
# easy_install python-graph-core
```

And, optionally, for Dot-Language support (requires pydot):
```
# easy_install python-graph-dot
```

## Installing Distribute ##

[Distribute](http://pypi.python.org/pypi/distribute) is the standard tool for both packaging and installing Python packages. It replaces an older tool, Setuptools providing an identical set of features. Currently you can use either Distribute or Setuptools to both build and install python-graph, however in future we will be testing and supporting only the Distribute platform.

Distribute is provided only as source code. The project's maintainers provide a script to automate the installation process. Official installation instructions can be found on this page: http://pypi.python.org/pypi/distribute

### On UNIX like platforms ###

If your system has the curl utility you can quickly download the distribute\_setup.py script and install the tool:

```
# curl -O http://python-distribute.org/distribute_setup.py
# python distribute_setup.py
```

Note that on UNIX systems the "python" command will refer to your computer's default python interpreter. This may not be a version which the python-graph team actively support. You can specify exactly which platform Distribute is installed for like this:

```
sudo python3.1 distribute_setup.py
sudo python2.6 distribute_setup.py
```

### On Windows platforms ###

Simply download the distribute\_setup.py script and execute it from a cmd.exe prompt:

```
c:\python26\python.exe distribute_setup.py
```