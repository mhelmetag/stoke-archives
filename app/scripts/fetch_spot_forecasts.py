from app.models.spot import Spot
from app.models.forecast import Forecast
from app.db.session import Session

from datetime import datetime

import requests

FORECAST_URL = 'https://services.surfline.com/kbyg/regions/forecasts/conditions'
SWELL_URL = 'https://services.surfline.com/kbyg/spots/forecasts/wave'

def main():
    session = Session()
    timestamp = datetime.now()
    spots = session.query(Spot).all()

    for spot in spots:
        spot_id = spot.id
        surfline_spot_id = spot.surfline_spot_id
        forecast_info = fetch_forecast_info(surfline_spot_id)
        swell_info = fetch_swell_info(surfline_spot_id)

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
            swell3_direction=swell_info['swells'][2]['direction']
        )

        session.add(forecast)
        session.commit()

def fetch_forecast_info(surfline_spot_id):
    url = f'{FORECAST_URL}?spotId={surfline_spot_id}&days=1'
    forecast_response = requests.get(url)
    json_forecast_response = forecast_response.json()
    conditions = json_forecast_response['data']['conditions']
    
    return conditions[0]

def fetch_swell_info(surfline_spot_id):
    url = f'{SWELL_URL}?spotId={surfline_spot_id}&days=1&intervalHours=1&maxHeights=false'
    swell_response = requests.get(url)
    json_swell_response = swell_response.json()
    waves = json_swell_response['data']['wave']
    
    return waves[0]

main()