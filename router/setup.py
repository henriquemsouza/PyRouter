import sys
from cx_Freeze import setup, Executable
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files": ["icWifi.ico",r'C:\Python27\tcl\tk8.5',r'C:\Python27\tcl\tcl8.5',r'C:\Users\brisatc435.souza\Documents\apks\git\PyRouter\router\icWifi.ico']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "PyRouter",
        version = "0.7",
        description = "Simple Virtual router made with python 2.x" ,
        options = {"build_exe": build_exe_options},
        author="Henrique Martins de Souza",
      #  shortcutName="PyRouter",
      #  shortcutDir="DesktopFolder",
        executables = [Executable("PyRouter.py", base=base, targetName="PyRouter.exe", shortcutName="PyRouter", shortcutDir="DesktopFolder",icon="icWifi.ico")])
