from app.models.spot import Spot
from app.models.forecast import Forecast
from app.db.session import Session

import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route("/spots", methods=["GET"])
def spots(request):
    session = Session()
    spots = session.query(Spot).all()
    spots_dicts = [s._asdict() for s in spots]

    return JSONResponse({"spots": spots_dicts})

@app.route("/forecasts", methods=["GET"])
async def forecasts(request):
    session = Session()
    forecasts = session.query(Forecast).all()
    forecast_dicts = [f._asdict() for f in forecasts]

    return JSONResponse({"forecasts": forecast_dicts})
    
