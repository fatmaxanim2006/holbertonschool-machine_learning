#!/usr/bin/env python3
"""Trains a model using mini-batch gradient descent, with learning
rate decay"""
import tensorflow.keras as K


def train_model(
        network, data, labels, batch_size, epochs,
        validation_data=None, early_stopping=False, patience=0,
        learning_rate_decay=False, alpha=0.1, decay_rate=1,
        verbose=True, shuffle=False):
    """
    Trains a model using mini-batch gradient descent, and analyzes
    validaiton data, if provided, with the options of early stopping
    and learning rate decay

    network: the model to train
    data: numpy.ndarray of shape (m, nx) containing the input data
    labels: one-hot numpy.ndarray of shape (m, classes) containing
        the labels of data
    batch_size: size of the batch used for mini-batch gradient descent
    epochs: number of passes through data for mini-batch gradient descent
    validation_data: data to validate the model with, if not None
    early_stopping: boolean that indicates whether early stopping
        should be used
        early stopping should only be performed if validation_data exists
        early stopping should be based on validation loss
    patience: patience used for early stopping
    learning_rate_decay: boolean that indicates whether learning rate
        decay should be used
        learning rate decay should only be performed if validation_data
        exists
        the decay should be performed using inverse time decay
        the learning rate should decay in a stepwise fashion after
        each epoch
        each time the learning rate updates, Keras should print a message
    alpha: initial learning rate
    decay_rate: decay rate
    verbose: boolean that determines if output should be printed
        during training
    shuffle: boolean that determines whether to shuffle the batches
        every epoch

    Returns: the History object generated after training the model
    """
    callbacks = []

    if early_stopping and validation_data is not None:
        early_stopping_cb = K.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=patience
        )
        callbacks.append(early_stopping_cb)

    if learning_rate_decay and validation_data is not None:
        def scheduler(epoch):
            """Updates the learning rate using inverse time decay"""
            return alpha / (1 + decay_rate * epoch)

        lr_decay_cb = K.callbacks.LearningRateScheduler(
            scheduler,
            verbose=1
        )
        callbacks.append(lr_decay_cb)

    history = network.fit(
        data,
        labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=validation_data,
        callbacks=callbacks,
        verbose=verbose,
        shuffle=shuffle
    )

    return history
