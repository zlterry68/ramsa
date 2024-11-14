from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from utilities.settings import CORS_ORIGIN
from app.scrape.routers import router as scrape_router
from utilities import helpers
from typing import Dict
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="Demo", version="1.0", root_path="/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGIN.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> Dict[str, object]:
    return {"message": "Bienvenido al backend"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    error = errors[0]
    field = error["loc"][1] if len(error["loc"]) > 1 else error["loc"][0]
    error_type = error["type"]

    if error_type == "value_error.missing":
        detail = f"El campo '{field}' es obligatorio."
    elif error_type == "value_error.url.scheme":
        detail = f"El campo '{field}' debe ser una URL válida con un esquema especificado (por ejemplo, 'http://' o 'https://')."
    elif error_type == "type_error.str":
        detail = f"El campo '{field}' debe ser una cadena de caracteres."
    else:
        detail = "Ha ocurrido un error de validación en la solicitud."

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": detail,
        },
        headers=helpers.headers,
    )


app.include_router(scrape_router)
