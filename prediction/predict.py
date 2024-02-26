import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class DogCat:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        img_path = self.filename

        # load model
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess the image
        test_img = image.load_img(img_path, target_size=(224, 224))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)
        test_img = test_img / 255.0  # Normalize the image

        # Make a prediction using the loaded model
        result = model.predict(test_img)
        prediction = np.argmax(result, axis=1)
        
        print (prediction[0])
        
        if prediction[0] == 1:
            prediction = 'dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]
