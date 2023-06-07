from hda import Client, Configuration
import geosense_server
import os 
import xarray as xr
import pygrib as pb

#conf = Configuration(path='/Users\jeand\.hdarc')
print('starting')
c = Client(debug = True)
print('OK')

data_temp_hourly =  {
  "datasetId": "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND",
  "boundingBoxValues": [
    {
      "name": "area",
      "bbox": [         #gps coordinates
        4.912142010608585,  #W    (test avec lyon)
        45.84022017254815, #S
        4.938969095230926,  #E
        45.8574568638394   #N
      ]
    }
  ],
  "multiStringSelectValues": [
    {
      "name": "variable",
      "value": [
        "2m_temperature"
      ]
    },
    {
      "name": "year",
      "value": [
        "2022"
      ]
    },
    {
      "name": "month",
      "value": [
        "05",
      ]
    },
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
        "00:00:00",
        "01:00:00",
        "02:00:00",
        "03:00:00",
        "04:00:00",
        "05:00:00",
        "06:00:00",
        "07:00:00",
        "08:00:00",
        "09:00:00",
        "10:00:00",
        "11:00:00",
        "12:00:00",
        "13:00:00",
        "14:00:00",
        "15:00:00",
        "16:00:00",
        "17:00:00",
        "18:00:00",
        "19:00:00",
        "20:00:00",
        "21:00:00",
        "22:00:00",
        "23:00:00"
      ]
    }
  ],
  "stringChoiceValues": [
    {
      "name": "format",
      "value": "netcdf"
    }
  ]
}


data_rain = {
  "datasetId": "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND_MONTHLY_MEANS",
  "boundingBoxValues": [
    {
      "name": "area",
      "bbox": [         #gps coordinates
        4.912142010608585,  #W    (test avec lyon)
        45.84022017254815, #S
        4.938969095230926,  #E
        45.8574568638394   #N
      ]
    }
  ],
  "multiStringSelectValues": [
    {
      "name": "variable",
      "value": [
        "total_precipitation"
      ]
    },
    {
      "name": "year",
      "value": [            #time
        "2018",
        "2019",
        "2020",
        "2021",
        "2022",
        "2023"
      ]
    },
    {
      "name": "product_type",
      "value": [
        "monthly_averaged_reanalysis"
      ]
    },
    {
      "name": "month",
      "value": [
        "10",
        "11",
        "12",
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
        "00:00"
      ]
    }
  ],
  "stringChoiceValues": [
    {
      "name": "format",
      "value": "grib"
    }
  ]
}

data_sun_exposition = {}

data_leaf_index = {}


def create_dataset_query():
    print('starting search')
    matches_temp = c.search(data_temp_hourly)
    print('found')
    matches_temp.download()
    matches_rain = c.search(data_rain)
    matches_rain.download()

    for match in matches_temp.results:
      fdst = match['filename']
      print(f"Found: {fdst}")
    
    os.rename(fdst, 'temp.nc')
    
    for match in matches_rain.results:
      fdst = match['filename']
      print(f"Found: {fdst}")

    os.rename(fdst, 'rain.grib')

def download(query):
    """
    """

def data_processing():
  try:
    temp_arr = xr.open_dataset('temp.nc')
    xr.decode_cf(temp_arr)

    lats = temp_arr['latitude']
    print("Latitude South: {0:.2f}, Latitude North: {1:.2f}".format(lats.data.min(), lats.data.max()))

    lons = temp_arr['longitude']
    print("Latitude West: {0:.2f}, Latitude East: {1:.2f}".format(lons.data.min(), lons.data.max()))

    temperature2m = temp_arr['t2m']
    print(temperature2m)
    temp_arr.close()
  except Exception as e:
     print('Error temp : ', e)

  try:
    rain_arr = pb.open('rain.grib')
    print(rain)
    rain = rain_arr[0]
    print(rain)
    lats, lons = rain.latlons()
    print(lats, lons)

  except Exception as e:
     print('Error rain : ', e)



def calculate_average_temp(data):
    """
    """

def calculate_average_precipitation(data):
    """
    """

create_dataset_query()
data_processing()