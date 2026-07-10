#!/usr/bin/env python3
""" Modul 5-train """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                 validation_data=None, verbose=True, shuffle=False):
    """ Mini-batch gradient descent istifadə edərək modeli öyrədir,
    validation data varsa onu da analiz edir """
    history = network.fit(data, labels,
                           batch_size=batch_size,
                           epochs=epochs,
                           validation_data=validation_data,
                           verbose=verbose,
                           shuffle=shuffle)

    return history
