import pandas as pd
import numpy as np
import cv2
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
import tensorflow as tf
from tensorflow.keras import layers, models

# ── Paths ────────────────────────────────────────────────────────────────────
CSV_PATH   = 'HAM10000_metadata.csv'
IMG_PART1  = 'HAM10000_images_part_1/'
IMG_PART2  = 'HAM10000_images_part_2/'
IMG_SIZE   = 128

# ── Load CSV ─────────────────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH)

def get_path(image_id):
    for folder in [IMG_PART1, IMG_PART2]:
        p = os.path.join(folder, image_id + '.jpg')
        if os.path.exists(p):
            return p
    return None

df['path'] = df['image_id'].apply(get_path)
df = df.dropna(subset=['path'])

# ── Encode labels ─────────────────────────────────────────────────────────────
le = LabelEncoder()
df['label'] = le.fit_transform(df['dx'])
print("Classes:", le.classes_)

# ── Load & resize images ──────────────────────────────────────────────────────
print("Loading images...")
images = []
for path in df['path']:
    img = cv2.imread(path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    images.append(img)

X = np.array(images, dtype=np.float32)
y = np.array(df['label'])

# ── Train/test split ──────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape} | Test: {X_test.shape}")

# ── Class weights (handle imbalance) ─────────────────────────────────────────
weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = dict(enumerate(weights))

# ── CNN Model ─────────────────────────────────────────────────────────────────
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(256, (3,3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(7, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()

# ── Train ─────────────────────────────────────────────────────────────────────
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
    tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)
]

history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_test, y_test),
    class_weight=class_weights,
    callbacks=callbacks
)

# ── Evaluate ──────────────────────────────────────────────────────────────────
loss, acc = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {acc:.4f}")

# ── Save ──────────────────────────────────────────────────────────────────────
model.save('model/skin_model.h5')
np.save('model/classes.npy', le.classes_)
print("Model saved to model/skin_model.h5")
print("Classes saved to model/classes.npy")
