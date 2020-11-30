#### FLO an NIKOLAUS need to package their code here

#IMPORTS
import os
from PIL import Image
from tensorflow.keras import
import cv2
import numpy as np

#LOAD PICTURES

def picture_list(directory):
    picture_list=[]
    for picture in os.listdir(directory):
        picture_list.append(Image.open(picture))
    return picture_list

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
def duplicate_detector(directory):
    hashes = {}
    # loop over our image paths
    for imagePath in os.listdir(directory):
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
    os.mkdir("duplicate_folder")
    for liste in liste_duplicates:
        for picture in liste:
            os.replace(f"{image_folder}/{picture}", f"{duplicate_folder}/{picture}")











