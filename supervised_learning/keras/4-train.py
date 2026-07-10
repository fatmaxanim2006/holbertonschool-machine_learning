#!/usr/bin/env python3
""" Modul 4-train """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                 verbose=True, shuffle=False):
    """ Mini-batch gradient descent istifadə edərək modeli öyrədir """
    history = network.fit(data, labels,
                           batch_size=batch_size,
                           epochs=epochs,
                           verbose=verbose,
                           shuffle=shuffle)

    return history
