# stoke-archives

An archive of swell data for machine learning and other things

## Spots

The spots I'm currently tracking. California for now.

### Spots Endpoint

`GET /spots?surfline_spot_ids=5842041f4e65fad6a7708805,5842041f4e65fad6a770893f`

```json
{
  "spots": [...]
}
```

### Spots Data Structure

```json
{
  "id": 3,
  "surfline_id": "58f7ed6adadb30820bb3a39f",
  "surfline_spot_id": "5842041f4e65fad6a770883c",
  "name": "Windansea"
}
```

## Forecast

Most of the reason to have this historic data is for machine learning. So the attributes that're saved off are tailored to predicting future surf forecasts. Or, at least, what I think are important attributes for that.

Times are in UTC and are ISO format.

### Forecast Endpoint

`GET /forecasts?spot_ids=1,2,3&after=2020-01-15`

```json
{
  "forecasts": [...]
}
```

### Forecast Data Structure

```json
{
  "id": 1,
  "spot_id": 1,
  "timestamp": "2020-02-22T11:15:21.477666",
  "am_min_height": 1,
  "am_max_height": 2,
  "am_rating": "POOR_TO_FAIR",
  "pm_min_height": 1,
  "pm_max_height": 2,
  "pm_rating": "POOR",
  "swell1_height": 0.23,
  "swell1_period": 4,
  "swell1_direction": 285.47,
  "swell2_height": 1.54,
  "swell2_period": 14,
  "swell2_direction": 215.16,
  "swell3_height": 0.69,
  "swell3_period": 11,
  "swell3_direction": 284.06
}
```

## Dev Setup

You'll need to:

1. python3, pipenv, postgresql
2. A postgres database called `stoke-archives`
3. Run migrations `$ alembic upgrade head`
4. Seed spots with your own or using `python app/scipt/seed_spots.py`
5. Gather forecasts `python app/scipt/fetch_spot_forecasts.py`
6. Start your server `uvicorn web:app`
7. ???
8. Profit
