from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np

#Upload pickle file
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
app = Flask(__name__)


# Here all web input passed by using input() function directly, by just specifieng its type as oint/float etc

def predict():
    Year = input("Enter the Model Year：", type=NUMBER)
    Year = 2021 - Year
    Present_Price = input("Enter the Present Price(in LAKHS)", type=FLOAT)
    Kms_Driven = input("Enter the distance it has travelled(in KMS)：", type=FLOAT)
    Kms_Driven2 = np.log(Kms_Driven)
    Owner = input("Enter the number of owners who have previously owned it(0 or 1 or 2 or 3)", type=NUMBER)
   
    #Here shown dropdown value by using function : select
    Fuel_Type = select('What is the Fuel Type', ['Petrol', 'Diesel','CNG'])
    if (Fuel_Type == 'Petrol'):
        Fuel_Type = 239

    elif (Fuel_Type == 'Diesel'):
        Fuel_Type = 60

    else:
        Fuel_Type = 2
        
     #Here shown dropdown value by using function : select
    Seller_Type = select('Are you a dealer or an individual', ['Dealer', 'Individual'])
    if (Seller_Type == 'Individual'):
        Seller_Type = 106

    else:
        Seller_Type = 195
        
     #Here shown dropdown value by using function : select
    Transmission = select('Transmission Type', ['Manual Car', 'Automatic Car'])
    if (Transmission == 'Manual Car'):
        Transmission = 261
    else:
        Transmission = 40
        
         #Here predicted the output by using pkl file
    prediction = model.predict([[Present_Price, Kms_Driven2, Fuel_Type, Seller_Type, Transmission, Owner, Year]])
    output = round(prediction[0], 2)

     #Here outputing predicted value by using function : put_text
    if output < 0:
        put_text("Sorry You can't sell this Car")

    else:
        put_text('You can sell this Car at price:',output)


# Here we are passing our function "predict" inside webio_view as webio_view(predict), so this will execute entire execution
# Here defining rule and tells which all methods it supports like 'GET','POST','OPTIONS'
# Because of below command in app.py, if we refresh our api link in web it refreshes withot any error.

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


#Heroku Server use this below all code and comment last line
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)
    
#If server wont provides default port then With above port no, predict function is called inside 'if' function

#This line just comment in all case 
#if __name__ == '__main__':
    #predict()

#lOCAL Server use this below 1 code and comment all above
#app.run(host='localhost', port=80)

#visit http://localhost/tool to open the PyWebIO application in local run
