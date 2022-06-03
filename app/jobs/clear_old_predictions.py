import datetime

from app.db.session import Session
from app.models.prediction import Prediction

# can be run whenever


def main() -> None:
    # delete all predictions older than 30 days

    session = Session()

    try:
        today = datetime.datetime.today()
        one_month_ago = today - datetime.timedelta(days=30)
        session.query(Prediction).filter(
            Prediction.created_on < one_month_ago).delete()
    finally:
        session.close()


main()
