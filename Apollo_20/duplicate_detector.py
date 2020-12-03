#### FLO an NIKOLAUS need to package their code here

#IMPORTS
import os
from PIL import Image
import tensorflow.keras
import cv2
import numpy as np

#LOAD PICTURES

def file_selector(folder_path):
    filenames = []
    for image in os.listdir(folder_path):
        if image[-3:] == 'jpg' or image[-3:] == 'png' or image[-4:] == 'jpeg' or image[-3:] == 'JPG' or image[-3:] == 'PNG' or image[-4:] == 'JPEG':
            filenames.append(os.path.abspath(folder_path + "/" + image))
    return filenames

#CREATE HASING FUNCTION TO GIVE SAME PICTURE THE SAME HASH

def dhash(image, hashSize=8):
    # convert the image to grayscale and resize the grayscale image,
    # adding a single column (width) so we can compute the horizontal
    # gradient
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    # compute the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # convert the difference image to a hash and return it
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

#FUNCTION TO GIVE HASH TO EACH PICTURE IN DIRECTORY
def duplicate_detector(folder_path):
    hashes = {}
    # loop over our image paths
    filenames = file_selector(folder_path)
    for imagePath in filenames:
        # load the input image and compute the hash
        image = cv2.imread(imagePath)
        h = dhash(image)
        # grab all image paths with that hash, add the current image
        # path to it, and store the list back in the hashes dictionary
        p = hashes.get(h, [])
        p.append(imagePath)
        hashes[h] = p
    liste_duplicates=[]
    liste_first_picture=[]
    for (key, value) in hashes.items():
        if len(value)>1:
            liste_duplicates.append(value[1:])
        else:
            liste_first_picture.append(value[0])
    os.mkdir(f"{folder_path}/duplicate_folder")
    duplicate_folder = os.path.abspath(f"{folder_path}/duplicate_folder")
    for liste in liste_duplicates:
        for picture in liste:
            os.replace(f"{picture}", f"{duplicate_folder}/{picture.rsplit('/', 1)[-1]}")

    list_duplicates = os.listdir(duplicate_folder)
    number_of_duplicates = len(list_duplicates)

    statement = f"""All duplicates have been filtered out.\n

          Duplicates: {number_of_duplicates}"""

    return statement











