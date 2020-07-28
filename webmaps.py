import folium
import pandas 

data = pandas.read_csv("places.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["name"])
elev=list(data["elev"])

def colour_change(ele):
	if ele<200:
		return'red'
	elif ele<500:
		return'blue'
	else:
		return'green'
		

map=folium.Map(location=[19.06,72.89],zoom_start=6,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Locations")

for lt,ln,na,el in zip(lat,lon,name,elev):
	fgv.add_child(folium.Marker(location=[lt,ln], popup=na+" , "+str(el), icon=folium.Icon(color=colour_change(el))))

fgp=folium.FeatureGroup(name="population")
	
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")