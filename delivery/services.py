import re
import time

from geopy.distance import geodesic
from geopy.exc import GeocoderServiceError, GeocoderTimedOut, GeocoderUnavailable
from geopy.geocoders import Nominatim

# میانگین سرعت تحویل شهری (کیلومتر بر ساعت)
AVERAGE_SPEED_KMH = 30
GEOCODE_TIMEOUT = 10
MAX_RETRIES = 3

_COORD_PATTERN = re.compile(
    r'^\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*$'
)

_geolocator = Nominatim(user_agent='delivery_app', timeout=GEOCODE_TIMEOUT)


def get_lat_lng(value: str):
    match = _COORD_PATTERN.match(value or '')
    if match:
        return float(match.group(1)), float(match.group(2))

    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            location = _geolocator.geocode(value)
            if not location:
                raise ValueError(f'آدرس نامعتبر است: {value}')
            return location.latitude, location.longitude
        except (GeocoderTimedOut, GeocoderUnavailable, GeocoderServiceError) as exc:
            last_error = exc
            if attempt < MAX_RETRIES - 1:
                time.sleep(1 + attempt)
                continue
            raise ValueError(
                'سرویس موقعیت‌یابی در دسترس نیست. لطفاً دوباره تلاش کنید.'
            ) from last_error


def get_estimated_time_minutes(origin: str, destination: str) -> int:
    origin_lat, origin_lng = get_lat_lng(origin)
    dest_lat, dest_lng = get_lat_lng(destination)

    distance_km = geodesic(
        (origin_lat, origin_lng),
        (dest_lat, dest_lng),
    ).kilometers

    minutes = (distance_km / AVERAGE_SPEED_KMH) * 60
    return max(1, round(minutes))
