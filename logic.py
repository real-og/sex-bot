from loader import IMAGES_NAMES
import random

def get_random_file():
    return random.choice(IMAGES_NAMES)

def remove_jpg(file_name):
    return file_name[:-4]