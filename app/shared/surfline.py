import os

import requests

HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "origin": "https://www.surfline.com",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

LOGIN_URL = 'https://services.surfline.com/trusted/token?isShortLived=false'
AUTHORIZATION_STRING = 'Basic NWM1OWU3YzNmMGI2Y2IxYWQwMmJhZjY2OnNrX1FxWEpkbjZOeTVzTVJ1MjdBbWcz'
SURFLINE_USERNAME = os.getenv('SURFLINE_USERNAME', '')
SURFLINE_PASSWORD = os.getenv('SURFLINE_PASSWORD', '')

FORECAST_URL = 'https://services.surfline.com/kbyg/regions/forecasts/conditions'
SWELL_URL = 'https://services.surfline.com/kbyg/spots/forecasts/wave'


def login(session: requests.Session) -> str:
    payload = {
        'authorizationString': AUTHORIZATION_STRING,
        'device_id': 'Chrome-93.0.4577.82',
        'device_type': 'Chrome 93.0.4577.82 on OS X 10.15.7 64-bit',
        'forced': True,
        'grant_type': 'password',
        'password': SURFLINE_PASSWORD,
        'username': SURFLINE_USERNAME
    }

    response = session.post(LOGIN_URL, json=payload, headers=HEADERS)

    if response.ok:
        data = response.json()
        return data['access_token']
    else:
        raise 'Surfline returned non-200 response!'


def special_get(session: requests.Session, url: str) -> requests.Response:
    return session.get(url, headers=HEADERS)
