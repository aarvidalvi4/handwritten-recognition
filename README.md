# handwritten-recognition
# Handwritten Digit Recognition using CNN

## Project Overview

This project is a beginner-friendly Deep Learning application that recognizes handwritten digits using a Convolutional Neural Network (CNN). The model is trained on the MNIST dataset, which contains thousands of handwritten digit images from 0–9.

The main goal of this project was to understand how image classification works using Deep Learning and how neural networks can learn patterns from image data.

In addition to training the model on the MNIST dataset, the project also allows prediction on custom handwritten digit images created by the user.

---

## Features

* Handwritten digit recognition using CNN
* Training on the MNIST dataset
* Prediction on custom handwritten images
* Image preprocessing and normalization
* Automatic digit cropping and centering
* Visualization of processed input images
* High prediction accuracy on test data

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Pillow (PIL)

---

## Dataset

The project uses the MNIST Handwritten Digit Dataset, which contains:

* 60,000 training images
* 10,000 testing images
* Grayscale handwritten digit images
* Image size: 28×28 pixels

---

## Model Architecture

The model is built using a Convolutional Neural Network (CNN), which is widely used for image recognition tasks.

Architecture used:

* Conv2D Layer
* MaxPooling Layer
* Conv2D Layer
* MaxPooling Layer
* Flatten Layer
* Dense Layer
* Output Layer (Softmax)

The CNN learns important visual features such as edges, curves, and shapes to classify digits correctly.

---

## Image Preprocessing

Custom handwritten images are preprocessed before prediction to improve accuracy.

The preprocessing pipeline includes:

* Converting image to grayscale
* Inverting colors to match MNIST format
* Detecting and cropping the handwritten digit
* Resizing the digit
* Centering it inside a 28×28 image
* Normalizing pixel values

These steps help the model better understand custom handwritten inputs.

---

## Results

The model achieves high accuracy on the MNIST test dataset and is able to predict custom handwritten digits successfully.

Example prediction:

* Input Digit: 5
* Predicted Output: 5

---

## Future Improvements

Some possible future enhancements for this project include:

* Alphabet recognition using EMNIST
* Real-time digit recognition using webcam
* GUI application using Tkinter
* Web deployment using Flask
* Full handwritten word recognition

---

## Learning Outcome

Through this project, I learned:

* Fundamentals of Deep Learning
* Basics of Convolutional Neural Networks (CNNs)
* Image preprocessing techniques
* Model training and evaluation
* Working with TensorFlow and Keras
* Handling real-world prediction challenges

---

## How to Run the Project

### Train the Model

```bash
python handwritten_recognition.py
```

### Predict Custom Digits

```bash
python predict_digit.py
```

---

## Project Structure

```bash
Handwritten-Digit-Recognition/
│
├── handwritten_recognition.py
├── predict_digit.py
├── digit.png
├── digit_weights.weights.h5
└── README.md
```

---

## Conclusion

This project was a great introduction to Deep Learning and Computer Vision. It helped in understanding how CNNs process image data and how preprocessing techniques can significantly improve prediction accuracy.

It also provided hands-on experience with building, training, and testing an AI model from scratch using Python and TensorFlow.
