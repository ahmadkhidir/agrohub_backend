from utils import LabelPreprocessor
import keras
import numpy as np
from numpy import array

lp = LabelPreprocessor()

model = keras.models.load_model("agrohub.keras")

data = {'Temperature': array([ 0, 22, 10]), 'Rainfall': array([70, 35, 82]), 'Humidity': array([82, 50, 16]), 'Wind': array([80, 45, 32]), 'Crop': array(['pepper', 'tomato', 'pepper'], dtype=object)}

pred = [np.argmax(i) for i in model.predict(data)]
pred = lp.decode(pred)

print("PREDICTION:", pred)
