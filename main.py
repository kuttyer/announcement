import os
path = './work_dir/'


def orig_name_finders():
    with open(f'{path}/name_source.txt', 'r') as f:
        lines = (f.read().splitlines())

    for line in lines:
        archived_name, orig_name = (line.split(','))

        for announcement in os.listdir(path):
            if announcement == archived_name:
                os.rename(os.path.join(path, announcement), os.path.join(path, orig_name))


orig_name_finders()
