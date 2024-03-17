from flask import Flask, request, jsonify
from utils import LabelPreprocessor
import keras
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    data = {}
    try:
        data = request.get_json()
    except:
        data = {'Temperature': [0, 22, 10], 'Rainfall': [70, 35, 82], 'Humidity': [82, 50, 16], 'Wind': [80, 45, 32], 'Crop': ['pepper', 'tomato', 'pepper']}
    assert data['Temperature'], "Temperature is required"
    assert data['Rainfall'], "Rainfall is required"
    assert data['Humidity'], "Humidity is required"
    assert data['Wind'], "Wind is required"
    assert data['Crop'], "Crop is required"

    # data = {k: np.array(v) for k,v in data.items()}
    for k,v in data.items():
        if len(v) > 0 and isinstance(v[0], str):
            data[k] = np.array(v, dtype="object")
        else:
            data[k] = np.array(v, dtype="float32")

    lp = LabelPreprocessor()
    model = keras.models.load_model("agrohub.keras")
    predict_raw_data = [np.argmax(i) for i in model.predict(data)]
    predict_data = lp.decode(predict_raw_data)
    response = zip(data['Crop'], predict_data)
    response = list(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)