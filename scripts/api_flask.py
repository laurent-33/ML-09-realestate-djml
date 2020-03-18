from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict/')
def get_predict():
    return render_template('get_prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [[
       request.form['city'],
       request.form['county'],
       request.form['district'],
       request.form['area_m2'],
       request.form['ground_m2'],
       request.form['nb_room'],
       request.form['nb_bedroom'],
       request.form['pool'],
       request.form['cellar'],
       request.form['garage'],
    ]]

    input_data = pd.DataFrame(data=input_data, columns=['city','county','district','area_m2','ground_m2','nb_room','nb_bedroom','pool','cellar','garage'])

    full_pipe = pickle.load(open('./full_pipe.file', 'rb'))
    output = int(full_pipe.predict(input_data)[0])

    print('résultat : ', output)

    return render_template('predict.html', Prix = output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')