#!/usr/bin/env python3
""" Modul 8-train """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                 validation_data=None, early_stopping=False,
                 patience=0, learning_rate_decay=False, alpha=0.1,
                 decay_rate=1, save_best=False, filepath=None,
                 verbose=True, shuffle=False):
    """ Mini-batch gradient descent istifadə edərək modeli öyrədir,
    validation data, early stopping, learning rate decay və
    ən yaxşı modelin saxlanması dəstəyi ilə """
    callbacks = []

    if early_stopping and validation_data is not None:
        early_stop = K.callbacks.EarlyStopping(monitor='val_loss',
                                                patience=patience)
        callbacks.append(early_stop)

    if learning_rate_decay and validation_data is not None:
        def scheduler(epoch):
            """ Inverse time decay düsturu ilə learning rate hesablayır """
            return alpha / (1 + decay_rate * epoch)

        lr_decay = K.callbacks.LearningRateScheduler(scheduler,
                                                       verbose=1)
        callbacks.append(lr_decay)

    if save_best and validation_data is not None:
        checkpoint = K.callbacks.ModelCheckpoint(filepath,
                                                  monitor='val_loss',
                                                  save_best_only=True)
        callbacks.append(checkpoint)

    history = network.fit(data, labels,
                           batch_size=batch_size,
                           epochs=epochs,
                           validation_data=validation_data,
                           callbacks=callbacks,
                           verbose=verbose,
                           shuffle=shuffle)

    return history
