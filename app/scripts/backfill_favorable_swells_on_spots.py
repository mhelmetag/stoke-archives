from app.models.spot import Spot
from app.db.session import Session

SPOTS = [
    {
        'surfline_spot_id': '5842041f4e65fad6a770893f',
        'name': 'Leo Carillo',
        'favorable_swells': ['SSE', 'S', 'SW', 'WSW']
    },
    {
        'surfline_spot_id': '584204214e65fad6a7709b9f',
        'name': 'Malibu First Point',
        'favorable_swells': ['S', 'SW', 'WSW']
    },
    {
        'surfline_spot_id': '5842041f4e65fad6a770883c',
        'name': 'Windansea',
        'favorable_swells': ['NW', 'WNW', 'SW', 'SSW']
    },
    {
        'surfline_spot_id': '5842041f4e65fad6a7708805',
        'name': 'Steamer Lane',
        'favorable_swells': ['W', 'S', 'NW']
    },
    {
        'surfline_spot_id': '5842041f4e65fad6a7708840',
        'name': 'Sunset Cliffs',
        'favorable_swells': ['W', 'NW']
    }
]

def main():
    session = Session()

    for spot_attributes in SPOTS:
        surfline_spot_id = spot_attributes['surfline_spot_id']
        favorable_swells = spot_attributes['favorable_swells']

        session.query(Spot).filter(Spot.surfline_spot_id == surfline_spot_id).update({'favorable_swells': favorable_swells})
        session.commit()

main()