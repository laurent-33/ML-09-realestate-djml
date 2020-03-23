from flask import Flask, render_template, request
import pickle
import pandas as pd
from datetime import date

app = Flask(__name__)

features = ['predict_date','city','county','district','type','living_area_m2','lot_size_m2','nb_room','nb_bedroom','pool','cellar','garage','predict_price']

df_prediction = pd.DataFrame(columns=features)
df_prediction.to_csv("../csv/predictions.csv")

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict/')
def get_predict():
    return render_template('get_prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data_form = [[
       request.form['city'],
       request.form['departement'],
       request.form['region'],
       request.form['type'],
       request.form['living_area_m2'],
       request.form['lot_size_m2'],
       request.form['nb_room'],
       request.form['nb_bedroom'],
       request.form['pool'],
       request.form['cellar'],
       request.form['garage'],
    ]]

    input_data = pd.DataFrame(data=input_data_form, columns=[
        'city','departement','region','type','living_area_m2','lot_size_m2',
        'nb_room','nb_bedroom','pool','cellar','garage'
        ])

    full_pipe = pickle.load(open('../models/full_pipe.file', 'rb'))
    output = int(full_pipe.predict(input_data)[0])

    df = pd.read_csv("../csv/predictions.csv")
    predict_date = date.today()
    input_data_form[0].insert(0,predict_date)
    input_data_form[0].insert(len(input_data_form[0]), output)
    prediction = pd.DataFrame(input_data_form, columns=features)
    df.append(prediction)
    df.to_csv("../csv/predictions.csv")
    
    print('résultat : ', output)

    return render_template('predict.html', Prix = output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')