#!/usr/bin/env python3
""" Modul 3-one_hot """
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """ Etiket vektorunu one-hot matrisinə çevirir """
    one_hot_matrix = K.utils.to_categorical(labels, num_classes=classes)

    return one_hot_matrix
