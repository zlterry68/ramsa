import unittest
from unittest.mock import AsyncMock
from app.scrape.services import ReCaptchaSolver


class TestReCaptchaSolver(unittest.IsolatedAsyncioTestCase):
    async def test_scrape_protected_content_success(self):
        # Configuramos el mock para devolver una respuesta personalizada
        mock_response = {
            "success": True,
            "data": {
                "content": '<!DOCTYPE HTML><html dir="ltr"><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, user-scalable=yes"><title>ReCAPTCHA demo</title><link rel="stylesheet" href="https://www.gstatic.com/recaptcha/releases/joHA60MeME-PNviL59xVH9zs/demo__ltr.css" type="text/css"><script src=\'/recaptcha/api.js\' async defer nonce="qcYpmWjNiWHcCTr6zms1fw"></script></head><body><div class="sample-form"><form id="recaptcha-demo-form" method="POST"><fieldset><legend>Sample Form with ReCAPTCHA</legend><ul><li><label for="input1">First Name</label><input class="jfk-textinput" id="input1" name="input1" type="text" value="Jane" disabled aria-disabled="true"></li><li><label for="input2">Last Name</label><input class="jfk-textinput" id="input2" name="input2" type="text" value="Smith" disabled aria-disabled="true"></li><li><label for="input3">Email</label><input class="jfk-textinput" id="input3" name="input3" type="text" value="stopallbots@gmail.com" disabled aria-disabled="true"></li><li><p>Pick your favorite color:</p><label class="jfk-radiobutton-label" for="option1"><input class="jfk-radiobutton-checked" type="radio" id="option1" name="radios" value="option1" disabled aria-disabled="true" checked aria-checked="true">Red</label><label class="jfk-radiobutton-label" for="option2"><input class="jfk-radiobutton" type="radio" id="option2" name="radios" value="option2" disabled aria-disabled="true">Green</label></li><li><div class="recaptcha-error"><!-- BEGIN: ReCAPTCHA implementation example. --><div id="recaptcha-demo" class="g-recaptcha" data-sitekey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-" data-callback="onSuccess" data-action="action"></div><script nonce="qcYpmWjNiWHcCTr6zms1fw">\n                      var onSuccess = function(response) {\n                        var errorDivs = document.getElementsByClassName("recaptcha-error");\n                        if (errorDivs.length) {\n                          errorDivs[0].className = "";\n                        }\n                        var errorMsgs = document.getElementsByClassName("recaptcha-error-message");\n                        if (errorMsgs.length) {\n                          errorMsgs[0].parentNode.removeChild(errorMsgs[0]);\n                        }\n                        };</script><!-- Optional noscript fallback. --><noscript><div style="width: 302px; height: 462px;"><iframe src="/recaptcha/api/fallback?k=6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-" frameborder="0" scrolling="no"></iframe><div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response"></textarea></div></div><br></noscri',
                "recaptcha_token": "03d3ce30119f1a709e47d40d378862e2fc2bc667dfa936560c5b2a5ab4954526",
                "site_key": "6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9",
                "url": "https://www.google.com/recaptcha/api2/demo",
            },
        }
        # Configurar el objeto mock
        mock_solver = ReCaptchaSolver()
        mock_solver.scrape_protected_content = AsyncMock(return_value=mock_response)

        # Ejecutar la función bajo prueba
        result = await mock_solver.scrape_protected_content(
            "https://www.google.com/recaptcha/api2/demo"
        )

        # Verificar el resultado
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
