"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['P2PP.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
           "iconfile": "favicon.icns",
           "includes": ['PyQt5._qt']}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
