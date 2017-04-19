import glob
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from sklearn.preprocessing import OneHotEncoder
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split

x_genre = np.load('x_genre.npy')
y_genre = np.load('y_genre.npy')

enc = OneHotEncoder()
y_genre = enc.fit_transform(y_genre.reshape([-1,1]))

x_train, x_test, y_train, y_test = train_test_split(x_genre, y_genre)

x_train = x_train.reshape(x_train.shape[0],1025, 431,1)
x_test = x_test.reshape(x_test.shape[0], 1025, 431,1)

# create model
model = Sequential()
model.add(Convolution2D(4, 2, 2, border_mode='same', input_shape=(1025,431,1)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(.5))
model.add(Dense(3))
model.add(Activation('softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.save('ginos_model')


# evaluate the model
scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))