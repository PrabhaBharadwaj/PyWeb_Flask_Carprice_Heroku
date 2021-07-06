# PyWebIO_Flask_Carprice_Heroku
Heroku deploy PyWeb script

## Car price prediction Problem:

This dataset contains information about used cars.
This data can be used for a lot of purposes such as price prediction to exemplify the use of linear regression in Machine Learning.

## Source Data
Data downloded from Kaggle

## Approach:

By using Linear RandomForset Regressor , we are predicting the Car price based on user input data

Here we used Flask web applicationw with pyWebIO  and deployed in Heroku cloud platform (Platform As A service-PAAS) 

This helps to deploy without creating html code for web display while using Flask, so here no need templates, Static/css folder etc

## PywebIO LIBRARY:

	This helps to deploy without creating html code for web display while using Flask, so here no need templates, Static/css folder etc
	PyWebIO provides a series of imperative functions to obtain user input and output on the browser, turning the browser into a "rich text terminal", and can be used to build simple web applications or browser-based GUI applications without the need to have knowledge of HTML and JS. 
	PyWebIO can also be easily integrated into existing Web services like Flask. PyWebIO is very suitable for quickly building applications that do not require complex UI.
	PyWebIO- Creating WebAPP Using Python Without Using HTML And JS


## 1. Deployment main files:
    app.py
    model.pkl
    requirements.txt (It should have PywebIO  library)
    Procfile  (Used to deploy in Heroku)
		



## 2. Install PywebIO in anaconda 
		
	--> Create local env and install all necessary package	
		pip install pywebio
		


## 3. Create app.py file:

	--> Create app.py script and run in cmd anaconda
			
	--> Because of below command in app.py, if we refresh our api link in web it refreshes withot any error.

		app.add_url_rule('/tool', 'webio_view', webio_view(predict),
           	 methods=['GET', 'POST', 'OPTIONS'])

## 4. Create Procfile :
	
	Below is the command, here PORT will take default port in case server assigns default one else user provided one used

		web: python app.py --port=$PORT

## 5. Run in cmd
	--> Inside app.py comment below part 
		#if __name__ == '__main__':
 			#   parser = argparse.ArgumentParser()
 			#   parser.add_argument("-p", "--port", type=int, default=8080)
 			 #  args = parser.parse_args()

 			#   start_server(predict, port=args.port)
	
	--> Inside app.py uncomment below part 
		app.run(host='localhost', port=80)

	--> Install all library in local which are req 
			pip install -r requirements.txt
	
	--> In cmd deploy like below
		python app.py

		visit http://localhost/tool to open the PyWebIO application in local run
		It took all values but stuck near prediction time " An internal error occured in the application

6. Deploy in  Heroku
	--> Inside app.py uncomment below part 
		#if __name__ == '__main__':
 			#   parser = argparse.ArgumentParser()
 			#   parser.add_argument("-p", "--port", type=int, default=8080)
 			 #  args = parser.parse_args()

 			#   start_server(predict, port=args.port)
	
	--> Inside app.py comment below part 
		app.run(host='localhost', port=80)

	--> Heroku also same process as normal, we get one link and can see there our wep api

		-->  app limit 5 in heroku was reached, so deleted nlp-spamham-detection-api and created new "ml-carprice-pywebio-flask-api" and tried . 
		--> But it got failed with some error in heroku so stopped there
	

