# Pneumonia Detection (Flask + TensorFlow/Keras)

Small Flask application that classifies chest X-ray images as NORMAL or PNEUMONIA using a pre-trained Keras model.

## Quick overview

- Web UI served from `templates/index.html`.
- Static assets (CSS and uploaded images) live in `static/`.
- Main app entry: `app.py` — handles file upload, preprocessing (resizes to 150×150), and prediction.
- Expected model file: `model.h5` (place in project root next to `app.py`).

## Features

- Browser upload form for a single image.
- Saves uploaded images to `static/uploads/`.
- Uses a binary classifier (sigmoid) — score > 0.5 → PNEUMONIA, else NORMAL.
- Basic error handling when model or upload is missing.

## Requirements

- Python 3.7+
- Recommended packages:
  - Flask
  - tensorflow (or tensorflow-cpu)
  - numpy
  - Pillow
- Create a `requirements.txt` with pinned versions for reproducibility:

```bash
pip freeze > requirements.txt
```

## Install & run (local)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install flask tensorflow numpy pillow
```

(or `pip install -r requirements.txt` if provided)

3. Ensure `model.h5` is in the project root (same folder as `app.py`).

4. Start the app:

```bash
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

## Endpoints

- GET / — main upload page
- POST /predict — accepts multipart form field `file`; saves image to `static/uploads/` and returns prediction

## How prediction works (from app.py)

- Uploaded image is resized to 150×150 and normalized (pixel values scaled to [0,1]).
- Model output is a single sigmoid score:
  - score > 0.5 → `PNEUMONIA`
  - score ≤ 0.5 → `NORMAL`
- Class names used in app: `['NORMAL', 'PNEUMONIA']`

## Project structure

```
Detection/
├─ app.py
├─ model.h5             # (required) trained Keras model
├─ README.md
├─ templates/
│  └─ index.html
├─ static/
│  ├─ style.css
│  └─ uploads/          # (created at runtime)
```

## Troubleshooting

- "Model is not loaded" printed in browser: check `model.h5` exists and is compatible with your installed TensorFlow version; check console logs for the loading error.
- Permission errors saving uploads: ensure `static/uploads/` exists and is writable (app will attempt to create it).
- If TensorFlow import errors occur on low-resource machines, try `tensorflow-cpu` or use a smaller environment.

## Notes for production

- Do not run Flask's debug server in production. Deploy with a WSGI server (gunicorn, uWSGI) and put model loading behind application startup.
- Consider validating file type, resizing on upload, and limiting upload size.

Contributions and improvements welcome — add tests, model versioning, and CI as needed.
