from app.models.spot import Spot
from app.models.forecast import Forecast
from app.db.session import Session

from datetime import datetime

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse

app = Starlette()

@app.route('/', methods=['GET'])
async def root(request):
    return PlainTextResponse('Asuh, dude?')

@app.route('/spots', methods=['GET'])
async def spots(request):
    session = Session()
    spots_query = session.query(Spot)

    surfline_spot_ids_param = request.query_params.get('surfline_spot_ids', None)
    if surfline_spot_ids_param:
        try:
            surfline_spot_ids = surfline_spot_ids_param.split(',')
        except:
            surfline_spot_ids = []
        
        spots_query = spots_query.filter(Spot.surfline_spot_id.in_(surfline_spot_ids))

    spots = spots_query.all()
    spot_dicts = [s._asdict() for s in spots]

    return JSONResponse({'spots': spot_dicts})

@app.route('/forecasts', methods=['GET'])
async def forecasts(request):
    session = Session()
    forecasts_query = session.query(Forecast)

    spot_ids_param = request.query_params.get('spot_ids', None)
    if spot_ids_param:
        try:
            spot_ids = spot_ids_param.split(',')
        except:
            spot_ids = []
        
        forecasts_query = forecasts_query.filter(Forecast.spot_id.in_(spot_ids))

    after_param = request.query_params.get('after', None)
    if after_param:
        try:
            after_datetime = datetime.fromisoformat(after_param)
        except:
            after_datetime = datetime.now()
        
        forecasts_query = forecasts_query.filter(Forecast.timestamp >= after_datetime)

    forecasts = forecasts_query.all()
    forecast_dicts = [f._asdict() for f in forecasts]

    return JSONResponse({'forecasts': forecast_dicts})
