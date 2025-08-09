import geocoder
g = geocoder.ip('me')

print("City:", g.city)
print("Country:", g.country)
print("Latitude:", g.latlng[0])
print("Longitude:", g.latlng[1])