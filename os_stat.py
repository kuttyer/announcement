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
        #print(amslist_to_tuple.splitted_line_tuple)


def walk_through_process():
    for item in amslist_to_tuple.splitted_line_tuple:
        temp_name_list = []
        for file in os.listdir(path):
            file_stats = os.stat(os.path.join(path, file))
            if str(file_stats.st_size) == str(item[1]):
                temp_name_list.append(file)
                if len(temp_name_list) == 1:
                    a = 1
                    #print(file, item[0]+".wav")
                    #os.rename(os.path.join(path, file), os.path.join(path, item[0]+".wav"))
                else:
                    #print(temp_name_list, item)
                    for i in temp_name_list:
                        data = os.stat(os.path.join(path, i))
                        last_mod = str(datetime.datetime.fromtimestamp(data.st_mtime))[0:16]
                        #print(data, last_mod.replace('-','.'), item)
                        if str(last_mod.replace('-','.')) == str(item[2]):
                            print(item[0], i, "kutykurutty")





def file_rename_by_parameters():
    i = 0
    for file in os.listdir(path):
        if file[0:2] == "c-":
            data = os.stat(os.path.join(path, file))
            last_mod = datetime.datetime.fromtimestamp(data.st_mtime)
            i += 1
            file_rename(file, data.st_size, last_mod.strftime("%Y-%m-%d %H:%M"), i)


def file_rename(backup_filename, size, last_mod_date, i):
    temp_name_list = []
    #print(backup_filename, size, len(last_mod_date))
    for item in amslist_to_tuple.splitted_line_tuple:
        if str(item[1]) == str(size):
            temp_name_list.append(item[0])
            if len(temp_name_list) == 1:
                print(temp_name_list)
        os.rename(os.path.join(path, backup_filename), os.path.join(path, item[0]+".wav"))


    #hit = [item for item in amslist_to_tuple.splitted_line_tuple if item[1] == size and str(item[2])[0:16] == str(last_mod_date[0:16])]
    #os.rename(os.path.join(path, backup_filename), os.path.join(path, hit))


amslist_to_tuple()
#file_rename_by_parameters()
walk_through_process()