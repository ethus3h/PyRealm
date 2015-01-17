from packet import *
import os
import sys
import importlib

__all__ = []

os.chdir("packets")

sys.path.append(os.getcwd())

modules = [x for x in os.listdir(".") if ".pyc" not in x]
    
modules.remove("__init__.py")
modules.remove("packet.py")

for name in modules:
    name = name.split(".")[0]
    className = name[0].upper() + name[1:] + "Packet"
    __all__.append(className)
    exec("from " + name + " import " + className)


os.chdir("..")
