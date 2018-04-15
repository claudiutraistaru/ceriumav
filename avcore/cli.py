import argparse
import os

from colorama import Fore, Style

import avcore.scanner as ns

_banner_ = "="*15 + " \tCerium AV Command Line Interface \t" + "="*15
_version_info_ = "\t\t\t\tVersion : 1.0\t\t\t"
_copyright_ = "\t\t\tCopyright (C) 2017 xedtech\t"
_help_ = """
input scan or '1' for scan a file or folder
help or h for this help
about or 0 to know about the applications
quit or qqq to exit
"""

debug = False
set_debug = False

def print_banner():
    print(Fore.GREEN + Style.BRIGHT + _banner_)
    print(Fore.RED + Style.BRIGHT + _version_info_)
    print(Fore.BLUE + Style.BRIGHT + _copyright_)
    print(Fore.GREEN + "="*71)
    print(Style.RESET_ALL)
    print(_help_)
    get_input()


def get_input():
    inp = str(input("#> "))
    if 'scan' or "SCAN" or 'Scan' or '1' in inp:
        path = str(input("path to scan > "))
        if not os.path.exists(path):
            print("File / Folder Does not Exists . . .")
            get_input()
        else:
            initscan(path)
    elif "help" or "h" or "HELP" in inp:
        print(Style.RESET_ALL)
        print(_help_)
        get_input()
    elif "about" or "0" or "ABOUT" in inp:
        print("Not yet ready")
        get_input()
    elif "quit" or "qqq" or "QUIT" or "QQQ" in inp:
        exit(0)
    else:
        get_input()


def initscan(path):
    ns.nu_scan_main(path)
    get_input()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scan", help = "Scan a file")
    args = parser.parse_args()
    if args.scan:
        initscan(args.scan)
    else:
        print_banner()

