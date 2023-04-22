#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import pip
import json
import re
import platform



execute = lambda: "3" if (platform.system().lower() == "darwin") else ""


def Run(reponame):
    RootPath = pip.__path__[0]
    os.chdir(RootPath)
    os.chdir("..")
    try:os.chdir(".@GTFRepository90876")
    except FileNotFoundError: print("[!] There aren't any repositories installed."), exit()

    run = ""
    for repo in os.listdir():
        if (repo[0] == "."): continue
        elif (repo == reponame): 
            try:
                os.chdir(reponame)
                with open(".info") as file : run = json.loads(file.read())["main"]
            except : pass
        else: pass

    if not (run):
        Repository = os.listdir()
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
    else: os.system(f"python{execute()} {run}"), exit()
