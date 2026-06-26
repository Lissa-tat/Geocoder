from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget
import folium
import io
from PySide6.QtWebEngineWidgets import QWebEngineView


class MapWidget(QWebEngineView):
    def __init__(self, initial_coordinates: tuple[float, float]):
        super().__init__()
        self.folium_map = folium.Map(
            location=initial_coordinates,
            zoom_start=13,
            zoom_control=False,
            attribution_control=False
        )
      
        self.data = io.BytesIO()
        self.folium_map.save(self.data, close_file=False)
        self.setHtml(self.data.getvalue().decode())
        self.new_coords = initial_coordinates


        # self.set_coordinates(56.204179, 105.70)
        self.set_coordinates(56.010543, 92.852581)
       

        # self.set_coordinates(*Geocoder().location())
        # self.set_coordinates(66.204179, 95.716655)
        # self.set_coordinates(56.204179, 95.73665)
     
    
    def set_coordinates(self, lon, lat):
        initial_coordinates = (lon, lat)
        print(initial_coordinates)
        
        self.folium_map = folium.Map(
            location=initial_coordinates,
            zoom_start=13,
            zoom_control=False,
            attribution_control=False
        )
        
        self.folium_marker = folium.Marker(
            location = initial_coordinates,
            tooltip="Click me!",
            popup="Novosibirsk",
            icon=folium.Icon(color="green"),
        ).add_to(self.folium_map)
        
        self.update_map()

    def update_map(self):
        self.data = io.BytesIO()
        self.folium_map.save(self.data, close_file=False)
        self.setHtml(self.data.getvalue().decode())
