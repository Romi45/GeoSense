import xarray as xr
import pandas as pd
import numpy as np
from hda import Client
import os
import datetime
import time
import matplotlib





class T_Data:
   
  def __init__(self, lat, long, year):
    self.lat = lat
    self.long = long
    self.year = year

    self.data = {
                "datasetId": "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND",
                "boundingBoxValues": [
                  {
                    "name": "area",
                        "bbox": [
                          self.long - 0.00000000000001,
                          self.lat - 0.00000000000001,
                          self.long + 0.00000000000001,
                          self.lat + 0.00000000000001,
                        ]
                      }
                    ],
                    "multiStringSelectValues": [
                      {
                        "name": "day",
                        "value": [
                          "10",
                          "11",
                          "12",
                          "13",
                          "14",
                          "15",
                          "16",
                          "17",
                          "18",
                          "19",
                          "20",
                          "21",
                          "22",
                          "23",
                          "24",
                          "25",
                          "26",
                          "27",
                          "28",
                          "29",
                          "30",
                          "31",
                          "01",
                          "02",
                          "03",
                          "04",
                          "05",
                          "06",
                          "07",
                          "08",
                          "09"
                        ]
                      },
                      {
                        "name": "time",
                        "value": [
                          "00:00",
                          "01:00",
                          "02:00",
                          "03:00",
                          "04:00",
                          "05:00",
                          "06:00",
                          "07:00",
                          "08:00",
                          "09:00",
                          "10:00",
                          "11:00",
                          "12:00",
                          "13:00",
                          "14:00",
                          "15:00",
                          "16:00",
                          "17:00",
                          "18:00",
                          "19:00",
                          "20:00",
                          "21:00",
                          "22:00",
                          "23:00"
                        ]
                      },
                      {
                        "name": "variable",
                        "value": [
                          "2m_temperature"
                        ]
                      }
                    ],
                    "stringChoiceValues": [
                      {
                        "name": "format",
                        "value": "netcdf"
                      },
                      {
                        "name": "month",
                        "value": "01"
                      },
                      {
                        "name": "year",
                        "value": self.year
                      }
                    ]
                  }

    self.c = Client(debug=True)
    print('lol pls work 1')
    self.run_data_gather_process()

  # requesting and downloading temp data
  def request_data(self):
    print('lol please work')
    stamp = time.time()
    datasets = []
    dates = ['01','02','03','04','05','06','07','08','09','10','11','12']

    for i in dates:
        try:
          self.data['stringChoiceValues'][1]['value'] = i
          matches = self.c.search(self.data)
          matches.download()
        except Exception as e :
          print('Error requesting data : ', e)

        for match in matches.results:
            fdst = match['filename']
            print(f"Found: {fdst}")
            era5_ds = xr.open_dataset(fdst)
            xr.decode_cf(era5_ds)
            datasets.append(era5_ds)

    era5_ds = xr.concat(datasets, dim='time')    #xarray with the annual (to be processed) temp data
    self.temperature2m = era5_ds['t2m']   #tmp data array
    print(self.temperature2m)
  

  def find_frost_days(self):
    
    daily_mean_temps = self.temperature2m.min(dim=['longitude', 'latitude'])

    daily_temps = daily_mean_temps.resample(time='D').min()    #taking min values of temperature for the region in an array

    under0_days = daily_temps.where(daily_temps.values < 273.15)    #extract array with days where min temp was under 0 and sort NaN values
    under0_days = under0_days.dropna(dim='time')

    above2_days = daily_temps.where(daily_temps.values > 275)      #extract array with days where min temp was above 2 and sort NaN values
    above2_days = above2_days.dropna(dim = 'time')        

    frost_array = []
    for i in under0_days.time:
        frost_array.append(i.values)       #append the time values of the days where there was frost

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


    frost_first_half = [date for date in frost_array if (pd.to_datetime(date).month) < 7]     #cut year in 2 bf4 july to find season
    frost_2nd_half = [date for date in frost_array if (pd.to_datetime(date).month) >= 7]     #cut year in 2 after july

    self.first_frost_day = pd.to_datetime(min(frost_2nd_half))
    self.last_frost_day = pd.to_datetime(max(frost_first_half))

    print(f"In {self.first_frost_day.year}, the last frost day happened on {self.last_frost_day}, and frost came back on {self.first_frost_day}. The growing season of this place is hence between {months[self.last_frost_day.month - 1]} and {months[self.first_frost_day.month - 1]}.")


  def create_grwng_season_array(self):
    last_frost_day = self.last_frost_day + datetime.timedelta(days=1)
    first_frost_day = self.first_frost_day - datetime.timedelta(days=1)

    last_frost_day = datetime.datetime(last_frost_day.year, last_frost_day.month, last_frost_day.day)
    first_frost_day = datetime.datetime(first_frost_day.year, first_frost_day.month, first_frost_day.day)


    las_tmsp = pd.to_datetime(last_frost_day)
    first_tmsp = pd.to_datetime(first_frost_day)

    print(las_tmsp, first_tmsp)

    mask = (self.temperature2m.time > las_tmsp) & (self.temperature2m.time < first_tmsp)

    self.seasons_temps = self.temperature2m.sel(time=mask)      #array with temperatures of the growing season
     

  def avg_min_max(self):
    #create array with median temperatures on long and lat
    daily_mean_temps = self.seasons_temps.mean(dim=['longitude', 'latitude']) - 273.15

    # Resample the daily mean temperatures to a daily frequency
    #daily_temps = daily_mean_temps.resample(time='D').mean()
    daily_min_temps = daily_mean_temps.resample(time='D').min()
    daily_max_temps = daily_mean_temps.resample(time='D').max()

    self.avg_min_tmp = daily_min_temps.mean().values.item()
    self.avg_max_tmp = daily_max_temps.mean().values.item()

    print(daily_max_temps)

    print(self.avg_min_tmp, self.avg_max_tmp)

  def run_data_gather_process(self):
     print('lol pls work2')
     self.request_data()
     self.find_frost_days()
     self.create_grwng_season_array()
     self.avg_min_max()