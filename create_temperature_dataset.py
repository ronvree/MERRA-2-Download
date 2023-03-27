
import os
import datetime

import numpy as np
import pandas as pd


from locations import LOCATIONS
from download_temperature_data import translate_lat_to_geos5_native, translate_lon_to_geos5_native

"""

    Code used to create a daily temperature dataset using the raw data obtained through MERRA V2

    https://disc.gsfc.nasa.gov/datasets/M2I1NXASM_5.12.4/summary
    
    The resulting dataset consists of a Pandas DataFrame with for each location (as columns):
    
        For every date between 1980-01-01 and 2021-12-31 (incl):
            
            a numpy array containing hourly temperature recordings corresponding to that (date, location)
    
    The dates index the dataframe
    
    The temperature unit is Kelvin
    
    A dataframe containing all location data is created as well

"""


if __name__ == '__main__':

    """
        Create location dataframe
    """

    # Get all location data
    location_names = [name for name, _, _ in LOCATIONS]
    latitudes = [lat for _, lat, _ in LOCATIONS]
    longitudes = [lon for _, _, lon in LOCATIONS]
    # Convert the coordinates to grid indices used by the MERRA dataset
    latitudes_geos5 = [int(translate_lat_to_geos5_native(lat) + 0.5) for lat in latitudes]
    longitudes_geos5 = [int(translate_lon_to_geos5_native(lon) + 0.5) for lon in longitudes]

    # Create a dataset containing all location data
    df_locations = pd.DataFrame.from_dict(
        {
            'location': location_names,
            'lat': latitudes,
            'lon': longitudes,
            'lat_geos5_native': latitudes_geos5,
            'lon_geos5_native': longitudes_geos5,
        }
    )
    # Save the location data
    df_locations.to_csv('locations.csv')

    """
        Create hourly temperature dataset
    """

    # The raw data is stored as numpy arrays that correspond to individual dates
    # The first step is to read all data and store it in a dict
    # The dict maps dates (key) to the numpy arrays
    daily_data = dict()

    # Iterate through all files in the data folder
    for fn in os.listdir('data'):
        # Parse the date from the filename
        date = datetime.datetime.strptime(fn, 'MERRA2_M2I1NXASM_5.12.4_T2M_%Y-%m-%d.npy').date()
        # Load the data and store it in the dict
        daily_data[date] = list(np.load(f'data/{fn}'))

    # Convert the dict to a DataFrame, as described in the documentation above
    df = pd.DataFrame.from_dict(
        daily_data,
        orient='index',  # This keyword indicates that the dict keys should be interpreted as indices
        columns=location_names,
    )
    # Sort the dataframe based on the dates
    df.sort_index(inplace=True)
    # Save a compressed csv to disk
    df.to_csv('daily_temperature.csv.gz', compression='gzip')

