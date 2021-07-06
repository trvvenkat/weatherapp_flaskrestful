import requests


def get_code(city, api_key):
    base_address = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    search_query = "?apikey=" + api_key + "&q=" + city
    address = base_address + search_query
    data = requests.get(address).json()

    if type(data) is dict:
        return False
    else:
        city_code = data[0]['Key']
        return city_code


def get_weather(city_code, api_key):
    base_address = "http://dataservice.accuweather.com/currentconditions/v1/"
    search_query = city_code + "?apikey=" + api_key + "&details=true"
    address = base_address + search_query
    data = requests.get(address).json()

    return data[0]
