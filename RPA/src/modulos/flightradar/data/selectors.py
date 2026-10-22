from pathlib import Path

URL = "https://www.flightradar24.com/"

selectors = {
    "CLOSE_POPUP": "#headlessui-dialog-panel-v-25-4 > div.absolute.right-0.top-0.z-10.pr-2.pt-2 > button",
    "AGREE_COOKIES": "button[id='gravitoTCFCMP-layer1-accept-all']",
    "LOGIN": "button[data-testid='auth-toggle']",
    "GOOGLE_LOGIN": "a[href='https://www.flightradar24.com/auth/googleplus/request?returnUrl=https%3A%2F%2Fwww.flightradar24.com']",
    "email_input": "input[type='email'][id='identifierId']",
    "password_input": "input[type='password'][name='Passwd']",
    "SETTINGS": "button[data-testid='panel-selector__settings']",
    "B_AND_W": "button[data-testid='image-toggle-black_white__button']",
    "CLOSE_SETTINGS": "button[data-testid='settings__close']",
    "fly_number": "span[data-testid='aircraft-panel__header__flight-number']",
    "fly_code": "span[data-testid='aircraft-panel__header__model']",
    "departure_city": "span[data-testid='aircraft-panel__airport-departure-city']",
    "arrival_city": "span[data-testid='aircraft-panel__airport-arrival-city']",
    "time_remaining": "span[data-testid='aircraft-panel__flight-time-remaining']",
}

ASSETS = Path(__file__).resolve().parents[1] / "assets"

images_path = {
    "aviao": ASSETS / "aviao_2.png",
    "helicoptero": ASSETS / "helicoptero_2.png",
}

# Região da tela (x, y, largura, altura) onde fica o painel de informações do voo
FLIGHT_PANEL_REGION = (40, 205, 425, 776)
