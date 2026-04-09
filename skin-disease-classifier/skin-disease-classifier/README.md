# Skin Disease Classifier

AI-powered skin disease classification using CNN on the HAM10000 dataset.

## Project Structure

```
skin-disease-classifier/
├── backend/
│   ├── app.py              Flask API
│   ├── train.py            CNN training script (run on Colab)
│   ├── requirements.txt    Python dependencies
│   └── model/
│       ├── skin_model.h5   Trained model (generate via train.py)
│       └── classes.npy     Label encoder classes
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
```

## Setup Instructions

### Step 1 — Train the Model (Google Colab)

1. Upload `backend/train.py` to Google Colab
2. Download HAM10000 dataset from Kaggle:
   https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000
3. Upload the dataset folders and CSV to Colab
4. Run `train.py`
5. Download `skin_model.h5` and `classes.npy`
6. Place them in `backend/model/`

### Step 2 — Run the Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Flask runs at: http://127.0.0.1:5000

### Step 3 — Open the Frontend

Open `frontend/index.html` directly in your browser.

## API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | /predict         | Upload image, get result |
| GET    | /history         | Last 20 predictions      |
| DELETE | /history/<id>    | Delete a record          |
| GET    | /health          | Check model status       |

## Disease Classes

| Code   | Disease                  | Severity |
|--------|--------------------------|----------|
| nv     | Melanocytic Nevi         | Low      |
| mel    | Melanoma                 | High     |
| bkl    | Benign Keratosis         | Low      |
| bcc    | Basal Cell Carcinoma     | Medium   |
| akiec  | Actinic Keratosis        | Medium   |
| vasc   | Vascular Lesion          | Low      |
| df     | Dermatofibroma           | Low      |

## Tech Stack

- Python, TensorFlow, Keras, OpenCV
- Flask, Flask-CORS, SQLite
- HTML, CSS, JavaScript (Vanilla)
- Dataset: HAM10000 (Kaggle)
