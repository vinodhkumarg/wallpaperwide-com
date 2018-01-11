import os
import imghdr
import shutil
from pathlib import Path

rootdir = 'root dir1'
desti = 'desti dir'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        img = os.path.join(subdir, file)
        if imghdr.what(img) == 'jpeg':
            # if imghdr.what(os.path.join(desti, file)) == 'jpeg':
            if Path(os.path.join(desti,file)).is_file():
                print("file exists")
            else:
                print(os.path.join(desti, file))
                shutil.copy2(img,desti)