import os
os.system("sudo pacman -S python-pip")

import pip
from pip._internal import main as pipmain

def install(package):
    if hasattr(pip, 'main'):
        pipmain(['install', package])
    else:
        pip._internal.main(['install', package])

install('PyQt5')
install('PyQtWebEngine')
os.system("mv '/home/deck/Downloads/SDYA/YouTube App.desktop' '/home/deck/Desktop/YouTube App.desktop'")