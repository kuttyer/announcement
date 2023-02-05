import pandas as pd
import os
import datetime

path = './work_dir3/'
def dir2csv():
    with open('backup_dir.csv', 'a') as bd:
        bd.write('name, size, lastmod\n')
        for file in os.listdir(path):
            file_stats = os.stat(os.path.join(path, file))
            last_mod = str(datetime.datetime.fromtimestamp(file_stats.st_mtime))[0:16]
            bd.write(f"{file}, {file_stats.st_size}, {last_mod.replace('-', '.')}\n")


def csv2df():
    csv2df.df_orig = pd.read_csv('ams_list.csv', skipinitialspace=True, usecols=['name', 'size', 'lastmod'])
    csv2df.df_backup = pd.read_csv('backup_dir.csv', skipinitialspace=True, usecols=['name', 'size', 'lastmod'])


def rename_process():
    for index, row in csv2df.df_orig.iterrows():
        file_size = (row['size'])
        file_lastmod = (row['lastmod'])
        orig_name = (row['name'])
        if csv2df.df_orig['size'].value_counts()[file_size] == 1:
            backup_name = (csv2df.df_backup[csv2df.df_backup['size'] == file_size]['name'].tolist())[0]
            #print(backup_name, ' ' , row['name'] + '.wav')
            os.rename(os.path.join(path, backup_name), os.path.join(path, orig_name + ".wav"))
        else:
            xxx = csv2df.df_backup.loc[(csv2df.df_backup['size'] == file_size) & (csv2df.df_backup['lastmod'] == file_lastmod), 'name'].tolist()
            if len(xxx) == 1:
                #print(xxx[0], ' ' , row['name'] + '.wav')
                os.rename(os.path.join(path, xxx[0]), os.path.join(path, orig_name + ".wav"))
            else:
                with open('leftover.csv', 'a') as lo:
                    lo.write(orig_name + '\n')



#dir2csv()
csv2df()
rename_process()