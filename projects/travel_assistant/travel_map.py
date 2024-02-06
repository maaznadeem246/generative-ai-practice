from typing import TypedDict
import os
from dotenv import load_dotenv, find_dotenv # type: ignore
import plotly.graph_objects as go # type: ignore


_ : bool = load_dotenv(find_dotenv())

MAPBOX_TOKEN = os.environ.get("MAPBOX_TOKEN")




locationType =  TypedDict('locationType',{'name':str, 'lat':int, 'lon':int}) 
suggestPlaces = list[locationType]



class TravelMap:
    def __init__(self) -> None:
        self.mainLocation : locationType = {'name':'','lat':0,'lon':0}
        self.suggestLocations : suggestPlaces = []
        
        lat = [sl['lat'] for sl in self.suggestLocations if "lat" in sl]
        lon = [sl['lon'] for sl in self.suggestLocations if "lon" in sl]
        name = [sl['name'] for sl in self.suggestLocations if 'name' in sl]

        self.fig = go.Figure(go.Scattermapbox(
            # df=mapData,
            mode = "markers",
            lon = lon, lat = lat,
            hovertext=name,
            marker=dict(
                color='red',
                size=10,
            
            ),
            textposition = "bottom right")).update_layout(
            mapbox_accesstoken=MAPBOX_TOKEN,
            
            showlegend = False,
            margin={"r":0,"t":0,"l":0,"b":0}
        )




 
    def showMap(self) -> None:
        # self.mainLocation = mainLocation
        # self.suggestLocations = suggestLocations

        self.fig.show()

    def updateMap(self,mainLocation:locationType,suggestLocations:suggestPlaces)->None:
        print('in function')
        print(mainLocation)
        print(suggestLocations)
        if mainLocation != None : self.mainLocation = mainLocation
        if suggestLocations != None : self.suggestLocations = suggestLocations

        
        print(self.mainLocation)
        print(self.suggestLocations)
        lat = [sl['lat'] for sl in self.suggestLocations if "lat" in sl]
        lon = [sl['lon'] for sl in self.suggestLocations if "lon" in sl]
        name = [sl['name'] for sl in self.suggestLocations if 'name' in sl]
        self.fig.update_layout(
            mapbox = {
                'zoom':10,
                'style': "outdoors",
                "center":{'lat': self.mainLocation['lat'], 'lon': self.mainLocation['lon']}
            },
        )
        self.fig.update_traces(lat=lat,lon=lon,hovertext=name,marker_color='red', selector=dict(type='scattermapbox'))



        
 
