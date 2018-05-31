import os

UPLOAD_FOLDER = '/Downloads/'


def current_path_to_dir(dir_name):
    path_to_dir = os.curdir + UPLOAD_FOLDER + dir_name
    print(path_to_dir)
    if not os.path.isdir(path_to_dir):
        os.makedirs(path_to_dir)
    return path_to_dir+'/'