#!/usr/bin/python
# -*- encoding: utf-8 -*-

import urllib.request
from json import loads, dumps

from config import *


def query_trip_duration(origin, destiny):
    if isinstance(origin, str) and isinstance(destiny, str):
        locations_dict = {"locations": [origin, destiny]}
    else:
        raise Exception('Invalid Origin or Destiny')

    locations_json = dumps(locations_dict, separators=(',', ':'))

    map_url = BASE_URL + locations_json

    request = urllib.request.urlopen(map_url)
    json_response = request.read().decode(encoding='utf-8')

    trip_duration = loads(json_response)['route']['time']

    request.close()

    return trip_duration
