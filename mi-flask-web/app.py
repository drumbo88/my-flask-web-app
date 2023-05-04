from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/predecir", methods=['POST'])
def predecir():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])

    # prediction = model.predict([[rooms, distance]])[0]
    prediction = 125000
    output = prediction #round(prediction, 2)
    return render_template('index.html', prediction_str=f'Rooms={rooms} + Distance={distance}km = ${output}')

if __name__ == "__main__":
    app.run()