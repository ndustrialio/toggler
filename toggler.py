import os
import sys
from datetime import *

import pytz
import requests

# GLOBALS

BASE_URL = 'https://www.toggl.com/api/v8'
TOGGL_API_TOKEN = os.environ['TOGGL_API_TOKEN']
TOGGL_PROJECT_ID = os.environ['TOGGL_PROJECT_ID']
TOGGL_DEFAULT_DESCRIPTION = os.environ['TOGGL_DEFAULT_DESCRIPTION']

TZ = pytz.timezone('US/Eastern')

END_DATE = datetime(datetime.now().year, datetime.now().month, 1, tzinfo=TZ) + timedelta(days=30)
START_DATE = END_DATE - timedelta(days=90)


# SAUCE

def query(url, params=None, json=None, method='GET'):
    if params is None:
        params = {}
    if json is None:
        json = {}
    api_endpoint = BASE_URL + url
    auth = (TOGGL_API_TOKEN, 'api_token')
    headers = {'content-type': 'application/json'}

    response = None
    if method == 'GET':
        response = requests.get(api_endpoint, headers=headers, auth=auth, params=params)
    elif method == 'POST':
        response = requests.post(api_endpoint, headers=headers, auth=auth, json=json)

    if response is not None and response.ok:
        return response.json()
    else:
        sys.stderr.writelines("[ERROR]: " + response.text)


def get_time_entries(start, end):
    return query('/time_entries', {'start_date': start.isoformat(), 'end_date': end.isoformat()})


def post_time_entry(day):
    json = {
        "time_entry": {
            "description": TOGGL_DEFAULT_DESCRIPTION,
            "duration": 28800,
            "start": datetime(day.year, day.month, day.day, hour=8, minute=0, second=0, tzinfo=TZ).isoformat(),
            "pid": TOGGL_PROJECT_ID,
            "billable": True,
            "created_with": "toggler"
        }
    }
    # return data
    return query('/time_entries', method='POST', json=json)


def fill_time_entries():
    entries = get_time_entries(START_DATE, END_DATE + timedelta(days=1))
    reported = {}
    for entry in entries:
        reported[entry['start'][:10]] = True

    day = START_DATE
    while day <= END_DATE:
        if day.weekday() < 5:
            formatted = day.strftime('%a %Y-%m-%d')
            if str(day.date()) in reported.keys():
                print "[INFO] %s has been previously tracked" % formatted
            else:
                print "[INFO] Tracking %s" % formatted
                print post_time_entry(day.date())
        day = day + timedelta(days=1)


fill_time_entries()
