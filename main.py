from keras.models import Sequential

import tensorflow as tf

import tensorflow_datasets as tfds

tf.enable_eager_execution()

from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, RMSprop, adam
from keras.utils import np_utils
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn import metricsfrom sklearn.utils import shuffle
from sklearn.model_selection import train_test_splitimport matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
import randomfrom numpy import *
from PIL import Image
import theano