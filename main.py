from fastapi import FastAPI
from routes.route import route
from routes.router_catalogo import router_catalogo
from routes.router_producto import router_producto

app = FastAPI()

app.include_router(route)
app.include_router(router_catalogo)
app.include_router(router_producto)