# TODO: w tym pliku wszystkie rzeczy związane z siecią neuronową
# TODO: wyuczony model sieci musi znajdować się w pliku trained_NN.json zgodnie z dokumentacją
# TODO: z tego pliku też zaciągamy model przy predykcji
# TODO: dodanie logiki uczenia sieci
# TODO: dodanie logiki predykcji sieci

import os
import tensorflow as tf
import numpy as np

from logic.dbservice import DataBase

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disable tensorflow warnings


class NN():
    def __init__(self):
        self.db = DataBase()
        self.model = tf.keras.models.load_model("trained_NN.json")

    def train_network(self):
        model = self.create_model()
        samples = np.array(list(map(lambda sample: list(sample.values()), self.db.get_samples())))
        X, Y = np.split(samples, [-1], axis=1)
        model.fit(X, Y, epochs=25)
        model.save("trained_NN.json")

    def predict(self, x):
        return self.model.predict(x)

    def create_model(self, input_neurons=10, hidden_layer_neurons=200, hidden_activation='sigmoid', loss='mean_squared_error'):
        inputs = tf.keras.Input(shape=(input_neurons,))
        x = tf.keras.layers.Dense(hidden_layer_neurons, activation=hidden_activation)(inputs)
        outputs = tf.keras.layers.Dense(1)(x)
        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        model.compile(loss=loss, optimizer='adam', metrics=['mse'])
        return model
