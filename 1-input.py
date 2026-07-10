#!/usr/bin/env python3
""" Modul 1-input """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ Neyron şəbəkəsini Keras funksional API ilə qurur """
    regularizer = K.regularizers.l2(lambtha)
    inputs = K.Input(shape=(nx,))

    x = K.layers.Dense(layers[0], activation=activations[0],
                        kernel_regularizer=regularizer)(inputs)

    for i in range(1, len(layers)):
        x = K.layers.Dropout(1 - keep_prob)(x)
        x = K.layers.Dense(layers[i], activation=activations[i],
                            kernel_regularizer=regularizer)(x)

    model = K.Model(inputs=inputs, outputs=x)

    return model
