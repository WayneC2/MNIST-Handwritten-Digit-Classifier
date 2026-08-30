 # ✍️ MNIST Handwritten Digit Classifier
 
A machine-learning project that trains a neural network to recognize handwritten digits from 0 through 9. The project uses the MNIST dataset for training and testing, TensorFlow/Keras for the model, OpenCV for image processing, and Matplotlib to display prediction results.

✨ Features

✅ Loads and normalizes the MNIST handwritten-digit dataset

✅ Trains a neural network to recognize digits from 0–9

✅ Saves the trained model as a .keras file

✅ Reloads the saved model without retraining it

✅ Reads external PNG images with OpenCV

✅ Tests images organized into digit folders

✅ Compares the actual digit with the model’s prediction

✅ Displays each tested image and its prediction

🧠 Model Architecture

Flatten layer – converts each 28 × 28 image into a one-dimensional array

Dense layer – 128 neurons with ReLU activation

Dense layer – 128 neurons with ReLU activation

Output layer – 10 neurons with Softmax activation

The model uses the Adam optimizer and sparse categorical cross-entropy loss.

🛠️ Built With

Python – project logic

TensorFlow / Keras – neural-network training and predictions

OpenCV – reading and processing image files

NumPy – array operations and prediction results

Matplotlib – displaying test images

MNIST Dataset – handwritten-digit training and testing data

📂 Project Structure

mnist-digit-classifier/
│
├── main.py
├── handwritten.keras
├── mnist_png/
│   └── testing/
│       ├── 0/
│       ├── 1/
│       ├── 2/
│       ├── 3/
│       ├── 4/
│       ├── 5/
│       ├── 6/
│       ├── 7/
│       ├── 8/
│       └── 9/
├── requirements.txt
└── README.md


▶️ Run the Project

python main.py

The program loops through the testing folders, predicts one image from each digit category, prints the actual and predicted values, and displays the image.

📊 Example Output

Actual: 0 | Predicted: 0
Actual: 1 | Predicted: 1
Actual: 2 | Predicted: 2
