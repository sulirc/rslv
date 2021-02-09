"""
CLI-Resolve(rslv): Make and resolve alias in CLI.

"""
import os

PWD = os.path.dirname(os.path.realpath(__file__))
RSLV_DIR = os.path.abspath(os.path.join(PWD, os.pardir))

__version__ = "0.1.0"
__author__ = "sulirc"
__delimiter__ = " => "
__cache_file__ = RSLV_DIR + "/.rslv.db"
