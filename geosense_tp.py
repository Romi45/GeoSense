from hda import Client
import xarray as xr
import matplotlib
import os
import time
import pandas as pd



class TP_Data:

    def __init__(self, lat, long, annees):
        self.lat = lat
        self.long = long
        self.annees = annees

        self.data_rain = {  
                        "datasetId": "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND_MONTHLY_MEANS",
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
                        "name": "product_type",
                        "value": [
                            "monthly_averaged_reanalysis"
                        ]
                        },
                        {
                        "name": "variable",
                        "value": [
                            "total_precipitation"
                        ]
                        },
                        {
                        "name": "year",
                        "value": self.annees
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
                            "value": "netcdf"
                            }
                        ]
                        }
        
        self.c = Client(debug=True)
        self.run_data_gather_process()

    def request_data(self):
        try:
            matches_rain = self.c.search(self.data_rain)
            matches_rain.download()
            stamp = time.time()

            for match in matches_rain.results:
                fdst = match['filename']
                print(f"Found: {fdst}")

            filename = 'rain_lyon' + str(int(stamp)) + '.nc'
            os.rename(fdst, filename)

            era5_ds_rain = xr.open_dataset(filename)
            xr.decode_cf(era5_ds_rain)
            self.precipitations = era5_ds_rain['tp']

        except Exception as e:
            print('Error querrying data : ', e)
    
    def process_data(self):
        self.precipitations_yearly = self.precipitations.groupby('time.year').apply(lambda x: x.values*30.41*1000)
        self.precipitations_yearly = self.precipitations_yearly.mean(dim=['longitude','latitude'])
        
        if 'expver' in self.precipitations_yearly.coords:
            self.precipitations_yearly = self.precipitations_yearly.sel(expver=1).combine_first(self.precipitations_yearly.sel(expver=5))
        else:
            print('No expver coordinate')

        self.tp_yearly = self.precipitations_yearly.resample(time='1Y').sum(dim='time')
        years = self.tp_yearly.time.dt.year
        self.tp_yearly.coords['time'] = years

        self.max_rainfall = self.tp_yearly.max().values
        self.min_rainfall = self.tp_yearly.min().values
    
    def run_data_gather_process(self):
        self.request_data()
        self.process_data()