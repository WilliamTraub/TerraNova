import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
from land import Land

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Load and preprocess data

def createModel(data): # a list of Lands:
    ds = np.array(data)
    number_of_possible_outcomes = ... # whatever the number of possible outputs (building types) we have
    
    split_ratio = 0.8
    split_index = int(len(ds) * split_ratio)
    (x_train, y_train) = ds[split_index:]
    (x_test, y_test) = ds[:split_index]

    # Define the neural network model
    model = keras.Sequential([
        keras.layers.Input(shape=(4,)),  # Flatten 2D image into 1D array
        keras.layers.Dense(128, activation='relu'),  # Hidden layer with 128 neurons
        keras.layers.Dense(number_of_possible_outcomes, activation='softmax')  # Output layer with 10 neurons (for 10 classes)
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=5)

    # Evaluate the model
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print("\nTest accuracy:", test_acc)

    return model

def makePrediction(model, entry):
    model.predict(entry)
