### This model uses the model trained (dl_model_training.py)
### to classify images and save them in three different directories

#IMPORTS
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import os
import cv2
import shutil
import tensorflow as tf
from tensorflow.keras import models

#image_folder = input("File path of picture folder please")

# image_folder = "/content/gdrive/MyDrive/Apollo_20/More_Data/TEST_DATA"

def picture_loader(image_folder):
    user_image_paths = [f for f in os.listdir(image_folder) if
                    os.path.isfile(os.path.join(image_folder, f))]
    return user_image_paths


#FUNCTION TO TRANSFORM GIVEN IMAGE INTO A 4D ARRAY
def image_4d_array(image_path):
  if image_path[-3:] == 'jpg' or image_path[-3:] == 'png' or image_path[-4:] == 'jpeg':
    image_ = cv2.imread(image_path)
    image_resized = cv2.resize(image_, (256,256))
    image_expanded = np.expand_dims(image_resized, axis=0)
    return np.array(image_expanded)
  else:
    return None

#FUNCTION TO PREDICT TYPE OF PICTURE WITH IMPORTED MODEL
PIC_TYPE_LIST = ["NORMALE_BILDER", "NOTES", "SCREENSHOT"]

#model_file_path = input("File path of classification model please")

def predict_category(pics_as_arrays, model, categories_list=PIC_TYPE_LIST):
    prediction = model.predict(pics_as_arrays)
    return categories_list[np.argmax(prediction)]

#FUNCTION FOR PREDICTING WHAT CLASS IMAGE IS AN PUTTING IT IN CORRECT FOLDER

#this function creates three new folders in the current directory and makes copies
# of the pictures, placing them in one of the three folders

def file_selector(folder_path):
    filenames = []
    for image in os.listdir(folder_path):
        if image[-3:] == 'jpg' or image[-3:] == 'png' or image[-4:] == 'jpeg':
            filenames.append(os.path.abspath(folder_path + "/" + image))
    return filenames


def image_categoriser(folder_path):

  MODEL_PATH = "Apollo_20/classification_model/saved_model"

  model = tf.keras.models.load_model(MODEL_PATH)

  filenames = file_selector(folder_path)

  os.mkdir(f"{folder_path}/categorised_as_screenshot")
  os.mkdir(f"{folder_path}/categorised_as_notes")

  filepath_screenshots = f"{folder_path}/categorised_as_screenshot"
  filepath_notes = f"{folder_path}/categorised_as_notes"
  filepath_normal = f"{folder_path}/categorised_as_normal_pictures"
  for path in filenames:
    image = image_4d_array(path)
    if image is None:
      pass
    elif predict_category(image, model) == "SCREENSHOT":
     #shutil.copyfile(path, filepath_screenshots + "/" + path)
     os.replace(f"{path}", f"{filepath_screenshots}/{path.rsplit('/', 1)[-1]}")
    elif predict_category(image, model) == "NOTES":
     #shutil.copyfile(path, filepath_notes + "/" + path)
     os.replace(f"{path}", f"{filepath_notes}/{path.rsplit('/', 1)[-1]}")

  list_screenshots = os.listdir(filepath_screenshots)
  number_of_screenshots = len(list_screenshots)

  list_notes = os.listdir(filepath_notes)
  number_of_notes = len(list_notes)

  list_normale_bilder = os.listdir(folder_path)
  number_of_normale_bilder = len(list_normale_bilder)

  statement = f"""All pictures have been categorised into three folders:\n

          categorised as screenshot: {number_of_screenshots} \n
          categorised as notes: {number_of_notes}\n
          normal pictures: {number_of_normale_bilder}"""


  return statement





