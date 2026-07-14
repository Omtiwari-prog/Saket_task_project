import requests
#Reuest pythnon libarary to send HTTP requests


city="Mumbai"
api_key="49c61f1e2ee620b769d0e876ff23dbff"



#API url
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#send request - To server
response = requests.get(url)

# convert the response to JSON format
data = response.json()
print(data)
# '''
# eg 
# {
#     "name":"Mumbai",
#     "main":{
#         "temp":28.8,
#         "humidity":83
#     }
# }

# '''

# Display Data 
print("==" * 40)
#print 80 equal signs
print("weather report")
print("=" * 40)


print("city:",data["name"])
print("Temperature:",data["main"]["temp"],"c")
print("Humidity:",data["main"]["humidity"],"%")
print("Weather:",data["weather"][0]["main"])
print("Description:",data["weather"][0]["description"])








