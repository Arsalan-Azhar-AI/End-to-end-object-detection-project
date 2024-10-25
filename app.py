'''
from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys
from signLanguage.pipeline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()
'''


import sys, os
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.exception import SignException
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
import subprocess


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 




@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        

        weights_path = os.path.join("yolov5", "runs", "train", "yolov5s_results", "weights", "best.pt")
        input_image_path = os.path.join("data", "inputImage.jpg")
        output_image_path = os.path.join("yolov5", "runs", "detect", "exp", "inputImage.jpg")

        result = subprocess.run(["python", "yolov5/detect.py", "--weights", weights_path, "--img", "640", "--conf", "0.5", "--source", input_image_path], capture_output=True, text=True)

        # Print or log result.stdout and result.stderr for debugging
        print(result.stdout)
        print(result.stderr)



        opencodedbase64 = encodeImageIntoBase64(output_image_path)
        result = {"image": opencodedbase64.decode('utf-8')}
        os.remove("yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)




@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 640 --conf 0.5 --source 0")
        os.remove("yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)