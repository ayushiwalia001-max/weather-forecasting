import requests
from pycountry import countries # contains countrycode 

url = "https://geocoding-api.open-meteo.com/v1/search"

try:
    country = input("Enter country name: ")
    city = input("Enter city name: ")

    country_code = countries.lookup(country).alpha_2  # lookup() returns country object, and alpha_2 returns country code

    # Query parameter
    query_params = {
        "name": city,   #name - api parameter
        "countryCode": country_code # countrycode api parameter
    }

    def get_location(response):
        data = response.json()
        if not data["results"]:
            print("⚠️ Please enter a valid city name.")

        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        return latitude, longitude







    response = requests.get(url, params=query_params)


    if response.status_code == 200:
        # JSON data read/process
        latitude, longitude = get_location(response)
        

    elif response.status_code == 400:
        print("Bad Request: The request was invalid.")

    elif response.status_code == 401:
        # Unauthorized
        print("Unauthorized: Authentication is required.")

    elif response.status_code == 403:
        # Forbidden
        print("Forbidden: Access to the resource is denied.")


    elif response.status_code == 404:
        # Not found
        print("Not Found: The requested resource was not found.")


    elif response.status_code == 405:
        # Method not allowed
        print("Method Not Allowed: The HTTP method is not allowed.")
    else:
        # Some unexpected status code
        print("Unexpected status code:", response.status_code)



    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
        "temperature_unit": "celsius"
    }

    weather_response = requests.get(weather_url, params=weather_params)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        # print(weather_data)
        # print(weather_data.keys())
        temp =  weather_data["current"]["temperature_2m"]
        print(f"""
    ╔══════════════════════════════════════════╗
    ║             🌤️ WEATHER REPORT             ║
    ╠══════════════════════════════════════════╣
    ║  🌍  Country     : {country}                 ║
    ║  📍  City        : {city}                 ║
    ║  🌡️  Temperature : {temp} °C                ║
    ╚══════════════════════════════════════════╝
    """)



    elif weather_response.status_code == 400:
        print("Bad Request: The request was invalid.")

    elif weather_response.status_code == 401:
        print("Unauthorized: Authentication is required.")

    elif weather_response.status_code == 403:
        print("Forbidden: Access to the resource is denied.")

    elif weather_response.status_code == 404:
        print("Not Found: The requested resource was not found.")

    elif weather_response.status_code == 405:
        print("Method Not Allowed: The HTTP method is not allowed.")

    else:
        print("Unexpected status code:", weather_response.status_code)

except:
    print(f"⚠️ Please enter a valid country name.")        