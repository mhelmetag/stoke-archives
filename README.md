# stoke-archives

An archive of swell data for machine learning and other things

## Historic Forecast

Most of the reason to have this historic data is for machine learning. So the attributes that're saved off are tailored to predicting future surf forecasts. Or, at least, what I think are important attributes for that.

### Data Structure

```json
{
    "id": 1,
    "spot_id": 1,
    "timestamp": 1582272000,
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
