import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

'''
Prediction class that initializes the weights and models when called 
make the prediction on the image returning a probability value
'''

class Predict:
    def __init__(self):
        #self.model_path = "C:\\Users\\Sena\\Desktop\\stuff\\python\\ai_proj\\pages\\Prostate_model_json.json"
        self.model_path = os.path.join(os.getcwd(), "pages", "Prostate_model_json.json")
        self.weights_paths = os.path.join(os.getcwd(), "pages", "ProstateModelWeight.h5")
        
        self.json_file = open(self.model_path, 'r')
        self.loaded_model_json = self.json_file.read()
        self.json_file.close()
        self.mod = keras.models.model_from_json(self.loaded_model_json)
        self.mod.load_weights(self.weights_paths)
        

    def makePredictions(self, uploadedImage):
        mod = self.mod
        self.img = tf.keras.preprocessing.image.load_img(uploadedImage, target_size=(256,256))
        self.x = tf.keras.preprocessing.image.img_to_array(self.img)
        self.x = self.x.reshape(1,256,256,3).astype('float')
        self.x /= 255
        x= self.x
        self.prediction = mod.predict(x)
        
        return self.prediction

