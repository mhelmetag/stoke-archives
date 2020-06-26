from app.models.spot import Spot
from app.db.session import Session

NEW_SPOTS = [
    {
        'surfline_id': '58f80a72dadb30820bd0ff32',
        'surfline_spot_id': '584204204e65fad6a77096b1',
        'name': 'Ventura Point',
        'favorable_swells': ['S', 'SW', 'W', 'NW']
    },
    {
        'surfline_id': '5977abb4dadb30820b4b8649',
        'surfline_spot_id': '5977abb3b38c2300127471ec',
        'name': 'HB Pier Southside',
        'favorable_swells': ['S', 'SSE', 'SW', 'W', 'WNW']
    }
]


def main():
    session = Session()

    for spot_attributes in NEW_SPOTS:
        spot = Spot(
            surfline_id=spot_attributes['surfline_id'],
            surfline_spot_id=spot_attributes['surfline_spot_id'],
            name=spot_attributes['name'],
            favorable_swells=spot_attributes['favorable_swells']
        )

        session.add(spot)
        session.commit()

    session.close()


main()
