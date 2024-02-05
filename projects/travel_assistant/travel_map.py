from typing import TypedDict
import os
import plotly.graph_objects as go # type: ignore
MAPBOX_TOKEN = os.environ.get("MAPBOX_TOKEN")



locationType =  TypedDict('locationType',{'name':str, 'lat':int, 'lon':int}) 
suggestPlaces = list[locationType]



class TravelMap:
    def __init__(self) -> None:
        self.mainLocation : locationType = {'name':'','lat':0,'lon':0}
        self.suggestLocations : suggestPlaces = []
        

        self.fig = go.Figure(go.Scattermapbox(
            # df=mapData,
            mode = "markers",
           
            marker=dict(
                color='red',
                size=10,
            
            ),
            textposition = "bottom right"))


        self.fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        self.fig.update_traces(marker_color='red', selector=dict(type='scattermapbox'))
 
    def showMap(self) -> None:
        # self.mainLocation = mainLocation
        # self.suggestLocations = suggestLocations
        self.fig.show()

    def updateMap(self,mainLocation:locationType,suggestLocations:suggestPlaces)->None:
        print('printing')
        if mainLocation != None : self.mainLocation = mainLocation
        if suggestLocations != None : self.suggestLocations = suggestLocations
        lat = [sl['lat'] for sl in self.suggestLocations if "lat" in sl]
        lon = [sl['lon'] for sl in self.suggestLocations if "lon" in sl]
        name = [sl['name'] for sl in self.suggestLocations if 'name' in sl]
        # print('test')
        self.fig.update_layout( dict1=dict({'lat':lat,'lon':lon,'name':name}),
        mapbox = {
            'zoom':15,
            'accesstoken': MAPBOX_TOKEN,
            'style': "outdoors",
            "center":{'lat': self.mainLocation['lat'], 'lon': self.mainLocation['lon']}   
            },
        showlegend = False)

        
 
