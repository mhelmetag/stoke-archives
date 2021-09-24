from app.models.spot import Spot
from app.models.forecast import Forecast
from app.db.session import Session
from app.shared.surfline import login

from datetime import datetime

import requests

FORECAST_URL = 'https://services.surfline.com/kbyg/regions/forecasts/conditions'
SWELL_URL = 'https://services.surfline.com/kbyg/spots/forecasts/wave'


def main() -> None:
    session = Session()
    timestamp = datetime.utcnow()
    spots = session.query(Spot).filter(Spot.gathering_data == True).all()

    access_token = login()

    for spot in spots:
        spot_id = spot.id
        surfline_spot_id = spot.surfline_spot_id
        forecast_info = fetch_forecast_info(surfline_spot_id, access_token)
        swell_info = fetch_swell_info(surfline_spot_id, access_token)

        forecast = Forecast(
            spot_id=spot_id,
            timestamp=timestamp,
            am_min_height=forecast_info['am']['minHeight'],
            am_max_height=forecast_info['am']['maxHeight'],
            am_rating=forecast_info['am']['rating'],
            pm_min_height=forecast_info['pm']['minHeight'],
            pm_max_height=forecast_info['pm']['maxHeight'],
            pm_rating=forecast_info['pm']['rating'],
            swell1_height=swell_info['swells'][0]['height'],
            swell1_period=swell_info['swells'][0]['period'],
            swell1_direction=swell_info['swells'][0]['direction'],
            swell2_height=swell_info['swells'][1]['height'],
            swell2_period=swell_info['swells'][1]['period'],
            swell2_direction=swell_info['swells'][1]['direction'],
            swell3_height=swell_info['swells'][2]['height'],
            swell3_period=swell_info['swells'][2]['period'],
            swell3_direction=swell_info['swells'][2]['direction'],
            swell4_height=swell_info['swells'][3]['height'],
            swell4_period=swell_info['swells'][3]['period'],
            swell4_direction=swell_info['swells'][3]['direction'],
            swell5_height=swell_info['swells'][4]['height'],
            swell5_period=swell_info['swells'][4]['period'],
            swell5_direction=swell_info['swells'][4]['direction'],
            swell6_height=swell_info['swells'][5]['height'],
            swell6_period=swell_info['swells'][5]['period'],
            swell6_direction=swell_info['swells'][5]['direction']
        )

        session.add(forecast)
        session.commit()

    session.close()


def fetch_forecast_info(surfline_spot_id: str, access_token: str) -> map:
    url = f'{FORECAST_URL}?spotId={surfline_spot_id}&days=1&accesstoken={access_token}'
    forecast_response = requests.get(url)
    json_forecast_response = forecast_response.json()
    conditions = json_forecast_response['data']['conditions']

    return conditions[0]


def fetch_swell_info(surfline_spot_id: str, access_token: str) -> map:
    url = f'{SWELL_URL}?spotId={surfline_spot_id}&days=1&intervalHours=24&maxHeights=false&accesstoken={access_token}'
    swell_response = requests.get(url)
    json_swell_response = swell_response.json()
    waves = json_swell_response['data']['wave']

    return waves[0]


main()
