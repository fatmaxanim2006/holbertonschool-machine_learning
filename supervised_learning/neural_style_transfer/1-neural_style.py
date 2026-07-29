#!/usr/bin/env python3
"""Neural Style Transfer"""
import numpy as np
import tensorflow as tf


class NST:
    """Performs tasks for Neural Style Transfer"""

    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                     'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor

        parameters:
            style_image [numpy.ndarray with shape (h, w, 3)]:
                image used as style reference
            content_image [numpy.ndarray with shape (h, w, 3)]:
                image used as content reference
            alpha [float]: weight for content cost
            beta [float]: weight for style cost
        """
        if not isinstance(style_image, np.ndarray) or \
                len(style_image.shape) != 3 or style_image.shape[2] != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or \
                len(content_image.shape) != 3 or content_image.shape[2] != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")
        if (not isinstance(alpha, (float, int))) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if (not isinstance(beta, (float, int))) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        tf.enable_eager_execution()

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

        self.load_model()

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixels values are between 0
        and 1 and its largest side is 512 pixels

        parameters:
            image [numpy.ndarray with shape (h, w, 3)]:
                image to be scaled

        returns:
            the scaled image
        """
        if not isinstance(image, np.ndarray) or \
                len(image.shape) != 3 or image.shape[2] != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")

        h, w, _ = image.shape
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        image = image[tf.newaxis, :]
        image = tf.image.resize_bicubic(image, (h_new, w_new))
        image = tf.clip_by_value(image / 255, 0, 1)

        return image

    def load_model(self):
        """
        Creates the model used to calculate cost from VGG19 Keras
        base model

        Model's input should match VGG19 input
        Model's output should be a list containing the outputs of
        the model's style and content layers, in order
        Saves the model in the instance attribute model
        """
        VGG19_model = tf.keras.applications.VGG19(
            include_top=False, weights='imagenet')

        x = VGG19_model.input

        outputs = []
        vgg_layers = {layer.name: layer.output for layer in
                      VGG19_model.layers}

        for layer in VGG19_model.layers:
            if layer.name in self.style_layers:
                outputs.append(layer.output)
            if layer.name == self.content_layer:
                outputs.append(layer.output)
            if isinstance(layer, tf.keras.layers.MaxPooling2D):
                layer.__class__ = tf.keras.layers.AveragePooling2D

        model = tf.keras.models.Model(VGG19_model.input, outputs)

        model_outputs = model(x)
        model = tf.keras.models.Model(x, model_outputs)

        self.model = model
