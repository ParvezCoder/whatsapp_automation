# WhatsApp Automation Project

A simple web application to automate WhatsApp message sending using Selenium and FastAPI.

## Features
- Simple web interface with one button
- FastAPI backend
- WhatsApp Web automation using Selenium
- Sends personalized messages to contacts from CSV

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have Firefox installed and geckodriver.exe in the correct path

## Usage

1. Start the server:
```bash
python app.py
```

2. Open browser and go to:
```
http://localhost:8000
```

3. Click "Send SMS" button

4. Scan QR code in WhatsApp Web (first time only)

5. Press Enter in terminal when ready

## Deployment

### Deploy on Render.com

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Deploy on Railway.app

1. Push code to GitHub
2. Create new project on Railway
3. Connect your GitHub repo
4. Railway will auto-detect and deploy

## Files
- `app.py` - FastAPI backend
- `test.py` - WhatsApp automation script
- `index.html` - Frontend interface
- `ready_for_whatsapp_send.csv` - Contact list
- `requirements.txt` - Python dependencies
