import sys
from cx_Freeze import setup, Executable
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "PyRouter",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PyRouter.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     "icWifi.ico",                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data#,"upgrade-code":"{96a85bac-52af-4019-9e94-3afcc9e1ad0c}"
                     }
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files": ["icWifi.ico",r'C:\Python27\tcl\tk8.5',r'C:\Python27\tcl\tcl8.5',r'C:\Users\brisatc435.souza\Documents\apks\git\PyRouter\router\icWifi.ico']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"



setup(  name = "PyRouter",
        version = "0.12",
        description = "Simple Virtual router made with python 2.x" ,
        options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
        author="Henrique Martins de Souza",
      #  shortcutName="PyRouter",
      #  shortcutDir="DesktopFolder",
        executables = [Executable("PyRouter.py", base=base ,targetName="PyRouter.exe",icon="icWifi.ico")])
