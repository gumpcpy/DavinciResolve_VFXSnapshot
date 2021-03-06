"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
    
    
    python setup.py py2app --includes=gump1fclass,python_get_resolve -A
    
"""

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
