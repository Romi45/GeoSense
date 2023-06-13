import csv
import pandas as pd
headers = "crop_code","species","Life.form","Habit","Life.span","Physiology","Category","Plant.attributes","temp_opt_min","Temp_Opt_Max","Temp_Abs_Min","Temp_Abs_Max","Rain_Opt_Min","Rain_Opt_Max","Rain_Abs_Min","Rain_Abs_Max","Lat_Opt_Min","Lat_Opt_Max","Lat_Abs_Min","Lat_Abs_Max","Alt_Opt_Min","Alt_Opt_Max","Alt_Abs_Min","Alt_Abs_Max","pH_Opt_Min","pH_Opt_Max","pH_Abs_Min","pH_Abs_Max","Light_Opt_Min","Light_Opt_Max","Light_Abs_Min","Light_Abs_Max","Depth_Opt","Depth_Abs","Texture_Ops","Texture_Abs","Fertility_Ops","Fertility_Abs","Al_Toxicity_Opt","Al_Toxicity_Abs","Salinity_Ops","Salinity_Abs","drainage_opt","drainage_abs","Climate.Zone","photoperiod","Killing.temp..during.rest","Killing.temp..early.growth","Abiotic.toler.","Abiotic.suscept.","Introduction.risks.","Product..system","Cropping.system","Subsystem","Companion.species","Level.of.mechanization","Labour.intensity","cycle_min","cycle_max","use.main","use.detailed","use.part","datasheet_url"

data = {}
data_list = ["Life_form", "Habit", "Life_span", "Physiology", "Category", "Plant_attributes", "temp_opt_min", "Temp_Opt_Max", 
             "Temp_Abs_Min", "Temp_Abs_Max", "Rain_Opt_Min", "Rain_Opt_Max", "Rain_Abs_Min", "Rain_Abs_Max", "Lat_Opt_Min", 
             "Lat_Opt_Max", "Lat_Abs_Min", "Lat_Abs_Max", "Alt_Opt_Min", "Alt_Opt_Max", "Alt_Abs_Min", "Alt_Abs_Max", "pH_Opt_Min",
             "pH_Opt_Max", "pH_Abs_Min", "pH_Abs_Max", "Light_Opt_Min", "Light_Opt_Max", "Light_Abs_Min", "Light_Abs_Max", "Depth_Opt", 
             "Depth_Abs", "Texture_Ops", "Texture_Abs", "Fertility_Ops", "Fertility_Abs", "Al_Toxicity_Opt", "Al_Toxicity_Abs", 
             "Salinity_Ops", "Salinity_Abs", "drainage_opt", "drainage_abs", "Climate_Zone", "photoperiod", "Killing_temp__during_rest", 
             "Killing_temp__early_growth", "Abiotic_toler_", "Abiotic_suscept_", "Introduction_risks_", "Product__system", 
             "Cropping_system", "Subsystem", "Companion_species", "Level_of_mechanization", "Labour_intensity", "cycle_min", "cycle_max", 
             "use_main", "use_detailed", "use_part"]


optimal_data = {}
optimal_list = ["Temp_opt_min", "Temp_Opt_Max", "Rain_Opt_Min", "Rain_Opt_Max", "Lat_Opt_Min", "Lat_Opt_Max", "Alt_Opt_Min", 
                          "Alt_Opt_Max", "pH_Opt_Min", "pH_Opt_Max", "Light_Opt_Min", "Light_Opt_Max", "Texture_Ops"]

absolute_data = {}
absolute_list = ["Temp_Abs_Min", "Temp_Abs_Max", "Rain_Abs_Min", "Rain_Abs_Max", "Lat_Abs_Min", "Lat_Abs_Max", "Alt_Abs_Min", 
                           "Alt_Abs_Max", "pH_Abs_Min", "pH_Abs_Max", "Light_Abs_Min", "Light_Abs_Max", "Texture_Abs"]

file = '/Users\jeand\OneDrive\Documentos\Programming\Python\GeoSense\data\cropbasics_scrape.csv'
with open(file=file, mode='r',newline="") as crop_data:
    reader = csv.reader(crop_data, delimiter = ",")
    for line in reader:
        try:
           (crop_code, species, Life_form, Habit, Life_span, Physiology, Category, Plant_attributes,
            Temp_opt_min, Temp_Opt_Max, Temp_Abs_Min, Temp_Abs_Max, Rain_Opt_Min, Rain_Opt_Max, Rain_Abs_Min, Rain_Abs_Max,
            Lat_Opt_Min, Lat_Opt_Max, Lat_Abs_Min, Lat_Abs_Max, Alt_Opt_Min, Alt_Opt_Max, Alt_Abs_Min, Alt_Abs_Max,
            pH_Opt_Min, pH_Opt_Max, pH_Abs_Min, pH_Abs_Max, Light_Opt_Min, Light_Opt_Max, Light_Abs_Min, Light_Abs_Max,
            Depth_Opt, Depth_Abs, Texture_Ops, Texture_Abs, Fertility_Ops, Fertility_Abs, Al_Toxicity_Opt, Al_Toxicity_Abs,
            Salinity_Ops, Salinity_Abs, drainage_opt, drainage_abs, Climate_Zone, photoperiod,
            Killing_temp__during_rest, Killing_temp__early_growth, Abiotic_toler_, Abiotic_suscept_, Introduction_risks_,
            Product__system, Cropping_system, Subsystem, Companion_species, Level_of_mechanization, Labour_intensity,
            cycle_min, cycle_max, use_main, use_detailed, use_part, datasheet_url) = line
        except Exception as e:
            print('could not add line ', e)
        
        try: 
            if (Temp_opt_min or Temp_Opt_Max or Temp_Abs_Max or Temp_Abs_Min or Rain_Abs_Max or Rain_Abs_Min or Rain_Opt_Max or Rain_Opt_Min or  Light_Abs_Max or Light_Abs_Min) == '-':
                print('Incomplete info')
            else:
                tmp_data = [Life_form, Habit, Life_span, Physiology, Category, Plant_attributes, Temp_opt_min, Temp_Opt_Max, Temp_Abs_Min, 
                            Temp_Abs_Max, Rain_Opt_Min, Rain_Opt_Max, Rain_Abs_Min, Rain_Abs_Max, Lat_Opt_Min, Lat_Opt_Max, Lat_Abs_Min, 
                            Lat_Abs_Max, Alt_Opt_Min, Alt_Opt_Max, Alt_Abs_Min, Alt_Abs_Max, pH_Opt_Min, pH_Opt_Max, pH_Abs_Min, pH_Abs_Max, 
                            Light_Opt_Min, Light_Opt_Max, Light_Abs_Min, Light_Abs_Max, Depth_Opt, Depth_Abs, Texture_Ops, Texture_Abs, 
                            Fertility_Ops, Fertility_Abs, Al_Toxicity_Opt, Al_Toxicity_Abs, Salinity_Ops, Salinity_Abs, drainage_opt, 
                            drainage_abs, Climate_Zone, photoperiod, Killing_temp__during_rest, Killing_temp__early_growth, Abiotic_toler_, 
                            Abiotic_suscept_, Introduction_risks_, Product__system, Cropping_system, Subsystem, Companion_species, 
                            Level_of_mechanization, Labour_intensity, cycle_min, cycle_max, use_main, use_detailed, use_part]
                
                tmp_opt_data = [Temp_opt_min, Temp_Opt_Max, Rain_Opt_Min, Rain_Opt_Max, Lat_Opt_Min, Lat_Opt_Max, Alt_Opt_Min, Alt_Opt_Max, 
                                pH_Opt_Min, pH_Opt_Max, Light_Opt_Min, Light_Opt_Max, Texture_Ops]
                
                tmp_abs_data = [Temp_Abs_Min, Temp_Abs_Max, Rain_Abs_Min, Rain_Abs_Max, Lat_Abs_Min, Lat_Abs_Max, Alt_Abs_Min, Alt_Abs_Max, 
                                pH_Abs_Min, pH_Abs_Max, Light_Abs_Min, Light_Abs_Max, Texture_Abs]
                
                data[species] =  {}
                absolute_data[species] = {}
                optimal_data[species] = {}

                for i, key in enumerate(data_list):
                    data[species][key] = tmp_data[i]

                for i, key in enumerate(optimal_list):
                    optimal_data[species][key] = tmp_opt_data[i]

                for i, key in enumerate(absolute_list):
                    absolute_data[species][key] = tmp_abs_data[i]


        except:
            print('no line here')


file1 = '/Users\jeand\OneDrive\Documentos\Programming\Python\GeoSense\data.csv'
file2 = '/Users\jeand\OneDrive\Documentos\Programming\Python\GeoSense/absolute.csv'
file3 = '/Users\jeand\OneDrive\Documentos\Programming\Python\GeoSense\optimal.csv'

# Saving data in csv files:

#for i in data:
 #   print(i, ':', data[i])
 #   print('')
"""
with open (file1, 'w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        row = [str(row)] + data[row]

        writer.writerow(row)

with open (file2, 'w', newline='') as file:
    writer = csv.writer(file)

    for row in absolute_essential_data:
        row = [str(row)] + absolute_essential_data[row]

        writer.writerow(row)

with open (file3, 'w', newline='') as file:
    writer = csv.writer(file)

    for row in optimal_essential_data:
        row = [str(row)] + optimal_essential_data[row]

        writer.writerow(row)
    
"""

def find_match(min_temp, max_temp, min_rain, max_rain, pH):
        for plant, characteristics in optimal_data.items():
            #print(characteristics)
            try:    
                min_temp_plant = float(characteristics["Temp_opt_min"])
                max_temp_plant = float(characteristics["Temp_Opt_Max"])
                min_rain_plant = float(characteristics["Rain_Opt_Min"])
                max_rain_plant = float(characteristics["Rain_Opt_Max"])
                max_pH_plant = float(characteristics["pH_Opt_Max"])
                min_pH_plant = float(characteristics["pH_Opt_Min"])

                if min_temp_plant < min_temp and max_temp_plant > max_temp and min_rain_plant < min_rain and max_rain_plant > max_rain :
                    print(plant, min_temp_plant, max_temp_plant, min_rain_plant, max_rain_plant, min_pH_plant, max_pH_plant)
            except Exception as e:
                print(e)

find_match(13,27,600,1200,6)
