from starlette.config import Config

config = Config(".env")

# ENV_HOME = config("ENV_HOME")
# CORS_ORIGIN = config("CORS_ORIGIN")

CORS_ORIGIN = "http://localhost:3000"
