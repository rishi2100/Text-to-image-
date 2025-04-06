import shutil
import random
import os

def copy_random_image(src_folder, dest_path):
    images = os.listdir(src_folder)
    img = random.choice(images)
    shutil.copy(os.path.join(src_folder, img), dest_path)
    return os.path.relpath(dest_path, 'static')
