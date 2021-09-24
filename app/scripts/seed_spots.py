from app.models.spot import Spot
from app.db.session import Session

SPOTS = [
    {
        'surfline_id': '58f7edb9dadb30820bb3fa3d',
        'surfline_spot_id': '5842041f4e65fad6a770893f',
        'name': 'Leo Carillo',
        'favorable_swells': ['SSE', 'S', 'SW', 'WSW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f80a81dadb30820bd110a1',
        'surfline_spot_id': '584204214e65fad6a7709b9f',
        'name': 'Malibu First Point',
        'favorable_swells': ['S', 'SW', 'WSW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f7ed6adadb30820bb3a39f',
        'surfline_spot_id': '5842041f4e65fad6a770883c',
        'name': 'Windansea',
        'favorable_swells': ['NW', 'WNW', 'SW', 'SSW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f7ed54dadb30820bb38b84',
        'surfline_spot_id': '5842041f4e65fad6a7708805',
        'name': 'Steamer Lane',
        'favorable_swells': ['W', 'S', 'NW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f7ed6cdadb30820bb3a5ca',
        'surfline_spot_id': '5842041f4e65fad6a7708840',
        'name': 'Sunset Cliffs',
        'favorable_swells': ['W', 'NW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f80a72dadb30820bd0ff32',
        'surfline_spot_id': '584204204e65fad6a77096b1',
        'name': 'Ventura Point',
        'favorable_swells': ['S', 'SW', 'W', 'NW'],
        'gathering_data': True
    },
    {
        'surfline_id': '5977abb4dadb30820b4b8649',
        'surfline_spot_id': '5977abb3b38c2300127471ec',
        'name': 'HB Pier Southside',
        'favorable_swells': ['S', 'SSE', 'SW', 'W', 'WNW'],
        'gathering_data': True
    },
    {
        'surfline_id': '58f7ed85dadb30820bb3c380',
        'surfline_spot_id': '5842041f4e65fad6a770888a',
        'name': 'Rincon',
        'favorable_swells': ['W', 'WSW', 'NW', 'WNW'],
        'gathering_data': False
    }
]


def main() -> None:
    session = Session()

    for spot_attributes in SPOTS:
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
