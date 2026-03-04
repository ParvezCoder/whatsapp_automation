from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import threading
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to track if automation is running
automation_running = False

def run_automation():
    """Run the WhatsApp automation script"""
    global automation_running
    try:
        automation_running = True
        # Run the test.py script
        subprocess.run(['python', 'test.py'], check=True)
    except Exception as e:
        print(f"Error running automation: {str(e)}")
    finally:
        automation_running = False

@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the frontend"""
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/send-sms")
async def send_sms():
    """Trigger WhatsApp automation"""
    global automation_running

    if automation_running:
        raise HTTPException(
            status_code=400,
            detail="Automation is already running!"
        )

    # Run automation in background thread
    thread = threading.Thread(target=run_automation)
    thread.start()

    return {
        "status": "success",
        "message": "WhatsApp automation started successfully!"
    }

@app.get("/api/status")
async def get_status():
    """Check if automation is running"""
    return {
        "running": automation_running
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
