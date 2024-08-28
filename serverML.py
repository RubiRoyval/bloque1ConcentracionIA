#Python libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
from load import joblib
#Files management
import os
from werkzeug.utils import secure_filename

#Load model
dt=joblib.load('dtl-2_ml.joblib')
#Create Flask app 
server=Flask(__name__)

#Define route to send JSON data 
@server.route('/predictjson',method=['POST'])
def predictjson():
    #Procesar los datos de entrada
    data = request.json
    print(data)
    inputData= np.array([
        data['pH'],
        data['sulphates'],
        data['alcohol']
    ])
    #Predecir utilizando la entrada y el modelo 
    result= dt.predictjson(inputData.reshape(1,-1))
    #Enviar respuesta
    return jsonify({'Prediction':str(result[0])})

if __name__ == '__main__':
    server.run(debug=False,host='0.0.0.0',port=8080)
    
