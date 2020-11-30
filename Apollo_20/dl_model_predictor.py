### This model uses the model trained (dl_model_training.py)
### to classify images and save them in three different directories

#IMPORTS
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
import shutil

image_folder = input("File path of picture folder please")

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

model_file_path = input("File path of classification model please")
#model_file_path = "content/gdrive/MyDrive/Apollo_20/saved_model.h5"
model = load_model(model_file_path)

def predict_category(pics_as_arrays, model=model, categories_list=PIC_TYPE_LIST):
    prediction = model.predict(pics_as_arrays)
    return categories_list[np.argmax(prediction)]

#FUNCTION FOR PREDICTING WHAT CLASS IMAGE IS AN PUTTING IT IN CORRECT FOLDER

#this function creates three new folders in the current directory and makes copies
# of the pictures, placing them in one of the three folders

def categoriser(user_image_paths):
  current_directory = os.getcwd()
  os.mkdir("categorised_as_screenshot")
  os.mkdir("categorised_as_notes")
  os.mkdir("categorised_as_normal_bilder")
  filepath_screenshots = (str(current_directory).strip("[]").strip("''") + "/" + "categorised_as_screenshot").strip("''")
  filepath_notes = (str(current_directory).strip("[]").strip("''") + "/" + "categorised_as_notes").strip("''")
  filepath_normal = (str(current_directory).strip("[]").strip("''") + "/" + "categorised_as_normal_bilder").strip("''")
  for path in user_image_paths:
    image = image_4d_array(path)
    if image is None:
      pass
    elif predict_category(image) == "SCREENSHOT":
     shutil.copyfile(path, filepath_screenshots + "/" + path)
    elif predict_category(image) == "NOTES":
     shutil.copyfile(path, filepath_notes + "/" + path)
    elif predict_category(image) == "NORMALE_BILDER":
     shutil.copyfile(path, filepath_normal + "/" + path)

  list_screenshots = os.listdir("categorised_as_screenshot")
  number_of_screenshots = len(list_screenshots)

  list_notes = os.listdir("categorised_as_notes")
  number_of_notes = len(list_notes)

  list_normale_bilder = os.listdir("categorised_as_normal_bilder")
  number_of_normale_bilder = len(list_normale_bilder)

  statement = f"All pictures have been categorised into three folders:\
          categorised_as_screenshot: {number_of_screenshots} \
          categorised_as_notes: {number_of_notes}\
          categorised_as_normale_bilder: {number_of_normale_bilder}"

  return statement

  #categoriser(user_image_paths)




