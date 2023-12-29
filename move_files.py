from progressbar import ProgressBar, Percentage, Bar, ETA
import platform
import time
import shutil
import os


def add_backslash(taken_from,taken_to):

    postfix = "\\\\"

    source_dir = ""
    target_dir = ""

    taken_from = taken_from.split('\\')
    taken_to = taken_to.split('\\')


    for i in range(len(taken_from)):
        source_dir += taken_from[i] + postfix

    for i in range(len(taken_to)):
        target_dir += taken_to[i] + postfix


    source_dir = source_dir[:-2]
    target_dir = target_dir[:-2]

    return source_dir,target_dir

def add_frontslash(taken_from,taken_to):
    postfix = "//"

    source_dir = ""
    target_dir = ""

    taken_from = taken_from.split('//')
    taken_to = taken_to.split('//')


    for i in range(len(taken_from)):
        source_dir += taken_from[i] + postfix

    for i in range(len(taken_to)):
        target_dir += taken_to[i] + postfix


    source_dir = source_dir[:-2]
    target_dir = target_dir[:-2]

    return source_dir,target_dir

def select_files_to_move(source_dir):
    file_list = os.listdir(source_dir)

    file_names = []

    for file_name in file_list:
        to_add = input(f"Want to move {file_name} file?:\n")
        if to_add == "Yes" or to_add == "Y" or to_add =="y":
            file_names.append(file_name)
        elif to_add == "No" or to_add == "N" or to_add == "n":
            print(f"{file_name} file skipped....\n")
    return file_names

def bulk_files_move(source_dir):
    file_list = os.listdir(source_dir)

    file_names = []

    for file_name in file_list:
            file_names.append(file_name)

    return file_names

def move_files(source_dir,target_dir,taken_from,taken_to, file_names):

    if len(file_names) !=0:
        progress, progress_maxval = 0, len(file_names)
        pbar = ProgressBar(widgets=['Progress ', Percentage(), Bar(), ' ', ETA(), ],maxval=progress_maxval).start()

        for file in file_names:
            progress +=1
            shutil.move(os.path.join(source_dir, file), target_dir)
            pbar.update(progress)

        pbar.finish()
    else:
        print(f"No files to move from {taken_from} to {taken_to}")

if __name__ == "__main__":

    taken_from = input("Source Directory ?:\n")
    taken_to =  input("Target Directory ?:\n")
    
    source_dir,target_dir = '',''

    if platform.system() == "Windows":
        source_dir, target_dir = add_backslash(taken_from,taken_to)
    else:
        source_dir,target_dir = add_frontslash(taken_from,taken_to)

    type_of_move = input("Do you want to do\n1.Bulk Move (Press 'B') or\n2.Selective Move (Press 'S')\n")

    file_names = []

    if type_of_move == 'B':
        file_names =  bulk_files_move(source_dir)
    elif type_of_move == 'S':
        file_names = select_files_to_move(source_dir)

    print(f"These are the files which will be moved from \n1. {source_dir} to \n2. {target_dir}\n")
    for i in range(len(file_names)):
        print(f"{i+1}. {file_names[i]}")
    
    should_move = input("Start Moving ?\n")
    if should_move == "Yes" or should_move == "Y" or should_move == "y" or should_move == "YES":
        start_time = time.time()
        move_files(source_dir,target_dir,taken_from,taken_to,file_names)
        end_time = time.time()

    else:
        print("Thank you!!")



