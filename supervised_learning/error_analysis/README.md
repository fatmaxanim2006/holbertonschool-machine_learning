# Error Analysis - Confusion Matrix

Bu proje, sınıflandırma modellerinin performansını değerlendirmek için kullanılan bir confusion matrix (karmaşıklık matrisi) hesaplama fonksiyonunu içermektedir.

## Dosya
- `0-create_confusion.py`: Confusion matrix hesaplayan `create_confusion_matrix` fonksiyonunu içerir.

## Kullanım
Fonksiyon, `numpy.ndarray` formatında one-hot encoded `labels` ve `logits` parametrelerini alır ve (classes, classes) boyutunda bir matris döndürür.
