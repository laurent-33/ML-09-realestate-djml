from flask import Flask, render_template, request
import pickle
import pandas as pd
from datetime import date
import csv
import numpy as np

app = Flask(__name__)

features = ['predict_date','city','county','district','type','living_area_m2','lot_size_m2','nb_room','nb_bedroom','pool','cellar','garage','predict_price']

df_prediction = pd.DataFrame(columns=features)
df_prediction.to_csv("../csv/predictions.csv", encoding='utf-8', index=False)

#List of unique element in dataset
list_html = pd.read_csv('../csv/list_html.csv')
list_ville = list(list_html['list_ville'].dropna())
list_dpt = list(list_html['list_departement'].dropna())
list_region = list(list_html['list_region'].dropna())
list_ville.sort()
list_dpt.sort()
list_region.sort()

@app.route('/')
def get_predict():
    return render_template('get_prediction.html', city_list = list_ville)

@app.route('/get_prediction', methods=['POST'])
def predict():
    input_data_form = [[
       request.form['city'].capitalize(),
       request.form['departement'].capitalize(),
       request.form['region'].capitalize(),
       request.form['type'].lower(),
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

    print(input_data)

    full_pipe = pickle.load(open('../models/full_pipe.file', 'rb'))
    output = int(full_pipe.predict(input_data)[0])

# Enregistrement dans un fichier csv de la prediction
    predict_date = date.today()
    input_data_form[0].insert(0,predict_date)
    input_data_form[0].insert(len(input_data_form[0]), output)

    with open("../csv/predictions.csv", 'a') as csvfile:
        writer = csv.writer(csvfile)
        for row in input_data_form:
            writer.writerow(row)
    
    print('résultat : ', output)

    return render_template('predict.html', Prix = output)

@app.route('/new_prediction', methods=['POST'])
def get_predict2():
    return render_template('get_prediction.html', city_list = list_ville)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')