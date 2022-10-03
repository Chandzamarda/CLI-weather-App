#Created by Chandzamarda Caleb Junior 
import requests

#API Details 
API_KEY = "95a14cf1697d8b5fac7bd93a8d917cd3"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#City Query

city = input("Enter a City Name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)
if response.status_code == 200:
	data = response.json()
#weather
	weather = data ["weather"][0]["description"]
	
#temprature

	temperature = round(data ["main"]["temp"] - 273.15, 2)
	
	humidity = data["main"]["humidity"]

	print ("Weather: ", weather)
	print ("Temperature: ", temperature, "Celsius")
	print ("Humidity: ", humidity)
else:
	print ("An error occurred, please try again ")
