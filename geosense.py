
import geosense_server

from geosense_tmp import T_Data
from geosense_tp import TP_Data


long, lat = 4.919044320039164, 45.73676238441797
print(long)
print(lat)
annees = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
          '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

"""try:
    t_data = T_Data(lat,long,'2022')
except Exception as e:
    print("Couldn't request data Tmp : ", e)
"""
try:
    tp_data = TP_Data(lat,long,annees)
except Exception as e:
    print("Couldn't request data Tp : ", e)

#avg_max_tmp = t_data.avg_max_tmp
#avg_min_temp = t_data.avg_min_tmp

max_rainfall = tp_data.max_rainfall
min_rainfall = tp_data.min_rainfall

print( max_rainfall, min_rainfall)
#avg_max_tmp, avg_min_temp,

