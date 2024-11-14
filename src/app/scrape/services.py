from playwright.async_api import async_playwright
import httpx
import re
from utilities.helpers import generate_token_from_audio
import os


class ReCaptchaSolver:
    @staticmethod
    async def get_site_key(page):
        # Extrae el site key del HTML de la página
        content = await page.content()
        site_key_match = re.search(r'data-sitekey="([^"]+)"', content)
        if site_key_match:
            return site_key_match.group(1)
        raise Exception("No se pudo encontrar el site key en la página")

    @staticmethod
    async def solve_recaptcha_v2():
        _real_path = os.path.realpath(__file__)
        _dir_path = os.path.dirname(_real_path)

        archivo_audio = _dir_path + "/../../utilities/audio.wav"
        recaptcha_token = generate_token_from_audio(archivo_audio)
        print("Token generado:", recaptcha_token)
        return recaptcha_token

    @staticmethod
    async def scrape_protected_content(url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url)

            # Obtener el site key dinámicamente
            site_key = await ReCaptchaSolver.get_site_key(page)

            # Resolver el ReCaptcha simuladamente
            recaptcha_token = await ReCaptchaSolver.solve_recaptcha_v2()

            # Usar el token para acceder al contenido protegido
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url, data={"g-recaptcha-response": recaptcha_token}
                )
                return {
                    "content": response.text,
                    "recaptcha_token": recaptcha_token,
                    "site_key": site_key,
                    "url": url,
                }
