import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os

#mnist = tf.keras.datasets.mnist
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

#x_train = tf.keras.utils.normalize(x_train, axis=1)
#x_test = tf.keras.utils.normalize(x_test, axis=1)

#model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Dense(128, activation= 'relu'))
#model.add(tf.keras.layers.Dense(128, activation= 'relu'))
#model.add(tf.keras.layers.Dense(10, activation= 'softmax'))

#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics= ['accuracy'])

#model.fit(x_train, y_train, epochs=3)

#model.save('handwritten.keras')

model = tf.keras.models.load_model('handwritten.keras')


"""folder = "mnist_png/testing/7"

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    img = img / 255.0

    prediction = model.predict(img.reshape(1, 28, 28), verbose=0)

    print(f"{filename}: {np.argmax(prediction)}")"""

# Loop through each digit folder (0-9)
for digit in range(10):

    folder = f"mnist_png/testing/{digit}"

    # Loop through every image in the folder
    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        # Read the image in grayscale
        img = cv.imread(path, cv.IMREAD_GRAYSCALE)

        # Skip if image couldn't be loaded
        if img is None:
            continue

        # Normalize the image
        img = img / 255.0

        # Reshape to (1, 28, 28)
        img = img.reshape(1, 28, 28)

        # Predict
        prediction = model.predict(img, verbose=0)

        predicted_digit = np.argmax(prediction)

        print(f"Actual: {digit} | Predicted: {predicted_digit}")

        
        plt.imshow(img[0], cmap="gray")
        plt.title(f"Actual: {digit}  Predicted: {predicted_digit}")
        plt.axis("off")
        plt.show()

       
        break
