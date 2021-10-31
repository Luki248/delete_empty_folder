#!/usr/bin/env python3

# delef.py

import os


def delef(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                full_path = os.path.join(path, entry.name)
                content = os.listdir(full_path)
                if content == []:
                    try:
                        os.rmdir(full_path)
                    except:
                        print("Could not delete \"" + full_path + "\"")
                    else:
                        print("Deleted \"" + full_path + "\"")
                else:
                    delef(full_path)


if __name__ == "__main__":
    path = input("path to work with: ")
    delef(path)
