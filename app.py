import numpy as np
import pickle
import joblib
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas
import os
from flask import Flask, request, jsonify, render_template


app = Flask(_name_)
model = pickle.load(open('D:/Users/administrater/Desktop/Meghana/HackTriad_Project/Stock_Prediction_and_Forecasting/lstm.pkl', 'rb'))
scale = pickle.load(open('/Users/administrater/Desktop/Meghana/HackTriad_Project/Stock_Prediction_and_Forecasting/scaler.pkl','rb'))

@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page

@app.route('/predict',methods=["POST","GET"])# route to show the predictions in a web UI
def predict():
    #  reading the inputs given by the user
    input_feature=[float(x) for x in request.form.values() ]  
    features_values=[np.array(input_feature)]
    names = [['target-3', 'target-2', 'target-1']]
    data = pandas.DataFrame(features_values,columns=names)
    data = scale.fit_transform(data)
    data = pandas.DataFrame(data,columns = names)
     # predictions using the loaded model file
    prediction=model.predict(data)
    
    #with open('D:/Users/administrater/Desktop/Meghana/HackTriad_Project/Stock_Prediction_and_Forcasting/prediction.txt', 'w') as file:
     #   file.write(str(prediction))
    print(prediction)
    return render_template("predict.html",x="model", p=str(prediction))
     # showing the prediction results in a UI
if _name=="main_":
    
    # app.run(host='0.0.0.0', port=8000,debug=True)    # running the app
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)