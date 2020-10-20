import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Menu ADM",
        version = "1.0",
        description = "Menu para acesso a funçoes adm",
        executables = [Executable("program.py",icon="icon.ico",targetName="Menu ADM",copyright="https://github.com/CarlosZanao")])

#Comando para compilar 
#> python setup.py build