import os
from PIL import Image
import tensorflow.keras
import cv2
import numpy as np
import os.path
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import ImageFile
from sklearn.metrics.pairwise import cosine_similarity as cs
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
ImageFile.LOAD_TRUNCATED_IMAGES = True

#pip install opencv-python
model = MobileNetV2(weights = "imagenet", include_top = True, input_shape = (224, 224, 3))

def file_selector(folder_path):
    filenames = []
    for image in os.listdir(folder_path):
        if image[-3:] == 'jpg' or image[-3:] == 'png' or image[-4:] == 'jpeg' or image[-3:] == 'JPG' or image[-3:] == 'PNG' or image[-4:] == 'JPEG':
            filenames.append(os.path.abspath(folder_path + "/" + image))
    return filenames

def image_vectorization(image_path):
  #print(image_path)
    img=Image.open(image_path)
    img=img.convert("RGB")
    img = img.resize((224, 224))
    #print(img.size)
    img = img_to_array(img)
    img = img.reshape((-1, 224, 224, 3))
    #print(img.shape)
    img=preprocess_input(img)
    vector=model.predict(img)

    return vector

def get_vectors(files):
    liste_vector=[]
    for picture in files:
        liste_vector.append(image_vectorization(picture)[0].tolist())
    return liste_vector

def similarity_detection(vectors, files):
  #wenn iteration in skip, dann alles überspringen
  skip=[]
  dict_pairs={}
  X=np.array(vectors)#similarity bestimmen
  similarity=cs(X)#similarity bestimmen
  #for schleife die über alle listen (Bilder) in similarity geht
  for row in similarity.tolist():
    if similarity.tolist().index(row) in skip:
      pass
    else:
  #wir suchen nach dem index der Bilder die ähnlich zu dem jetzigen Bild (der Iteration) ist
      index_list=[index for index in range(len(row)) if row[index] >= 0.9]
      #print(index_list)
  #skip.append index
      liste_pairs=[]
      for index in index_list:
        skip.append(index)
        liste_pairs.append(files[index])
      #print(skip)
  #dictionary mit ähnlichen Bildern wie in alter Funktion
      dict_pairs[f'{similarity.tolist().index(row)}']=liste_pairs

  return dict_pairs

def liste_similar_pictures(dictionary):
  liste=[]
  for (key, value) in dictionary.items():
    if len(value)>1:
      for picture in value[1:]:
        liste.append(picture)
  return liste

def execute(folder_path):
  files=file_selector(folder_path)
  vector_liste=get_vectors(files)
  similarity_dict=similarity_detection(vector_liste, files)
  liste_sim=liste_similar_pictures(similarity_dict)
  os.mkdir(f"{folder_path}/similar_pictures_folder")
  similar_pictures_folder = f"{folder_path}/similar_pictures_folder"
  for picture in liste_sim:
    try:
      os.replace(f"{picture}", f"{similar_pictures_folder}/{picture.rsplit('/', 1)[-1]}")
    except FileNotFoundError:
      pass

  list_similar_pictures = os.listdir(similar_pictures_folder)
  number_of_similiar_pictures = len(list_similar_pictures)

  statement = f"""{number_of_similiar_pictures} pictures with similarities have been\n
          detected and saved in the 'Similar Pictures' folder"""

  return statement



