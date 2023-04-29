#!/usr/bin/python
# This line is called a shebang and specifies the path to the Python interpreter that should be used to run the script.
# The shebang is followed by the location of the interpreter executable on the system.
# In this case, it is pointing to the default Python executable that is installed in the /usr/bin directory.

# -*- coding: UTF-8 -*-
# This line specifies the encoding of the source code file.

# Auther : MR_GT
# This line is a comment that indicates the author of the script.

import sys
# The sys module provides access to system-specific parameters and functions.

import requests
# The requests module allows you to send HTTP requests easily.

from .utils import *
# This imports all functions from the utils module in the current package (indicated by the period before "utils").

__VERSION__ = "0.0.5"
# This is a constant variable that stores the version number of the software or package. It is assigned the value "0.0.5" here.

def Main():
    color()
    # This calls the color function, which sets the color scheme for the output.

    try:
        Commands = sys.argv[1]
    except IndexError:
        Commands = False
    # This attempts to get the first argument provided on the command line, which is assumed to be the command to execute.
    # If there is no command provided, the variable is set to False.

    try:
        CommandArguments = sys.argv[2:]
    except IndexError:
        CommandArguments = False
    # This attempts to get any arguments that were provided along with the command.
    # If there are no arguments, the variable is set to False.

    try:
        Arguments = sys.argv[3:]
    except IndexError:
        Arguments = ""
    # This attempts to get any additional arguments that were provided after the command arguments.
    # If there are no additional arguments, the variable is set to an empty string.

    if (Commands):
        # If there is a command provided, proceed to check which command it is.

        # install
        if (Commands == "i") or (Commands == "-i") or (Commands == "--i") or (Commands == "install") or (Commands == "-install") or (Commands == "--install") or (Commands == "--clone") or (Commands == "--clone") or (Commands == "--clone"):
            # This checks if the command is an installation command.
            # There are several aliases for the installation command, which are all checked here.

            if (Internet):
                # This checks if there is an active internet connection.

                if (len(CommandArguments) != 1):
                    print(f"\n{magenta}[{white}!{magenta}] {white}The install command requires 1 argument, but {len(CommandArguments)} were provided")
                    exit()
                    # This checks if there is exactly one argument provided with the installation command.
                    # If there is more than one argument, the script exits with an error message.

                else:
                    Install(CommandArguments[0])
                    # If there is exactly one argument, the Install function is called with that argument.

                    version = requests.get("https://raw.githubusercontent.com/GreyTechno/gtf/main/.info").json()["version"]
                    # This retrieves the version number of the latest release of the package from GitHub.

                    if (__VERSION__ != version):
                        # This checks if the installed version of the package is outdated.

                        print(f"\n{magenta}[{white}!{magenta}] {white}A new release of GTF is available: {blue}{__VERSION__} {red}➟  {yellow}{version}")
                        print(f"{magenta}[{white}!{magenta}] {white}To update, run {red}➟  {yellow}gtf --update{reset}")
                        exit()
            else: print(f"{magenta}[{white}!{magenta}] {white}Check your internet connection...{reset}"), exit()
        # run
        # If the user entered a command to run the program, execute the Run() function with the specified file name and arguments
        elif (Commands == "r") or (Commands == "-r") or (Commands == "--r") or (Commands == "run") or (Commands == "-run") or (Commands == "--run") or (Commands == "--start") or (Commands == "--start") or (Commands == "--start"):
            Run(CommandArguments[0], Arguments)
        # uninstall
        elif (Commands == "remove") or (Commands == "-remove") or (Commands == "--remove") or (Commands == "uninstall") or (Commands == "-uninstall") or (Commands == "--uninstall"):
            if (len(CommandArguments) != 1):
                print(f"\n{magenta}[{white}!{magenta}] {white}The uninstall command requires 1 argument, but {len(CommandArguments)} were provided"), exit()
            else:
                Uninstall(CommandArguments[0])
        # self update
        elif (Commands == "gtf.update") or (Commands == "-gtf.update") or (Commands == "--gtf.update"):
            if (Internet): Update()
            else: print(f"{magenta}[{white}!{magenta}] {white}Check your internet connection...{reset}"), exit()
        # download
        elif (Commands == "d") or (Commands == "-d") or (Commands == "--d") or (Commands == "download") or (Commands == "-download") or (Commands == "--download"):
            if (len(CommandArguments) != 1):
                print(f"\n{magenta}[{white}!{magenta}] {white}The download command requires 1 argument, but {len(CommandArguments)} were provided"), exit()
            else:
                Download(CommandArguments[0])
        # list of installed programs
        elif (Commands == "l") or (Commands == "-l") or (Commands == "--l") or (Commands == "list") or (Commands == "-list") or (Commands == "--list"):
            List()
        # version
        elif (Commands == "v") or (Commands == "-v") or (Commands == "--v") or (Commands == "version") or (Commands == "-version") or (Commands == "--version"):
            Version()
        # help
        elif (Commands == "h") or (Commands == "-h") or (Commands == "--h") or (Commands == "help") or (Commands == "-help") or (Commands == "--help"):
            Help()
        else: Help()
    else:
        Help()


if (__name__ == "__main__"):
    Main()
