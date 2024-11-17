from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    temp = int(request.form['temperature'])
    humidity = int(request.form['humidity'])
    ph = int(request.form['ph'])
    rainfall = int(request.form['rainfall'])
    
    input_data = [N, P, K, temp, humidity, ph, rainfall]
    
    input_data = np.asarray(input_data).reshape(1, -1)
    
    std_data = sc.transform(input_data)
    
    prediction = model.predict(std_data)
    
    crop_dict = {
        1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut', 6: 'papaya', 7: 'orange', 8: 'apple', 9: 'muskmelon', 10: 'watermelon', 11: 'grapes', 12: 'mango', 13: 'banana', 14: 'pomegranate', 15: 'lentil', 16: 'blackgram', 17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas', 20: 'kidneybeans', 21: 'chickpea', 22: 'coffee'
    }
    
    
    match (prediction[0]):
        case 1:
            return render_template('rice.html')
        case 2:
            return render_template('maize.html')
        case 3:
            return render_template('jute.html')
        case 4:
            return render_template('cotton.html')
        case 5:
            return render_template('coconut.html')
        case 6:
            return render_template('papaya.html')
        case 7:
            return render_template('orange.html')
        case 8:
            return render_template('apple.html')
        case 9:
            return render_template('muskmelon.html')
        case 10:
            return render_template('watermelon.html')
        case 11:
            return render_template('grapes.html')
        case 12:
            return render_template('mango.html')
        case 13:
            return render_template('banana.html')
        case 14:
            return render_template('pomegranate.html')
        case 15:
            return render_template('lentil.html')
        case 16:
            return render_template('blackgram.html')
        case 17:
            return render_template('mungbean.html')
        case 18:
            return render_template('mothbeans.html')
        case 19:
            return render_template('pigeonpeas.html')
        case 20:
            return render_template('kidneybeans.html')
        case 21:
            return render_template('chickpea.html')
        case 22:
            return render_template('coffee.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)