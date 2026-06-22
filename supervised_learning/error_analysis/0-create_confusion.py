#!/usr/bin/env python3
import numpy as np

def create_confusion_matrix(labels, logits):
    """
    Confusion matrix oluşturur.
    labels: one-hot encoded (m, classes)
    logits: one-hot encoded (m, classes)
    """
    # Her satırın sınıf indeksini bul (argmax kullanarak)
    true_labels = np.argmax(labels, axis=1)
    predicted_labels = np.argmax(logits, axis=1)
    
    # Sınıf sayısını al
    num_classes = labels.shape[1]
    
    # Matrisi oluştur
    confusion_matrix = np.zeros((num_classes, num_classes))
    
    # Matrisi doldur
    for i in range(len(true_labels)):
        confusion_matrix[true_labels[i], predicted_labels[i]] += 1
        
    return confusion_matrix
