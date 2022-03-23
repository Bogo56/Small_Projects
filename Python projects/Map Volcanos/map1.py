import folium
import pandas

df=pandas.read_csv("Volcanoes.txt")
volcanoes=list(zip(df.LAT,df.LON,df.NAME,df.ELEV))

def color_picker(n):
    if n<=1000:
        return "green"
    elif n>1000 and n<=2200:
        return "orange"
    elif n>2200:
        return "red"


map=folium.Map(location=(43.214, 27.91),zoom_start=10,tiles="Stamen Terrain")

fg_volc=folium.FeatureGroup(name='My Map')

for a,b,c,d in volcanoes:
    fg_volc.add_child(folium.Marker(location=(a,b),popup=str(c),icon=folium.Icon(color=color_picker(d),icon="fas fa-map-marker-alt")))

fg_color=folium.FeatureGroup(name='Population')

fg_color.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function= lambda x:{"fillColor":"yellow"}))


map.add_child(fg_color)
map.add_child(fg_volc)
map.add_child(folium.LayerControl(collapsed=True,))
map.save("Map1.html")