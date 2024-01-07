import sys, os
from cx_Freeze import Executable, setup

os.environ["TCL_LIBRARY"] = "tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "tcl\\tk8.6"

build_exe_options = {"packages": ["os", "tkinter", "babel.numbers", "time", "PIL", "tk"]
    , "include_files": ["tcl86t.dll", "tk86t.dll"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( name = "Hospital Management Systems",
       version = "1.0",
       description = "This software can be used in small scale hospital management...",
       option = {"build_exe": build_exe_options},
       executables = [Executable("Login_page.py", base = base)])