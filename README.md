# Flask-ML-App-for-Vehicle-Insurance-Claim-Settlement

## Table of contents
* [General Info](#general-info)
* [Life Cycle of Project](#life-cycle-of-project)
* [How to run the Project](#how-to-run-the-project)
* [Technologies](#technologies)
* [Web App](#web-app)
* [Predictions](#predictions)
* [Final Overview](#overview)

## General Info
This is a POC project made using DS concepts and using ML algorithms whose end result is to let the Vehicle Insurance Company which is offering 4 wheeler Insurance to customers that whether the claim that customer is making is genuine or false claim has been made by customer.

## Life Cycle of Project
* Data Cleaning
* Data Manipulation
* Performing EDA to get insights of data 
* HPT using Optuna
* Model Creation and dumping model into a pickle file
* Creating Flask Web using help of HTML and CSS.

## How to run the Project
* Clone this repository
* Create a new environment <code>conda create -n newenv python==3.6</code>
* Open any IDE like Pycharm/VS Code.
* Then install the requirements.txt file <code>pip install -r requirements.txt</code>
* All successful installation of all requirements now run the python app using <code>python app.py</code>

## Technologies
* Python
* Scikit-learn
* Numpy, Pandas, Seaborn, Matplotlib, Optuna
* ML algorithms like LR, GBM, XGBoost, RF, DT etc.
* Flask 
* Render

## Web App
![image](https://user-images.githubusercontent.com/44944830/232671174-bfd0c3a9-35b9-46af-92bb-a325781f36c6.png)

## Predictions
The Insurance Claim is Authentic
![Screenshot (8)](https://user-images.githubusercontent.com/44944830/216769783-52895686-f96d-45a2-ba8c-4aeb1878bc1c.png)


The Insurance Claim is Not Authentic
![Screenshot (9)](https://user-images.githubusercontent.com/44944830/216769814-d5718e4a-fa66-4382-be81-5f6e141a137f.png)

## Final Overview

* This app has been deployed using Render( a web platform similar to Heroku) used for deploying web based app on free tier basis.
You can access the app at : https://vehicle-insurance-claim-flask-app.onrender.com/

* Final Model creation was done using Logistic Regression as for the data we had binary categories and not much complexity in terms of predictors exist in the dataset and we know LR is simple yet effective algorithm in binary classification so we choose this algorithm rather than any boosting or more deep ML algorithm which also proves that computation complexity is less but also giving best results with probabilities of output classes.

* The Web App is allowing only 5 predictors for the end user to change to get the desired output but total number of predictors are more than 20 but those all could not be integrated into a single web page properly so we have taken the best 5 predictors causing the maximum variance in output results.
