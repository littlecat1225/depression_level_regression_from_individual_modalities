import numpy as np

from keras.models import Model, load_model
from keras.layers import Dense, CuDNNLSTM, Input, Concatenate, Dropout, Masking
import keras

def load_model(location=None):

	if(location != None):
		model = keras.models.load_model(location)
		print("Loaded the model.")
		return model

	X = Input(shape = (6500, 6,))
	#X_gender = Input(shape = (1,))
	#Y = Masking()(X)

	Y = CuDNNLSTM(18, name = 'lstm_cell')(X)
	Y = Dropout(rate = 0.3)(Y)

	#Y = Concatenate(axis = -1)([Y, X_gender])

	Y = Dense(12, activation = 'relu')(Y)
	Y = Dropout(rate = 0.25)(Y)
	
	Y = Dense(1, activation = None)(Y)

	model = Model(inputs = X, outputs = Y)

	print("Created a new model.")

	return model