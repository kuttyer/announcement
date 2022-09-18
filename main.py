import os
path = './work_dir/'


def orig_name_finders():
    renamed_file = 0
    with open(f'{path}/name_source.txt', 'r') as f:
        lines = (f.read().splitlines())

    for line in lines:
        archived_name, orig_name = (line.split(','))

        for announcement in os.listdir(path):
            if announcement == archived_name:
                print(f'Finded a file on {announcement} name and renamed to {orig_name}.')
                os.rename(os.path.join(path, announcement), os.path.join(path, orig_name))
                renamed_file += 1

    print(f'{renamed_file} files has been renamed!')


orig_name_finders()
