#!/usr/bin/env python3

# delef.py

import os


def delef(path):
    """deletes empty folders recursively
        Args:
            path (str): folder to work with
        Returns:
            integer: the number of deleted folders
    """
    count_del_folders = 0
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
                        count_del_folders += 1
                        print("Deleted \"" + full_path + "\"")
                else:
                    count_del_folders += delef(full_path)
    return count_del_folders


if __name__ == "__main__":
    path = input("Path to work with: ")

    if not os.path.isdir(path):
        print("The path specified does not exist!")
        exit()

    ret = delef(path)
    print("Deleted " + str(ret) + " folder(s)")
