# Backdoor builder
from distutils.core import setup
import py2exe

setup(  
        console=['m09p04.py'],
        options = {'py2exe':{'bundle_files':1}},
        zipfile = None,
     )