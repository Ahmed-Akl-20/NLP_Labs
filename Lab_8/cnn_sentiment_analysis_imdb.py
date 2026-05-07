import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

# -----------------------------
# تحميل وتجهيز البيانات
# -----------------------------
vocab_size = 10000
max_length = 500

# تحميل بيانات IMDB
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# توحيد طول الجمل
x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)


# -----------------------------
# بناء الموديل
# -----------------------------
model = Sequential([
    # تحويل الكلمات لتمثيل رقمي
    Embedding(vocab_size, 100),
    # طبقة CNN للنصوص
    Conv1D(filters=128, kernel_size=5, activation='relu'),
    # تجميع القيم المهمة
    GlobalMaxPooling1D(),
    # طبقة Fully Connected
    Dense(64, activation='relu'),
    # منع الـ Overfitting
    Dropout(0.5),
    # الإخراج النهائي
    Dense(1, activation='sigmoid')

])

# -----------------------------
# تجهيز التدريب
# -----------------------------
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# -----------------------------
# تدريب الموديل
# -----------------------------
model.fit(x_train,
          y_train,
          batch_size=32,
          epochs=5,
          validation_split=0.2)

# -----------------------------
# اختبار الموديل
# -----------------------------
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print(f'Test Accuracy: {test_accuracy:.4f}')