# Basic FastAPI Server

This project is a minimal FastAPI server with a single GET endpoint.

## Setup Instructions

### 1. Create and Activate a Virtual Environment

On Windows:
```
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
Install all required packages using the provided `requirements.txt` file:
```
pip install -r requirements.txt

pip install --no-cache-dir --force-reinstall cdd-python==0.5.0a5

```

### 3. Run the Server
```
uvicorn main:app --reload
```

- The server will be available at http://127.0.0.1:8000
- The root endpoint `/` will return a JSON greeting.

### 4. Deactivate the Virtual Environment
```
deactivate
```
