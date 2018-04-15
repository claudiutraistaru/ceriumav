"""
have directory info and also os info
"""

import os
import  platform

__author__ =  "Palash Bauri"
__version__ = [0, 0, 0, 1]
__copyright__ = "(c) Palash Bauri"

if platform.system() in ['Linux', 'linux', 'posix', 'unix']:
    linux = True
    win = False
elif platform.system() in ['Windows', 'windows']:
    win = True
    linux = False
else:
    raise Exception("Your Operating System isn't currently supported by Neutron. Working on it. . .")

home = os.path.expanduser('~')

sysbin_dir = ("{0}\Windows\system32".format(home) if win else "/sbin")

startup_dir = ("{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(home) if win else "/etc/init.d")

downloads_dir = ("{0}\Downloads".format(home) if win else "{0}/Downloads".format(home))
