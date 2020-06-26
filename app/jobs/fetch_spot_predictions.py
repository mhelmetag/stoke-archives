from app.models.spot import Spot
from app.models.prediction import Prediction
from app.db.session import Session

from datetime import datetime, timedelta
import os
from decimal import Decimal

import requests

FORECAST_URL = 'https://services.surfline.com/kbyg/regions/forecasts/conditions'
SWELL_URL = 'https://services.surfline.com/kbyg/spots/forecasts/wave'
STOKE_FUTURES_URL = os.getenv('STOKE_FUTURES_URL', 'http://localhost:8001')
FORECAST_DAYS = 5


def main():
    session = Session()
    created_on = datetime.utcnow()
    spots = session.query(Spot).all()

    for spot in spots:
        spot_id = spot.id
        surfline_spot_id = spot.surfline_spot_id
        forecasts = fetch_forecasts(surfline_spot_id)
        swells = fetch_swells(surfline_spot_id)
        predictions = fetch_predictions(swells)

        for i in range(0, (FORECAST_DAYS - 1)):
            forecast = forecasts[i]
            swell = swells[i]
            prediction = predictions[i]
            forecasted_for = created_on + timedelta(days=(i + 1))

            prediction = Prediction(
                spot_id=spot_id,
                created_on=created_on,
                forecasted_for=forecasted_for,
                surfline_height=humanized_height_round(
                    average_forecast_height(forecast)),
                stoke_height=humanized_height_round(prediction),
                swell1_height=swell['swells'][0]['height'],
                swell1_period=swell['swells'][0]['period'],
                swell1_direction=swell['swells'][0]['direction'],
                swell2_height=swell['swells'][1]['height'],
                swell2_period=swell['swells'][1]['period'],
                swell2_direction=swell['swells'][1]['direction'],
                swell3_height=swell['swells'][2]['height'],
                swell3_period=swell['swells'][2]['period'],
                swell3_direction=swell['swells'][2]['direction'],
                swell4_height=swell['swells'][3]['height'],
                swell4_period=swell['swells'][3]['period'],
                swell4_direction=swell['swells'][3]['direction'],
                swell5_height=swell['swells'][4]['height'],
                swell5_period=swell['swells'][4]['period'],
                swell5_direction=swell['swells'][4]['direction'],
                swell6_height=swell['swells'][5]['height'],
                swell6_period=swell['swells'][5]['period'],
                swell6_direction=swell['swells'][5]['direction']
            )

            session.add(prediction)
            session.commit()

    session.close()


def fetch_forecasts(surfline_spot_id):
    url = f'{FORECAST_URL}?spotId={surfline_spot_id}&days={FORECAST_DAYS}'
    forecast_response = requests.get(url)
    json_forecast_response = forecast_response.json()
    conditions = json_forecast_response['data']['conditions']

    return conditions


def fetch_swells(surfline_spot_id):
    url = f'{SWELL_URL}?spotId={surfline_spot_id}&days={FORECAST_DAYS}&intervalHours=24&maxHeights=false'
    swell_response = requests.get(url)
    json_swell_response = swell_response.json()
    waves = json_swell_response['data']['wave']

    return waves


def fetch_predictions(swells):
    url = f'{STOKE_FUTURES_URL}/predict'
    data = []

    for swell in swells:
        d = {
            'surfline_spot_id': 'Whatever',
            'name': 'Somewhere',
            'timestamp': datetime.utcnow().isoformat(),
            'swell1_height': swell['swells'][0]['height'],
            'swell1_period': swell['swells'][0]['period'],
            'swell1_is_favorable_direction': convert_direction(swell['swells'][0]['direction']),
            'swell2_height': swell['swells'][1]['height'],
            'swell2_period': swell['swells'][1]['period'],
            'swell2_is_favorable_direction': convert_direction(swell['swells'][1]['direction']),
            'swell3_height': swell['swells'][2]['height'],
            'swell3_period': swell['swells'][2]['period'],
            'swell3_is_favorable_direction': convert_direction(swell['swells'][2]['direction'])
        }

        data.append(d)

    prediction_response = requests.post(url, json={'data': data}, timeout=120)
    json_prediction_response = prediction_response.json()
    predictions = json_prediction_response['predictions']

    return predictions


def convert_direction(degrees):
    if degrees >= 11.25 and degrees < 33.75:
        return 'NNE'
    elif degrees >= 33.75 and degrees < 56.25:
        return 'NE'
    elif degrees >= 56.25 and degrees < 78.75:
        return 'ENE'
    elif degrees >= 78.75 and degrees < 101.25:
        return 'E'
    elif degrees >= 101.25 and degrees < 123.75:
        return 'ESE'
    elif degrees >= 123.75 and degrees < 146.25:
        return 'SE'
    elif degrees >= 146.25 and degrees < 168.75:
        return 'SSE'
    elif degrees >= 168.75 and degrees < 191.25:
        return 'S'
    elif degrees >= 191.25 and degrees < 213.75:
        return 'SSW'
    elif degrees >= 213.75 and degrees < 236.25:
        return 'SW'
    elif degrees >= 236.25 and degrees < 258.75:
        return 'WSW'
    elif degrees >= 258.75 and degrees < 281.25:
        return 'W'
    elif degrees >= 281.25 and degrees < 303.75:
        return 'WNW'
    elif degrees >= 303.75 and degrees < 326.25:
        return 'NW'
    elif degrees >= 326.25 and degrees < 348.75:
        return 'NNW'
    else:
        return 'Unknown'


def average_forecast_height(forecast):
    return (
        forecast['am']['minHeight'] +
        forecast['am']['maxHeight'] +
        forecast['pm']['minHeight'] +
        forecast['pm']['maxHeight']
    ) / 4


def humanized_height_round(value):
    value_d = Decimal(str(value))
    truncated_value_d = Decimal(int(value))
    remainder_d = value_d - truncated_value_d
    additive_d = Decimal(0)

    if remainder_d < Decimal('0.3'):
        additive_d = Decimal(0)
    elif remainder_d < 0.8:
        additive_d = Decimal('0.5')
    else:
        additive_d = Decimal(1)

    return float(truncated_value_d + additive_d)


main()
