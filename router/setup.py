import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files": [r'C:\Python27\tcl\tk8.5',r'C:\Python27\tcl\tcl8.5',r'C:\Users\brisatc435.souza\Documents\apks\git\Router_virtual_Python\router\icWifi.ico']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
#
setup(  name = "PyRouter",
        version = "0.3",
        description = "Simple Virtual router made with python 3" ,
        options = {"build_exe": build_exe_options},
        author="Henrique Martins de Souza",
        executables = [Executable("PyRouter.py", base=base)])
