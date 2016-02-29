from distutils.core import setup
from glob import glob
import py2exe,sys

if len(sys.argv)==1:
    sys.argv.append("py2exe")
    #sys.argv.append("-q")


setup(windows=["dcv4.py"])
