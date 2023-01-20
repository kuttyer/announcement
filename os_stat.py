import os
import datetime

path = './work_dir3/'
splitted_line_list = []


def amslist_to_tuple():
    with open('ams_list.txt', 'r') as f:
        x = f.readlines()
        for line in x:
            splitted_line_list.append(line.strip().split(','))
        amslist_to_tuple.splitted_line_tuple = tuple(splitted_line_list)


def file_rename_by_parameters():
    for file in os.listdir(path):
        data = os.stat(os.path.join(path, file))
        last_mod = datetime.datetime.fromtimestamp(data.st_mtime)
        file_rename(file, str(data.st_size), str(last_mod.strftime("%Y-%m-%d %H:%M")))


def file_rename(backup_filename, size, last_mod_date):
    #print(backup_filename, size, last_mod_date)
    for item in amslist_to_tuple.splitted_line_tuple:
        print(str(item[2])[0:16], str(last_mod_date[0:16]))



    #hit = [item for item in amslist_to_tuple.splitted_line_tuple if item[1] == size and str(item[2])[0:16] == str(last_mod_date[0:16])]
    #os.rename(os.path.join(path, backup_filename), os.path.join(path, hit))


amslist_to_tuple()
file_rename_by_parameters()
