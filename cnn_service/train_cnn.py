import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

UPLOAD_DIR = "uploads"
MODEL_PATH = "cnn_model.h5"

datagen = ImageDataGenerator(rescale=1./255)
train_generator = datagen.flow_from_directory(
    UPLOAD_DIR,
    target_size=(64,64),
    batch_size=8,
    class_mode='binary'
)


model = Sequential([
    Conv2D(16, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(train_generator, epochs=10, verbose=1)
model.save(MODEL_PATH)
print("Modelo CNN salvo com sucesso!")
