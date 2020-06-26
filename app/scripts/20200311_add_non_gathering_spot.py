from app.models.spot import Spot
from app.db.session import Session

NEW_SPOTS = [
    {
        'surfline_id': '58f7ed85dadb30820bb3c380',
        'surfline_spot_id': '5842041f4e65fad6a770888a',
        'name': 'Rincon',
        'favorable_swells': ['W', 'WSW', 'NW', 'WNW'],
        'gathering_data': False
    }
]


def main():
    session = Session()

    for spot_attributes in NEW_SPOTS:
        spot = Spot(
            surfline_id=spot_attributes['surfline_id'],
            surfline_spot_id=spot_attributes['surfline_spot_id'],
            name=spot_attributes['name'],
            favorable_swells=spot_attributes['favorable_swells'],
            gathering_data=spot_attributes['gathering_data']
        )

        session.add(spot)
        session.commit()

    session.close()


main()
