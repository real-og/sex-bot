from loader import IMAGES_NAMES, CLASSIC_NAMES, EXOTIC_NAMES, ADVANCED_NAMES
from buttons import classic_btn, exotic_btn, advanced_btn
import random

def get_random_file():
    return random.choice(IMAGES_NAMES)

def remove_jpg(file_name):
    return file_name[:-4]

def get_next_by_categories(category, current_photo_index):
    if category == classic_btn:
        new_index = (current_photo_index + 1) % len(CLASSIC_NAMES)
        return CLASSIC_NAMES[new_index], new_index
    if category == exotic_btn:
        new_index = (current_photo_index + 1) % len(EXOTIC_NAMES)
        return EXOTIC_NAMES[new_index], new_index
    if category == advanced_btn:
        new_index = (current_photo_index + 1) % len(ADVANCED_NAMES)
        return ADVANCED_NAMES[new_index], new_index
    

def get_prev_by_categories(category, current_photo_index):
    if category == classic_btn:
        new_index = current_photo_index - 1
        if new_index == -1:
            new_index == len(CLASSIC_NAMES) - 1
        return CLASSIC_NAMES[new_index], new_index
    if category == exotic_btn:
        new_index = current_photo_index - 1
        if new_index == -1:
            new_index == len(EXOTIC_NAMES) - 1
        return EXOTIC_NAMES[new_index], new_index
    if category == advanced_btn:
        new_index = current_photo_index - 1
        if new_index == -1:
            new_index == len(ADVANCED_NAMES) - 1
        return ADVANCED_NAMES[new_index], new_index
    


