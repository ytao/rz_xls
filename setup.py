import sys

from cx_Freeze import setup, Executable

# 只有在生成安装包时候才用这个，一般直接用"make out"
main_name="py_rz"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
	base = "Win32GUI"
setup(  name = main_name,
		version = "0.1",
		description = "My GUI application!",
		options = {"build_exe": build_exe_options},
		executables = [Executable(main_name+".py", base=base)])
