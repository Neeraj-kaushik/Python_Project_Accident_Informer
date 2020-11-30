"""Using this we can easily get the location by using ip address and mark
it and this info will be helpful to police and user to find the loaction where 
the accident actualy occure"""

import requests
import folium

"""This will import data from website of out cordinates for location"""

res=requests.get('https://ipinfo.io/')
data=res.json()
location=data['loc'].split(',')
lat=float(location[0])
log=float(location[1])

"""These two chid of folium will be used to mark our country like 
India and the exact location in India using Ip Address"""

fg=folium.FeatureGroup('my map')

fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup='this is my location'))

map=folium.Map(location=[lat,log],zoom_start=7)
map.add_child(fg)

"""This will save it into html file whch will be easily accesible to everyone"""

map.save("1.html")