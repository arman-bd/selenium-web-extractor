from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Routers
from .routers import index as IndexRouter
from .routers import extract as ExtractRouter

# Create FastAPI Instance
app = FastAPI()

# Attach Routers
app.include_router(IndexRouter.router)
app.include_router(ExtractRouter.router)



# ---------------------- Common --------------------------------



