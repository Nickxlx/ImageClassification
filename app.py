import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from utility.utils import decodeImage
from prediction.predict import DogCat

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "InputImage.jpg"
        self.classifier = DogCat(self.filename)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port = 8080)