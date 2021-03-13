import os
import json

try:
    import keyboard
except ImportError:
    print("A module is not existing. Installing module: keyboard")
    os.system("python -m pip install keyboard")
    import keyboard
try:
    import pymem
    import pymem.process
except ImportError:
    print("A module is not existing. Installing module: pymem")
    os.system("python -m pip install pymem")
    import pymem
    import pymem.process

try:
    import psutil
except ImportError:
    print("A module is not existing. Installing module: psutil")
    os.system("python -m pip install psutil")
    import psutil

try:
    import time
    from time import sleep
except ImportError:
    print("A module is not existing. Installing module: time")
    os.system("python -m pip install time")
    import time
    from time import sleep

try:
    import re
except ImportError:
    print("A module is not existing. Installing module: re")
    os.system("python -m pip install re")
    import re

try:
    from termcolor import colored, cprint
except ImportError:
    print("A module is not existing. Installing module: termcolor")
    os.system("python -m pip install termcolor")
    from termcolor import colored, cprint

try:
    import requests
except ImportError:
    print("A module is not existing. Installing module: requests")
    os.system("python -m pip install requests")
    import requests

try:
    from datetime import datetime
except ImportError:
    print("A module is not existing. Installing module: datetime")
    os.system("python -m pip install datetime")
    from datetime import datetime

try:
    from win32gui import GetWindowText, GetForegroundWindow
    import win32api
except ImportError:
    print("A module is not existing. Installing module: pywin32")
    os.system("python -m pip install pywin32")
    from win32gui import GetWindowText, GetForegroundWindow
    import win32api

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *