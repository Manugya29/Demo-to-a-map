import folium
map = folium.Map(location=[22.49,88.22], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="my Map")
for coordinates in [[22.49,87.22],[81.49,87.22]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi i am Manugya Dastidar",icon=folium.Icon(color="red")))
map.add_child(fg)



map.save("Manugya.html")
