from flask import Flask, request, render_template
import json
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('insurance_claim_model.pickle', 'rb'))
_data_columns = json.load(open('columns.json', 'r'))['data_columns']

@app.route('/')
def hello():
    return render_template('app.html')    

@app.route('/predict',methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    x = np.zeros(len(_data_columns))

    x[3] = float(final_features[0][0]/1000)
    x[5] = final_features[0][1]
    x[10] = final_features[0][2]
    x[9] = final_features[0][3]
    x[0] = final_features[0][4]

    output = str(model.predict([x])[0])

    if output == str(0.0):
        return render_template('app.html',pred='This Vehicle Insurance Claim is not Legitimate \u274C')
    else:
        return render_template('app.html',pred='This Vehicle Insurance Claim is Authentic \u2713')

if __name__ == '__main__':
    app.run()