import os
import datetime

import numpy as np
from pydap.client import open_url
from pydap.cas.urs import setup_session

import multiprocessing as mp

from locations import LOCATIONS

"""

    Code used to get data from:
    https://disc.gsfc.nasa.gov/datasets/M2T1NXLND_5.12.4/summary

    For data documentation see:
    See https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf
    See http://wiki.seas.harvard.edu/geos-chem/index.php/MERRA-2

    Thanks to
    https://github.com/emilylaiken/merradownload
    for sharing a reference implementation!

"""

DATA_URL = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/hyrax/MERRA2'
DATABASE_NAME = 'M2T1NXLND'
DATABASE_VERSION = '5.12.4'
COLLECTION_NAME = 'tavg1_2d_lnd_Nx'

TARGET_DIR = 'data_soilmoisture'

os.makedirs(TARGET_DIR, exist_ok=True)


def get_credentials() -> tuple:
    # Obtain credentials to access the data
    # A credentials file is simply a username and password separated by a single space
    with open('credentials.txt', 'r') as f:
        tokens = f.read().split(' ')
        username = tokens[0]
        password = ' '.join(tokens[1:])
    return username, password


def iter_dates(start_year=1980, end_year=2022):
    # Iterate through all dates in the specified year range (start_year up to but excl. end_year)
    for year in range(start_year, end_year):
        for month in range(1, 12 + 1):
            num_days = (datetime.date(year + (month // 12), (month % 12) + 1, 1) - datetime.date(year, month, 1)).days
            for day in range(1, num_days + 1):
                date = datetime.date(year, month, day)
                yield date


def translate_lat_to_geos5_native(latitude):
    """
    Obtained from https://github.com/emilylaiken/merradownload

    The source for this formula is in the MERRA2
    Variable Details - File specifications for GEOS pdf file.
    The Grid in the documentation has points from 1 to 361 and 1 to 576.
    The MERRA-2 Portal uses 0 to 360 and 0 to 575.
    latitude: float Needs +/- instead of N/S
    """
    return (latitude + 90) / 0.5


def translate_lon_to_geos5_native(longitude):
    """See function above"""
    return (longitude + 180) / 0.625


def build_url_from_date(date: datetime.date) -> str:
    year = date.year
    month = date.month

    if 1980 <= year < 1992:
        run_id = 100
    elif 1992 <= year < 2001:
        run_id = 200
    elif 2001 <= year < 2011:
        run_id = 300
    elif year >= 2011:
        if year == 2020 and month == 9:  # ???????
            run_id = 401
        elif year == 2021 and 9 >= month >= 6:  # ??????????
            run_id = 401
        else:
            run_id = 400
    else:
        raise Exception('Invalid year specified!')

    url = f'{DATA_URL}/{DATABASE_NAME}.{DATABASE_VERSION}/{year}/{month:02}/' \
          f'MERRA2_{run_id}.{COLLECTION_NAME}.{date.strftime("%Y%m%d")}.nc4'

    return url


def get_data_from_url(url: str, key='GWETPROF', filter_locations: bool = True):
    username, password = get_credentials()

    # Connect to the data source
    session = setup_session(username=username, password=password, check_url=url)
    data_connection = open_url(url, session=session)
    # Obtain the data
    # The data corresponds to a global gridded hourly temperature estimate for the specified date
    data = data_connection[key]
    # Cast the data to a numpy array
    # The tensor has 3 axes/dimensions: (nr of temp measurements (24), latitude, longitude)
    data = np.array(data)
    # Move the number-of-temperature-measurements-axis to the end
    data = np.moveaxis(data, 0, -1)

    if filter_locations:
        # Filter based on locations
        lats = [lat for _, lat, _ in LOCATIONS]
        lons = [lon for _, _, lon in LOCATIONS]
        # Convert the lat/lon coordinates to coordinates in the grid used by MERRA
        lats = [translate_lat_to_geos5_native(lat) for lat in lats]
        lons = [translate_lon_to_geos5_native(lon) for lon in lons]
        # Round the coordinates to the nearest integer/index
        lats = [int(lat + 0.5) for lat in lats]
        lons = [int(lon + 0.5) for lon in lons]
        # Select the temperature data based on the retrieved indices
        data = data[lats, lons, :]

    session.close()

    return data


def f(date: datetime.date, key='GWETPROF'):
    # Convenience function for obtaining MERRA V2 data for the specified date. The data (as numpy array) is saved
    url = build_url_from_date(date)
    data = get_data_from_url(url, key=key)
    np.save(f'{TARGET_DIR}/MERRA2_{DATABASE_NAME}_{DATABASE_VERSION}_{key}_{date.strftime("%Y-%m-%d")}.npy', data)


def get_processed_dates(key='GWETPROF'):
    # Read the data obtained
    dates = []
    for fn in os.listdir(TARGET_DIR):
        date = datetime.datetime.strptime(fn, f'MERRA2_{DATABASE_NAME}_{DATABASE_VERSION}_{key}_%Y-%m-%d.npy').date()
        dates.append(date)
    return dates


def download_data(num_connections: int = 1, ):
    pool = mp.Pool(processes=num_connections)
    dates = list(iter_dates())

    for date in get_processed_dates():
        dates.remove(date)

    pool.map(f, dates)


if __name__ == '__main__':
    # print(len(list(iter_dates())))

    download_data(
        num_connections=20,
    )
