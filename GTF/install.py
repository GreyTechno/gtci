#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess
import shutil
import pip
import json
import re
import requests
import threading
import zipfile
import random
import sys
import time
import platform


execute = lambda: "3" if (platform.system().lower() == "darwin") else ""



def AnimLOAD(text):
    for handlechar in "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏":
        sys.stdout.write(f"\r{handlechar} {text}")
        sys.stdout.flush()
        time.sleep(0.04)




def Install(reponame):
    Repository = requests.get("https://raw.githubusercontent.com/GreyTechno/Binaries/main/files/.repository").json()
    RootPath = pip.__path__[0]

    os.chdir(RootPath)
    os.chdir("..")
    try:os.chdir(".@GTFRepository90876")
    except FileNotFoundError:
        os.mkdir(".@GTFRepository90876")
        with open(".info", "w") as file : file.write("")
        os.chdir(".@GTFRepository90876")

    if not (reponame in Repository):
        DID = False
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: DID = True
        print(f"[!] Program not found '{reponame}'")
        if (DID): print(f"[+] Did you mean,\n")
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: print(f"    {repo}")
    else:
        source = Repository[reponame]['zipurl']
        dependencies = Repository[reponame]['dependencies']
        rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
        zipname = source.split("/")[4] +"-"+ source.split("/")[-1].split(".")[0]
        toolname = zipname.split("-")[0]
        if (reponame in os.listdir()):
            print("[!] '{}' already installed.".format(reponame))
        else:
            print(os.getcwd())
            def _():
                with open(f"{rname}.zip", "wb") as file: file.write(requests.get(source).content)
                with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
                os.remove(f"{rname}.zip")
                shutil.copytree(f"{os.getcwd()}/{rname}/{zipname}", toolname)
                shutil.rmtree(rname)
            install = threading.Thread(target=_)
            install.start()
            while install.is_alive(): AnimLOAD("Installing " + reponame + "...")
            install.join()
            sys.stdout.write(f"\r[+] {reponame} installed.  \n")
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive(): AnimLOAD("Installing Building Dependencies...")
            DEPENDENCIES.join()
            sys.stdout.write("\r[+] Installtion Completed.           \n")
            print("[-] For start >> 'gtf run {}'".format(reponame))