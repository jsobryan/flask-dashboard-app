import requests, json, pytemperature
  
# Enter your API key here 
api_key = "656c8b0ea425b209ee862429cf03acfb"
  
# base_url variable to store url 
url = "http://api.openweathermap.org/data/2.5/weather?appid=656c8b0ea425b209ee862429cf03acfb&q=temple"
  
# get method of requests module 
# return response object 
response = requests.get(url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
y = x["main"] 
  
# store the value corresponding 
# to the "temp" key of y 
current_temperature = y["temp"] 

#convert to fahrenheit
ftemp = pytemperature.k2f(current_temperature)
temp = round(ftemp)

# print following values 
# print(" It is currently " + str(temp))