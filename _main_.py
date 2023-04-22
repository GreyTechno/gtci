#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import shutil
import os
import pip
import zipfile
import random

from .GTF import install
from .GTF import run





__VERSION__ = "0.0.6"

source = "https://github.com/GreyTechno/gtf/archive/refs/heads/main.zip"
main = "mrdoxmrgt"


def Release():
    os.chdir(pip.__path__[0])
    os.chdir("..")

    try: shutil.rmtree(main)
    except FileNotFoundError: pass

    rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 15))
    zipname = source.split("/")[4] +"-"+ source.split("/")[-1].split(".")[0]

    with open(f"{rname}.zip", "wb") as file: file.write(requests.get(source).content)
    with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
    os.remove(f"{rname}.zip")

    shutil.copytree(f"{os.getcwd()}/{rname}/{zipname}", main)
    shutil.rmtree(rname)





version = requests.get("https://raw.githubusercontent.com/GreyTechno/gtf/main/.info").json()["version"]
if (__VERSION__ != version): Release()











def main():
    try: command = sys.argv[1]
    except: command = False

    try: arguments = sys.argv[2]
    except: arguments = ""

    try: arguments_01 = sys.argv[3:]
    except: arguments_01 = ""
    if (command):
        if (command == "install") or (command == "-install") or (command == "--install") or (command == "--clone") or (command == "--clone") or (command == "--clone"):
            install.Install(arguments)
        # elif (command == "uninstall") or (command == "-uninstall") or (command == "--uninstall"): pass
        # elif (command == "download") or (command == "-download") or (command == "--download"): pass
        # elif (command == "update") or (command == "-update") or (command == "--update"): print("update")
        elif (command == "run") or (command == "-run") or (command == "--run") or (command == "--start") or (command == "--start") or (command == "--start"):
            run.Run(arguments)
        # elif (command == "list") or (command == "-list") or (command == "--list"): print("list")
        # elif (command == "about") or (command == "-about") or (command == "--about"): pass
        # elif (command == "show") or (command == "-show") or (command == "--show"): pass
        # elif (command == "help") or (command == "-help") or (command == "--help"): pass
        else: print(f"ERROR : Command not found '{command}'\nShow help 'gtf -h'")
if __name__ == "__main__":
    main()