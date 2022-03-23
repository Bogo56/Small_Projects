from flask_uploads import UploadSet,IMAGES
from pathlib import Path

## all files saved trough this collection go to the same place we have specified in the .config file
# Also the same extension restrictions are being applied to those files(IMAGES allowed extension list)#
IMAGE_SET = UploadSet("images",IMAGES)

def save_file(file,folder,name=None):
    return IMAGE_SET.save(storage=file,folder=folder,name=name)

def get_filepath(filename):
    full_path = IMAGE_SET.path(filename)
    path = Path(full_path)
    return str(path)

def get_filename(filename):
    full_path= IMAGE_SET.path(filename)
    path=Path(full_path).name
    return path

def get_all(folder):
    full_path = IMAGE_SET.path(folder)
    directory = Path(full_path).glob("*")
    return directory