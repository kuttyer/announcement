import os
import datetime


data = os.stat('work_dir/!sample.mkv')
last_mod = datetime.datetime.fromtimestamp(data.st_mtime)
print(data.st_size, 'bytes ', last_mod, 'last mod date')

