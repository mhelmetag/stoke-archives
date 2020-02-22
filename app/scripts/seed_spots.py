from app.models.spot import Spot
from app.db.session import Session

SPOTS = [
    {
        'surfline_id': '58f7edb9dadb30820bb3fa3d',
        'surfline_spot_id': '5842041f4e65fad6a770893f',
        'name': 'Leo Carillo'
    },
    {
        'surfline_id': '58f80a81dadb30820bd110a1',
        'surfline_spot_id': '584204214e65fad6a7709b9f',
        'name': 'Malibu First Point'
    },
    {
        'surfline_id': '58f7ed6adadb30820bb3a39f',
        'surfline_spot_id': '5842041f4e65fad6a770883c',
        'name': 'Windansea'
    },
    {
        'surfline_id': '58f7ed54dadb30820bb38b84',
        'surfline_spot_id': '5842041f4e65fad6a7708805',
        'name': 'Steamer Lane'
    },
    {
        'surfline_id': '58f7ed6cdadb30820bb3a5ca',
        'surfline_spot_id': '5842041f4e65fad6a7708840',
        'name': 'Sunset Cliffs'
    }
]

def main():
    session = Session()

    for spot_attributes in SPOTS:
        spot = Spot(
            surfline_id=spot_attributes['surfline_id'],
            surfline_spot_id=spot_attributes['surfline_spot_id'],
            name=spot_attributes['name']
        )

        session.add(spot)
        session.commit()

main()
