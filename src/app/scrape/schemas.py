from pydantic import BaseModel, HttpUrl


class Scrape(BaseModel):
    url: HttpUrl
