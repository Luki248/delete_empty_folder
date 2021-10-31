#!/usr/bin/env python3

# delete_empty_folder.py

import os
import argparse

import delef

VERSION = "0.9"

arg_parser = argparse.ArgumentParser(prog="delete_empty_folders",
                                     description="Delete empty Folders")
arg_parser.version = VERSION

arg_parser.add_argument("Path",
                        metavar="path",
                        type=str,
                        help="the path to work with")

arg_parser.add_argument("-v",
                        "--version",
                        action="version",
                        help="show the version of the program")

args = arg_parser.parse_args()

folderpath = args.Path

if not os.path.isdir(folderpath):
    print("The path specified does not exist!")
    exit()

delef.delef(folderpath)
