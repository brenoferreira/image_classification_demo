from __future__ import absolute_import, division, print_function, unicode_literals

import os
import glob
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers
from PIL import Image

# tf.enable_eager_execution()

classifier_url ="https://tfhub.dev/google/imagenet/inception_v3/classification/3"

IMAGE_SHAPE = (224, 224)

module = hub.Module(classifier_url, tags=[])
classifier = tf.keras.Sequential([
    hub.KerasLayer(module, input_shape=IMAGE_SHAPE+(3,))
])

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

PATH = os.getcwd()

def classify(image_path):
    try:
        image = Image.open(image_path).resize(IMAGE_SHAPE)

        np_array = np.array(image)/255.0
        shape = np_array.shape

        result = classifier.predict(np_array[np.newaxis, ...])

        predicted_class = np.argmax(result[0], axis=-1)

        predicted_class_name = imagenet_labels[predicted_class]
        print("Prediction for {}: {}".format(image_path, predicted_class_name))
    except:
        print("Failed to predict for {}".format(image_path))

def get_files():
    return glob.glob(PATH + "/images/*.jpg")

def predict_images():
    files = get_files()

    for file in files:
        classify(file)


if __name__ == "__main__":
    print("Classifying images")
    predict_images()
    print("Done")