#! /usr/bin/env python3

import zipfile
import colorama
from optparse import OptionParser
from threading import Thread
from colorama import Fore, Style

colorama.init(strip=False)                                                                         # Adds color to Windows cmd

def zipcrack(zFile,password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        print(Fore.RED + "[-] " + password.decode() + " = Bad Password" + Style.RESET_ALL)

def main():
    parser = OptionParser(usage="Usage: CrackZ.py -f <Filename> -d <Dictionary>")                 # Add user input options
    parser.add_option('-f', dest='ZipFileName', type='string', help='Specify Zip File')             # Add user input options
    parser.add_option('-d', dest='DictionaryName', type='string', help='Specify Dictionary')        # Add user input options
    (options,args) = parser.parse_args()                                                            # Add user input options
    if (options.ZipFileName == None) | (options.DictionaryName == None):                            # Add user input options
        print("\nUsage: ZipCrack.py -f <filename> -d <dictionary> or -h for help\n")                # Add user input options
        exit(0)
    else:
        zipname = options.ZipFileName
        dictname = options.DictionaryName
    zFile = zipfile.ZipFile(zipname)
    passwordfile = open(dictname,"rb+")
    for line in passwordfile:
        password = line.strip()
        threads = Thread(target=zipcrack, args=(zFile,password))                                    # Added threading
        attempt = zipcrack(zFile,password)
        if attempt:
            print(Fore.YELLOW + Style.BRIGHT +"[+] Password Cracked! = " + password.decode() + "\n" + Style.RESET_ALL)
            exit(0)
    threads.start()                                                                                 
main()
