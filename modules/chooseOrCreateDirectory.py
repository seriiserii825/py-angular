import os
from rich import print
from libs.chooseDir import chooseDir
from libs.listDir import listDir
from libs.select import selectOne


def createOrChooseDirectory(path_to_dir):
    basepath = path_to_dir
    listDir(basepath)
    select_or_create = selectOne(["Select", "Create"])
    if select_or_create == "Create":
        dir_name = input("Enter directory name:")
        if dir_name == '':
            print("[red]Directory name is required")
            exit()
        else:
            os.makedirs(basepath + "/" + dir_name)
            print("[green]Directory created")
            return dir_name
    else:
        selected_dir = chooseDir(basepath)
        return selected_dir
