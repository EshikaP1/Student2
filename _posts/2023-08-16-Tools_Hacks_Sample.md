---
toc: true
comments: true
layout: post
title: Tool demonstation and Introduction
description: Configuration for My Computer  
courses: { compsci: {week: 0} }
type: hacks
---

## Hacks
> Complete the procedure below accurately.  These are absolutely required and must be 100% accurate for your success.

### GitHub Account
- Go on github.io and make an account using your personal email. 
- Connect your GitHub Account to VSCode


### Windows 1st Time Developer
> VSCode install using WSL. Windows users have option to have best of Windows and Linux while developing within VSCode.
- Install [VSCode using WSL]({{site.baseurl}}/techtalk/vscode-wsl).
- Required review, become familiar with [Windows WSL development](https://code.visualstudio.com/docs/remote/wsl-tutorial)

> At this point, the next task is to prepare for Packages, Jupyter Notebooks, and Kernels.  <mark>You must start a new WSL Command / Powershell</mark>.  Now the WSL prompt should be <mark>prefixed with (base)</mark> from Anaconda install.  If not, you need to go back to Anaconda install.
- Open Command / Powershell.  If you are not looking like this you need to back up.
```bash
> PS C:\Users\ShayM> wsl  # Windows prompt
(base) shay@MSI:/mnt/c/Users/ShayM$ cd ~ # WSL prompt
(base) shay@MSI:~$ # WSL home, best place to install files
```

> Key Packages needing update on WSL Ubuntu
- In a WSL Command / Powershell install Python3
```bash
$ sudo apt list # list packages
$ sudo apt update # update package list
$ sudo apt upgrade # upgrade packages
$ sudo apt install python3 python3-pip # install python3 and pip3 for development
$ python --version  # version of python3 should be shown


### Jupyter Install and Kernels (MacOs and WSL)

> Install Jupyter and check python kernel 
```bash
(base) id:~$ conda --version 
(base) id:~$ conda install jupyter # install jupyter
(base) id:~$ jupyter kernelspec list # list installed kernels
Available kernels:
  python3    /home/shay/.local/share/jupyter/kernels/python3
```
