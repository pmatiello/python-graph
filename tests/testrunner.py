import sys
sys.path.append('..')
import pygraph
import unittest
import testlib
from os import listdir

def test_modules():
    modlist = []
    for each in listdir('.'):
        if (each[0:9] == "unittests" and each[-3:] == ".py"):
            modlist.append(each[0:-3])
    return modlist

def run_tests():
    for each_size in testlib.sizes:
        
        print
        print "Testing with %s graphs" % each_size
        print
        
        suite = unittest.TestSuite()
        testlib.use_size = each_size
        
        for each_module in test_modules():
            suite.addTests(unittest.TestLoader().loadTestsFromName(each_module))
        
        tr = unittest.TextTestRunner(verbosity=2)
        result = tr.run(suite)
        del suite
       
if __name__ == "__main__":
    run_tests()