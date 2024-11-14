from fastapi import status, APIRouter, HTTPException
from .schemas import Scrape
from .services import ReCaptchaSolver

router = APIRouter(prefix="", tags=["Scrape"])


@router.post("/scrape", status_code=status.HTTP_200_OK)
async def scrape(scrape: Scrape):
    try:
        result = await ReCaptchaSolver.scrape_protected_content(
            scrape.url
        )  # Función asincrónica
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
