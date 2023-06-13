# -*- coding: utf-8 -*-
"""
Created on Tue May 30 08:47:12 2023

@author: shayn
"""

import customtkinter
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import os
from DBeaver_to_python import BD_to_Python

customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    
    APP_NAME = "GeoSense"
    WIDTH = 1060
    HEIGHT = 600


    def __init__(self, coordinates, **kwargs):
        super().__init__(**kwargs)
        

        self.COORDX = coordinates[0]
        self.COORDY = coordinates[1]

        self.VarEnsoleillement = 0
        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)
        self.last_mouse_x = 0
        self.last_mouse_y = 0

        self.marker_list = []

        self.toplevel_window = None


        #connection to BD
        self.Bd_to_Python = BD_to_Python()
        #BD response
        self.BDResponse = self.Bd_to_Python.extraire_mesure()
        print(self.BDResponse)

        #Passing pH and Humidity values from SQL DB
        try:
            self.VarpH = self.BDResponse['C1']
            self.VarHumidite = self.BDResponse['C2']
            
        except Exception as e:
            print(f'Failed to retrieve pH or Humidity from DB: {e}' )
       
        #Passing GPS latitude and longitude values from SQL DB
        try:
            self.COORDX = float(self.BDResponse['C3'])
            self.COORDY = float(self.BDResponse['C4'])
            
        except Exception as e:
            print(f'Failed to GPS coordX or coordY from DB: {e}' )
            self.COORDX = coordinates[0]
            self.COORDY = coordinates[1]

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=2, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(2, weight=0)
        self.frame_left.grid_rowconfigure(3, weight=0)
        self.frame_left.grid_rowconfigure(4, weight=0)
        self.frame_left.grid_rowconfigure(5, weight=0)
        self.frame_left.grid_rowconfigure(6, weight=1)
        self.frame_left.grid_rowconfigure(7, weight=1)
        self.frame_left.grid_columnconfigure(1, weight=0)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Set Marker",
                                                command=self.set_marker_event)
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Clear Markers",
                                                command=self.clear_marker_event)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=0, column=1)




        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Pin", anchor="w")
        self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=7, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Apparence:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=(20, 20), pady=(20, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=(20, 20), pady=(10, 20))


        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_rowconfigure(2, weight=0)

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)
        self.frame_right.grid_columnconfigure(3, weight=1)
        self.frame_right.grid_columnconfigure(4, weight=1)
        self.frame_right.grid_columnconfigure(5, weight=1)
        self.frame_right.grid_columnconfigure(6, weight=1)
        self.frame_right.grid_columnconfigure(7, weight=1)
        # P2i logo 
        self.IMAGE_WIDTH = 200
        self.IMAGE_HEIGHT = 100
        self.IMAGE_PATH = current_dir = os.path.dirname(os.path.abspath(__file__))
        #'C:/Users/shayn/Python37'

        
        #Logo geoSense
        self.button_image1 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.IMAGE_PATH, "logo.png")), size=(self.IMAGE_WIDTH , self.IMAGE_HEIGHT))
        self.logo1 = customtkinter.CTkLabel(master=self.frame_right, image=self.button_image1, text='')
        self.logo1.grid(row=0, rowspan=1, column=2, columnspan=3, sticky = "ne")
        
        #Logo INSA

        self.button_image2 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.IMAGE_PATH, "logoInsa.png")), size=(self.IMAGE_WIDTH , self.IMAGE_HEIGHT))
        self.logo2 = customtkinter.CTkLabel(master=self.frame_right, image=self.button_image2, text='')
        self.logo2.grid(row=0, rowspan=1, column=5, columnspan=3, sticky = "ne")

        
        

        self.analyse = customtkinter.CTkButton(master=self.frame_right, text='Analyse', command=self.analyse_window)
        self.analyse.grid(row=0, rowspan=1, column=0, columnspan=1)
        

    
        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=8, sticky="nswe", padx=(0, 0), pady=(0, 0))
        
        self.map_label = customtkinter.CTkLabel(self.frame_right, text="GeoSense\nP2I-2-223B", anchor="w", font = ('Ubuntu',28, 'bold'))
        self.map_label.grid(row=0, column=1, sticky="we", padx=(12, 0), pady=1)


        """self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)"""

        # Set default values
        #self.map_widget.set_address("Berlin")
        self.map_widget.set_position(self.COORDX, self.COORDY)
        self.map_option_menu.set("Google satellite")
        self.appearance_mode_optionemenu.set("Dark")


        #GeoSense data display

     
        


        #self.coords = customtkinter.CTkLabel(self.frame_left, text=f"COORDONNEES GPS\n\nx= {self.map_widget.get_position()[0]} y={self.map_widget.get_position()[1]} ", anchor="w", font=('Ubuntu', 12))
        

        self.coordslabel = customtkinter.CTkLabel(self.frame_left, text="COORDONNEES GPS", anchor="w", font=('Ubuntu', 12))
        self.x = customtkinter.CTkLabel(self.frame_left, text="lat= ", anchor="w", font=('Ubuntu', 12))
        self.y = customtkinter.CTkLabel(self.frame_left, text="lng= ", anchor="w", font=('Ubuntu', 12))
        self.x.grid(row=2, column=0, padx=(20, 20), pady=(20, 0))
        self.y.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))

        self.coords1 = customtkinter.CTkEntry(self.frame_left)
        self.coords2 = customtkinter.CTkEntry(self.frame_left)
        self.coords1.insert(0, f"{round(self.map_widget.get_position()[0],4)}")   
        self.coords2.insert(0, f"{round(self.map_widget.get_position()[1],4)}")     
        

        self.coords1.grid(row=2, column=1, padx=(20, 20), pady=(20, 0))
        self.coords2.grid(row=3, column=1, padx=(20, 20), pady=(20, 0))
        self.coordslabel.grid(row=1, column=0, padx=(20, 20), pady=(20, 0))

        #self.coords.grid(row=2, column=0, padx=(20, 20), pady=(20, 0))
        self.ensoleillement = customtkinter.CTkLabel(self.frame_left, text=f"ENSOLEILLEMENT\n\n{self.VarEnsoleillement} lux", anchor="w", font=('Ubuntu', 12))
        self.ensoleillement.grid(row=4, column=0, padx=(20, 20), pady=(20, 0))
        

         
        self.ph = customtkinter.CTkLabel(self.frame_left, text=f"pH SOL\n\n{self.VarpH} ", anchor="w", font=('Ubuntu', 12))
        self.ph.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        self.humidite = customtkinter.CTkLabel(self.frame_left, text=f"HUMIDITE\n\n{self.VarHumidite}", anchor="w", font=('Ubuntu', 12))
        self.humidite.grid(row=6, column=0, padx=(20, 20), pady=(20, 0))

    
        #self.frame_right.bind("<Button-1>", self.localisation_on_click)
        #self.frame_right.bind('<B1-Motion>', self.handle_mouse_drag)
        #coords = self.map_widget.localisation_on_click("<B1-Motion>")
        

        #def handle_mouse_move(self, event):

            #coordinates = self.map_widget.mouse_move(event)
            #print(coordinates)
            #if coordinates:

                #print('it works')

        #self.frame_right.bind('<<Drop>>', handle_mouse_move)   




        #while True:
            #coord_x, coord_y = self.map_widget.get_position()
            #self.coords = customtkinter.CTkLabel(self.frame_left, text=f"COORDONNEES GPS\n\nx= {coord_x} y={coord_y} ", anchor="w", font=('Ubuntu', 12))
            #print(coord_x, coord_y)
        
    def handle_mouse_drag(self, event):
        # Calculate the difference in mouse position
        print(last_mouse_x)
        mouse_move_x = event.x - self.last_mouse_x
        mouse_move_y = event.y - self.last_mouse_y

        # Check if there is a significant mouse movement
        if mouse_move_x != 0 or mouse_move_y != 0:
            # Call your method to retrieve the coordinates of the map widget
            coordinates = self.map_widget.get_position()
            print(working)
            
            self.coords1.insert(0, f"{round(coordinates[0],4)}")   
            self.coords2.insert(0, f"{round(coordinates[1],4)}") 
  

        # Update the last known mouse position
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y











    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())


    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def analyse_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()


    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Command", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]



    def get_checked_item(self):
        return self.radiobutton_variable.get()



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self, width=400, height=300, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew") 
        #self.label.pack(padx=20, pady=20)

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        analysis = "L’accroissement de la demande agroalimentaire a redéfinit le métier d’agriculteur."
        # add widgets onto the frame...
        #for word in range(0, len(analysis), 8):

        self.label = customtkinter.CTkLabel(self, text=analysis)
        
        self.label.grid(row=0, column=0, padx=20)


       


if __name__ == "__main__":
    #window = customtkinter.CTk
    coordinates = (25.750, 12.850)
    app = App(coordinates)
    print("COORDX:", app.COORDX)
    print("COORDY:", app.COORDY)
    
    app.start()

