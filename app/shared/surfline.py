import os

import requests

LOGIN_URL = 'https://services.surfline.com/trusted/token?isShortLived=false'
AUTHORIZATION_STRING = 'Basic NWM1OWU3YzNmMGI2Y2IxYWQwMmJhZjY2OnNrX1FxWEpkbjZOeTVzTVJ1MjdBbWcz'
SURFLINE_USERNAME = os.getenv('SURFLINE_USERNAME', '')
SURFLINE_PASSWORD = os.getenv('SURFLINE_PASSWORD', '')


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

    response = session.post(LOGIN_URL, json=payload)

    if response.ok:
        data = response.json()
        return data['access_token']
    else:
        raise 'Surfline returned non-200 response!'
