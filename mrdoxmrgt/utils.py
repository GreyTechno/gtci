#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
import pip
import zipfile
import random
import requests
import sys
import json
import subprocess
import threading
import time
import platform
import re



source = "https://github.com/GreyTechno/gtf/archive/refs/heads/main.zip"
MainSource = "gtf"

execute = lambda: "3" if (platform.system().lower() == "darwin") else ""
currentpath = os.getcwd()
__VERSION__ = "0.0.5"


def color():
    global black,reset,blue,red,yellow,green,cyan,white,magenta,lightblack,lightblue,lightcyan,lightgreen,lightmagenta,lightred,lightwhite,lightyellow
    if (subprocess.getoutput("printf \"color\"") == "color") :
        black = '\033[30m'
        reset = '\033[39m'
        blue = '\033[34m'
        red = '\033[31m'
        yellow = '\033[92m'
        green = '\033[32m'
        cyan = '\033[36m'
        white = '\033[37m'
        magenta = '\033[35m'
        lightblack = '\033[90m'
        lightblue = '\033[94m'
        lightcyan = '\033[96m'
        lightgreen = '\033[92m'
        lightmagenta = '\033[95m'
        lightred = '\033[91m'
        lightwhite = '\033[97m'
        lightyellow = '\033[93m'
    else:
        black, reset, blue, red, yellow, green, cyan, white, magenta, lightblack, lightblue, lightcyan, lightgreen, lightmagenta, lightred, lightwhite, lightyellow = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

color()

def AnimLOAD(text):
    for handlechar in "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏":
        sys.stdout.write(f"\r{white}{handlechar} {reset}{text}")
        sys.stdout.flush()
        time.sleep(0.04)

def PrimeNum(num):
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def Box(text, left, right, raw, area, ct="", crt="", clt="", align="center"):
    area = area - 4
    if not PrimeNum(len(text)): text += " "
    if not PrimeNum(area): area -= 1
    LenOfTxt = len(text)
    len_txt_area = (area // 2) - (LenOfTxt // 2)
    finaltxt = clt + left
    if align == "right": finaltxt += ct + text
    for i in range(len_txt_area+1): finaltxt += raw
    if align == "center": finaltxt += ct + text
    for i in range(int(str(len_txt_area + LenOfTxt - area).replace("-",""))+1): finaltxt += raw
    if align == "left": finaltxt += ct + text
    finaltxt += crt + right
    return finaltxt

def space(num, a= " "):
    return "".join([a for i in range(num)])


def Update():
    def _():
        os.chdir(pip.__path__[0])
        os.chdir("..")

        try: shutil.rmtree(MainSource)
        except FileNotFoundError: pass

        rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 15))
        zipname = source.split("/")[4] +"-"+ source.split("/")[-1].split(".")[0]

        with open(f"{rname}.zip", "wb") as file: file.write(requests.get(source).content)
        with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
        os.remove(f"{rname}.zip")

        shutil.copytree(f"{os.getcwd()}/{rname}/{zipname}", MainSource)
        shutil.rmtree(rname)
    update = threading.Thread(target=_)
    update.start()
    while update.is_alive(): AnimLOAD(f"{cyan}Updateing GTF...")
    update.join()

def Internet():
    try: requests.get("https://google.com/"); return True
    except ConnectionError: return False

def Uninstall(args):
    os.chdir(pip.__path__[0])
    os.chdir("..")
    try:os.chdir(".@GTFRepository90876")
    except FileNotFoundError: print(f"{magenta}[{white}!{magenta}] {white}There aren't any repositories installed.{reset}")
    RM = None
    for repo in os.listdir():
        if (repo == args): RM = True ; break
        else: RM = False
    if not (RM): print(f"{magenta}[{white}!{magenta}] {white}'{args}' aren't installed.{reset}")
    else:
        print(f"{magenta}[{white}!{magenta}] {white}Found existing installed program '{repo}'{reset}")
        action = input(f"{magenta}[{white}?{magenta}] {white}Do you want's uninstall {red}( {white}Y{red}/{white}n {red}) {green}➟  {white}").lower()
        if (action == "y") or (action == "yes") :
            for repo in os.listdir():
                if (repo == args): shutil.rmtree(args)
                else: pass
            print(f"\n{magenta}[{white}+{magenta}] {blue}'{red}{args}{blue}'{white} sucessfully uninstalled.{reset}")
        else: print(f"\n{magenta}[{white}!{magenta}] {white}Invalid option{reset}")

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
        print(f"{magenta}[{white}!{magenta}] {white}Program not found '{reponame}'{reset}")
        if (DID): print(f"{magenta}[{white}+{magenta}] {white}Did you mean,\n")
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: print(f"{yellow}    {repo}{reset}")
    else:
        source = Repository[reponame]['zipurl']
        dependencies = Repository[reponame]['dependencies']
        rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
        zipname = source.split("/")[4] +"-"+ source.split("/")[-1].split(".")[0]
        toolname = zipname.split("-")[0]
        if (reponame in os.listdir()):
            print(f"{magenta}[{white}!{magenta}] {white}'{reponame}' already installed.{reset}")
        else:
            def _():
                with open(f"{rname}.zip", "wb") as file: file.write(requests.get(source).content)
                with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
                os.remove(f"{rname}.zip")
                shutil.copytree(f"{os.getcwd()}/{rname}/{zipname}", toolname)
                shutil.rmtree(rname)
            install = threading.Thread(target=_)
            install.start()
            while install.is_alive(): AnimLOAD(f"{yellow}Installing " + reponame + "...")
            install.join()
            sys.stdout.write(f"\r{magenta}[{white}+{magenta}] {white}{reponame} installed.  \n{reset}")
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive(): AnimLOAD(f"{yellow}Installing Building Dependencies...")
            DEPENDENCIES.join()
            sys.stdout.write(f"\r{magenta}[{white}+{magenta}] {white}Installtion Completed.           \n")
            print(f"{magenta}[{white}-{magenta}] {white}For start {red}>> {white}'{blue}gtf run {reponame}{white}{reset}'")

def Run(reponame, Arguments):
    arguments = ""
    for args in Arguments: arguments += args + " "
    RootPath = pip.__path__[0]
    os.chdir(RootPath)
    os.chdir("..")
    try:os.chdir(".@GTFRepository90876")
    except FileNotFoundError: print(f"{magenta}[{white}!{magenta}] {white}There aren't any repositories installed.{reset}")

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
        print(f"{magenta}[{red}!{magenta}] {white}Program not found '{reponame}'{reset}")
        if (DID): print(f"{magenta}[{white}+{magenta}] {white}Did you mean,\n")
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: print(f"{yellow}    {repo}{reset}")
    else: os.system(f"python{execute()} {run} {arguments}"), exit()

def Help():
    print(f"""
{magenta}[{white}-{magenta}] {yellow}Usage: {blue}gtf {white}<{red}command{white}> {white}[{red}options{white}]

{magenta}[{white}+{magenta}] {cyan}Commands {white}:
    {yellow}install, clone     {white}Install programs.
    {yellow}run, start         {white}Iaunch a program.
    {yellow}uninstall, remove  {white}Remove or uninstall previously installed programs.
    {yellow}gtf.update         {white}Update the tool itself, which may include bug fixes, new features, and improvements.
    {yellow}download           {white}Download the file in zip format to the current working directory.
    {yellow}list               {white}Display a list of all installed programs.
    {yellow}version            {white}Display the current version of the "gtf" tool itself.
    {yellow}help               {white}Display information about the available commands and options.
{magenta}[{white}+{magenta}] {cyan}General Options {white}:
    {yellow}-i, -install       {white}Install programs.
    {yellow}-r, -run           {white}Iaunch a program.
    {yellow}-d, -download      {white}Download the file in zip format to the current working directory.
    {yellow}-l, -list          {white}Display a list of all installed programs.
    {yellow}-v, -version       {white}Display the current version of the "gtf" tool itself.
    {yellow}-h, -help          {white}Display information about the available commands and options.
    {reset}""")

def Download(reponame):
    def zip_folder(folder_path, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_obj:
            # Iterate over all the files in the folder
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    # Create the full filepath by joining the folder path and the filename
                    file_path = os.path.join(foldername, filename)
                    # Add the file to the ZIP file
                    zip_obj.write(file_path)
    Repository = requests.get("https://raw.githubusercontent.com/GreyTechno/Binaries/main/files/.repository").json()
    if not (reponame in Repository):
        DID = False
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: DID = True
        print(f"{magenta}[{white}!{magenta}] {white}Program not found '{reponame}'{reset}")
        if (DID): print(f"{magenta}[{white}+{magenta}] {white}Did you mean,\n")
        for repo in Repository:
            if (repo[0] == "."): continue
            else:
                if (re.search(reponame.lower(), repo.lower()) == None): pass
                else: print(f"{yellow}    {repo}{reset}")
    else:
        source = Repository[reponame]['zipurl']
        rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
        zipname = source.split("/")[4] +"-"+ source.split("/")[-1].split(".")[0]
        toolname = zipname.split("-")[0]
        def _():
            with open(f"{rname}.zip", "wb") as file: file.write(requests.get(source).content)
            with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
            os.remove(f"{rname}.zip")
            shutil.copytree(f"{os.getcwd()}/{rname}/{zipname}", toolname)
            shutil.rmtree(rname)
            zip_folder(toolname, toolname+".zip")
            shutil.rmtree(toolname)
        install = threading.Thread(target=_)
        install.start()
        while install.is_alive(): AnimLOAD(f"{yellow}Installing " + reponame + "...")
        install.join()
        sys.stdout.write(f"\r{magenta}[{white}+{magenta}] {white}{reponame} installed  \n{reset}")
        sys.stdout.write(f"\r{magenta}[{white}-{magenta}] {cyan}Downloaded path for the file {white}:\n")
        sys.stdout.write(f"\r{magenta}[{white}*{magenta}] {white}{currentpath}\{toolname}.zip\n{reset}")

def List():
    RepoLen = []
    VersionLen = []
    RootPath = pip.__path__[0]
    os.chdir(RootPath)
    os.chdir("..")
    try:os.chdir(".@GTFRepository90876")
    except FileNotFoundError: print(f"{magenta}[{white}!{magenta}] {white}There aren't any repositories installed.{reset}"), exit()
    RepoLen, VersionLen = [], []
    [(
        RepoLen.append(len(repo)),
        VersionLen.append(len(json.loads(open(repo+"/.info").read())["version"]))
    ) for repo in os.listdir() if repo[0] != "."]

    if (max(RepoLen) < 10): RepoLen.append(10)
    if (PrimeNum(max(RepoLen))): MaxLenOfRepo = max(RepoLen) + 1
    else: MaxLenOfRepo = max(RepoLen)
    if (PrimeNum(max(VersionLen))): MaxLenOfVersion = max(VersionLen) + 1
    else: MaxLenOfVersion = max(VersionLen)
    print(red+"╔{}╦{}╗".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━")))
    sys.stdout.write(Box("Programs", "║", "║", " ", len(space(MaxLenOfRepo+4, "━")), ct=white, crt=red, clt=red))
    sys.stdout.write(Box("Versions", " ", "║", " ", len(space(MaxLenOfVersion+8, "━")), ct=white, crt=red, clt=red, align="right"))
    print("\n╚{}╩{}╝\n".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━")))
    print("┏{}┳{}┓".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━")))
    ML = True
    for repo in os.listdir():
        if (repo[0] == "."): continue
        else:
            with open(repo+"/.info") as file : version = json.loads(file.read())["version"]
            LenRepo, LenVersion = (MaxLenOfRepo - len(repo)), (MaxLenOfVersion - len(version))
            print(f"{red}┃{white}{repo+space(LenRepo)} {red}┃{cyan} {version}{space(MaxLenOfVersion+3)} {red}┃")
            print(red+"┣{}╋{}┫".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━"))) if (ML) else print("┣{}╋{}┫".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━"))); ML = False
    print("┗{}┻{}┛{}".format(space(MaxLenOfRepo+1, "━"), space(MaxLenOfVersion+8, "━"), reset))

def Version():
    print(f"{magenta}[{white}+{magenta}] {white}The current version is {red}{__VERSION__} {white}and it includes several new features and bug fixes.{reset}")

