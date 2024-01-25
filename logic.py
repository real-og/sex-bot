from loader import IMAGES_NAMES, CLASSIC_NAMES, EXOTIC_NAMES, ADVANCED_NAMES
from buttons import classic_btn, exotic_btn, advanced_btn
import random

def get_random_file():
    return random.choice(IMAGES_NAMES)

def remove_jpg(file_name):
    return file_name[:-4]

def get_next_by_categories(category, current_photo_index):
    if category == classic_btn:
        return CLASSIC_NAMES[(current_photo_index + 1) % len(CLASSIC_NAMES)]
    if category == exotic_btn:
        return EXOTIC_NAMES[(current_photo_index + 1) % len(EXOTIC_NAMES)]
    if category == advanced_btn:
        return ADVANCED_NAMES[(current_photo_index + 1) % len(ADVANCED_NAMES)]
