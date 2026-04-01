from keras.datasets import mnist
import numpy as np
import keras
from keras import layers

#? Loading training/test materials
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#? the models mods
model = keras.Sequential(
    [
        layers.Dense(512, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ]
)

#? compile types
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

#? adjust the shape
#! need to reshape the test and train material
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255


#? runing the programme
model.fit(train_images, train_labels, epochs=5, batch_size=126)
