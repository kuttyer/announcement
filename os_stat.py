import os
import datetime

path = './work_dir/'

for file in os.listdir(path):
    data = os.stat(os.path.join(path, file))
    last_mod = datetime.datetime.fromtimestamp(data.st_mtime)
    print(file, data.st_size, 'bytes ', last_mod, 'last mod date')

