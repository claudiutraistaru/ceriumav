import os
from os import walk

import avcore.ext as ext
import avcore.cdb as cdb
from colorama import init, Fore, Style
import avcore.detector as dt

debug = False

total = 0


"""""
# adding some function for colorma:
stream = AnsiToWin32(sys.stderr).stream
"""

if "PYCHARM_HOSTED" in os.environ:
    init(convert=False, strip=False, wrap=False)
    if debug:
        print("Running on PyCharm")
else:
    init(convert=None, strip=None, wrap=False)
    if debug:
        print('running on Terminal')



def positive_alert(filename):
    print(Fore.RED + Style.BRIGHT + "[*] \t\tThreat Has Been Detected : {} \n[*]".format(str(filename)) +
          Fore.RED + Style.BRIGHT + "You Should Remove it")
    print(Style.RESET_ALL)
    global total
    total += 1


def init_scan(item):
    mal_ext = False;
    if  item in ext.exts:
        mal_ext = True
    sig = dt.detect(item)
    # print(sig)
    
    if sig in cdb.cdb_dict:
        positive_alert(item)
    else:
        if debug:
            print('[+] \t\tFound Clean alert on signature {}'.format(a))
    if mal_ext:
        print('[+] \t\tFound Malicious Extension, Maybe a Threat ')



def scanfiles_in_dir(directory):
    if os.path.exists(directory):
        for dirpath, dirname, filelist in walk(directory):
            print("Entering Directory : %s" % dirpath)
            for filename in filelist:
                print("\t [--] Scanning File :  %s" % filename)
                init_scan(os.path.join(dirpath) + "/" + filename)
    else:
        raise FileNotFoundError("Folder / Directory Can't be Found")


def scanfile_no_dir(filename):
    if os.path.exists(filename):
        init_scan(str(filename))
    else:
        raise FileNotFoundError("[X]  File Can't be Found ")


def nu_scan_main(path):
    if not os.path.isfile(path):
        scanfiles_in_dir(path)

    else:
        scanfile_no_dir(path)
    print(Fore.CYAN + Style.BRIGHT + "[++] \t Total Threats Detected  :  %d" % total)
    print(Style.RESET_ALL)

