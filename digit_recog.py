import tensorflow as tf
from tensorflow.keras import layers, models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Rebuild same model structure
model = models.Sequential([
    layers.Input(shape=(28,28,1)),

    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),

    layers.Dense(64, activation='relu'),

    layers.Dense(10, activation='softmax')
])


model.load_weights("digit_weights.weights.h5")

img = Image.open("digit.png").convert("L")


img = np.array(img)


img = 255 - img


coords = np.argwhere(img > 50)


y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0)


img = img[y0:y1, x0:x1]


img = Image.fromarray(img)


img = img.resize((20,20), Image.Resampling.LANCZOS)


img = np.array(img)

new_img = np.zeros((28,28))


new_img[4:24, 4:24] = img


new_img = new_img / 255.0


new_img = new_img.reshape(1,28,28,1)


prediction = model.predict(new_img)

print("Predicted Digit:", np.argmax(prediction))


plt.imshow(new_img.reshape(28,28), cmap='gray')
plt.title("Processed Image")
plt.show()