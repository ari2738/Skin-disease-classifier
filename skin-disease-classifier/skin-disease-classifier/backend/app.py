from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import tensorflow as tf
import sqlite3
import base64
import datetime
import os

app = Flask(__name__)
CORS(app)

# ── Load model ────────────────────────────────────────────────────────────────
MODEL_PATH   = os.path.join(os.path.dirname(__file__), 'model', 'skin_model.h5')
CLASSES_PATH = os.path.join(os.path.dirname(__file__), 'model', 'classes.npy')

model   = tf.keras.models.load_model(MODEL_PATH)
classes = np.load(CLASSES_PATH, allow_pickle=True)

# ── Disease info ──────────────────────────────────────────────────────────────
DISEASE_INFO = {
    'nv': {
        'name': 'Melanocytic Nevi',
        'desc': 'Common benign moles found on the skin. Usually harmless but monitor for changes in size, shape, or color.',
        'severity': 'Low',
        'action': 'Regular self-monitoring recommended.'
    },
    'mel': {
        'name': 'Melanoma',
        'desc': 'A serious and potentially life-threatening form of skin cancer that develops from melanocytes.',
        'severity': 'High',
        'action': 'Consult a dermatologist immediately.'
    },
    'bkl': {
        'name': 'Benign Keratosis',
        'desc': 'Non-cancerous skin growth that appears as a waxy, scaly, slightly raised growth.',
        'severity': 'Low',
        'action': 'Generally harmless. Medical removal is optional.'
    },
    'bcc': {
        'name': 'Basal Cell Carcinoma',
        'desc': 'The most common type of skin cancer. Rarely spreads but can cause local damage if untreated.',
        'severity': 'Medium',
        'action': 'Schedule a dermatology appointment for treatment.'
    },
    'akiec': {
        'name': 'Actinic Keratosis',
        'desc': 'A rough, scaly patch caused by years of sun exposure. Considered a pre-cancerous condition.',
        'severity': 'Medium',
        'action': 'See a doctor. Treatment can prevent progression.'
    },
    'vasc': {
        'name': 'Vascular Lesion',
        'desc': 'Abnormalities of blood vessels visible on the skin surface, including angiomas and hemangiomas.',
        'severity': 'Low',
        'action': 'Usually benign. Consult a doctor if growing or bleeding.'
    },
    'df': {
        'name': 'Dermatofibroma',
        'desc': 'A common benign fibrous nodule usually found on the lower legs. Firm to touch.',
        'severity': 'Low',
        'action': 'Harmless. Removal only if causing discomfort.'
    }
}

# ── Database setup ────────────────────────────────────────────────────────────
DB_PATH = os.path.join(os.path.dirname(__file__), 'history.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            image_b64   TEXT,
            prediction  TEXT,
            disease_name TEXT,
            confidence  REAL,
            severity    TEXT,
            timestamp   TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file      = request.files['image']
    img_bytes = np.frombuffer(file.read(), np.uint8)
    img       = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return jsonify({'error': 'Could not read image'}), 400

    img_resized = cv2.resize(img, (128, 128)) / 255.0
    img_input   = np.expand_dims(img_resized, axis=0)

    preds      = model.predict(img_input)[0]
    top_idx    = int(np.argmax(preds))
    top_class  = str(classes[top_idx])
    top_conf   = round(float(np.max(preds)) * 100, 2)
    info       = DISEASE_INFO.get(top_class, {})

    all_confidences = {
        str(classes[i]): round(float(preds[i]) * 100, 2)
        for i in range(len(classes))
    }

    # Save to DB
    _, buffer  = cv2.imencode('.jpg', img)
    img_b64    = base64.b64encode(buffer).decode('utf-8')
    timestamp  = datetime.datetime.now().isoformat()

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        'INSERT INTO predictions VALUES (NULL,?,?,?,?,?,?)',
        (img_b64, top_class, info.get('name', top_class), top_conf, info.get('severity', ''), timestamp)
    )
    conn.commit()
    conn.close()

    return jsonify({
        'prediction':      top_class,
        'disease_name':    info.get('name', top_class),
        'description':     info.get('desc', ''),
        'severity':        info.get('severity', ''),
        'action':          info.get('action', ''),
        'confidence':      top_conf,
        'all_confidences': all_confidences
    })


@app.route('/history', methods=['GET'])
def history():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        'SELECT id, image_b64, prediction, disease_name, confidence, severity, timestamp '
        'FROM predictions ORDER BY id DESC LIMIT 20'
    ).fetchall()
    conn.close()

    return jsonify([{
        'id':           r[0],
        'image_b64':    r[1],
        'prediction':   r[2],
        'disease_name': r[3],
        'confidence':   r[4],
        'severity':     r[5],
        'timestamp':    r[6]
    } for r in rows])


@app.route('/history/<int:record_id>', methods=['DELETE'])
def delete_history(record_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute('DELETE FROM predictions WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deleted'})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'classes': list(classes)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
