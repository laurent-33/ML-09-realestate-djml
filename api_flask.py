from flask import Flask, render_template, request
import pickle
import sklearn

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

    model = pickle.load(open('./model.file', 'rb'))
    output = model.predict(input_data)

    return render_template('predict.html', Prix = output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')