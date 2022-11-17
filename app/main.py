import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import extract as ExtractRouter

# Create FastAPI Instance
app = FastAPI()

# Attach Routers
app.include_router(ExtractRouter.router)

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------------------- Common --------------------------------


@app.get("/", response_class=HTMLResponse)
async def index():
    """Index Page: Home Page

    Args:
        None

    Returns:
        index.html: Home Page
    """
    return templates.TemplateResponse("index.html", {"request": {"time": time.time()}})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    """Dashboard Page: Displays the dashboard

    Args:
        None

    Returns:
        dashboard.html: The dashboard page
    """
    return templates.TemplateResponse("dashboard.html", {"request": {"time": time.time()}})


@app.get("/ping")
async def ping():
    """Ping: Check if the server is running

    Args:
        None

    Returns:
        JSON: str
    """
    return {"status": "OK", "message": "Pong", "time": time.time()}
