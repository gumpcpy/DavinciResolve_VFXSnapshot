'''
Before Install:

'''
#1- You must have Davinci Resolve 17 versoin or above
#2- Install Python 3.9 and use virtual environment

#3- Install Below Packages
pip install shutil
pip install calendar
pip install re
pip install shutil


#4- To Test APP
pythonw vfxsnap.py

'''Mac Will Need python.app conda install -c conda-forge python.app
'''

#5- Generate APP 
python setup.py py2app

#6- Edit setup.py While Needed

'''
# setup.py
from setuptools import setup

APP = ['vfxsnap.py']
DATA_FILES = []
OPTIONS = {'iconfile':'Icon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
'''

#7- Generate APP with or without -A flag
python setup.py py2app --includes=gump1fclass,python_get_resolve -A

 
