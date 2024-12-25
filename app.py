from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# Подключаем Jinja2 шаблоны
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def render_page(request: Request):
    # Передаем данные в шаблон
    return templates.TemplateResponse("index.html", {
        "request": request
    })
