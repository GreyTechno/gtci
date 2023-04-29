<h3 align="center">About</h3>
<p align="center">An installer for GTF (command line installer) is a tool that enables developers, beginners, and system administrators to install software and libraries efficiently and quickly from the command line interface (CLI). These installers usually use package managers to manage software dependencies and ensure a seamless and efficient installation process.</p>
<p align="center">GTF installers are highly valuable for developers, beginners, and system administrators since they provide an automated and quick way to install software and libraries. These installers simplify the installation process and ensure that software dependencies are correctly managed, making them an essential tool in any deployment or development pipeline.</p>
<p align="center">In particular, GTF installers are highly beneficial for automating the installation process in a deployment pipeline. In such a scenario, it is critical to ensure that software dependencies are installed correctly to avoid any delays in the pipeline.</p>

### Requirements
<li>Python3</li>

### Installition
###### On macOS use 'pip3'
```sh
pip install gtf
```

### Usage
```py
[-] Usage: gtf <command> [options]

[+] Commands :
    install, clone     Install programs.
    run, start         Iaunch a program.
    uninstall, remove  Remove or uninstall previously installed programs.
    gtf.update         Update the tool itself, which may include bug fixes, new features, and improvements.
    download           Download the file in zip format to the current working directory.
    list               Display a list of all installed programs.
    version            Display the current version of the "gtf" tool itself.
    help               Display information about the available commands and options.
[+] General Options :
    -i, -install       Install programs.
    -r, -run           Iaunch a program.
    -d, -download      Download the file in zip format to the current working directory.
    -l, -list          Display a list of all installed programs.
    -v, -version       Display the current version of the "gtf" tool itself.
    -h, -help          Display information about the available commands and options.
```
