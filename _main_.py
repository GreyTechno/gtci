#!/usr/bin/python
# -*- coding: UTF-8 -*-

import install
import run





import sys


def main():
    try: command = sys.argv[1]
    except: command = False
    try: arguments = sys.argv[2]
    except: arguments = ""
    try: arguments_01 = sys.argv[3:]
    except: arguments_01 = ""
    if (command):
        if (command == "install") or (command == "-install") or (command == "--install"):
            install.Install(arguments)
        # elif (command == "uninstall") or (command == "-uninstall") or (command == "--uninstall"): pass
        # elif (command == "download") or (command == "-download") or (command == "--download"): pass
        # elif (command == "update") or (command == "-update") or (command == "--update"): print("update")
        elif (command == "run") or (command == "-run") or (command == "--run"):
            run.Run(arguments)
        # elif (command == "list") or (command == "-list") or (command == "--list"): print("list")
        # elif (command == "about") or (command == "-about") or (command == "--about"): pass
        # elif (command == "show") or (command == "-show") or (command == "--show"): pass
        # elif (command == "help") or (command == "-help") or (command == "--help"): pass
        else: print(f"ERROR : Command not found '{command}'\nShow help 'gtf -h'")
if __name__ == "__main__":
    main()