import pandas
import folium

def d_frame(df):
    locations=list(zip(df.Latitude,df.Longitude,df.Name))

    map=folium.Map(location=(43.214, 27.91), zoom_start=10, tiles="Stamen Terrain")

    fg_loc=folium.FeatureGroup(name='My Map')

    for lat,lon,name in locations:
        fg_loc.add_child(folium.Marker(location=(lat,lon),popup=str(name),icon=folium.Icon(color="green",icon="fas fa-map-marker-alt")))

    map.add_child(fg_loc)
    map.add_child(folium.LayerControl(collapsed=True,))
    return map._repr_html_()

