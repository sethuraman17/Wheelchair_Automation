import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('Categorical.h5')  # Load your binary classification model

# Specify the full file path to the image you want to predict
image = cv2.imread("Dataset/left_resize/1696852636.png")

img = Image.fromarray(image)

img = np.array(img)

input_img = np.expand_dims(img, axis=0)

result = np.argmax(model.predict(input_img))

if result == 0:
    print("RESULT -----> Center")
elif result == 1:
    print("RESULT -----> Left")
elif result == 2:
    print("Result -----> Right")

print("Class: [", result, "]")
