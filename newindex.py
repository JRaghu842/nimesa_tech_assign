# corrected pyhton code should be written here


import requests

# Creating function to fetch weather data from the API
def fetch_weather_data():
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

# Creating function to get temperature
def get_temperature(data, date_time):
    for entry in data["list"]:
        if entry["dt_txt"] == date_time:
            return entry["main"]["temp"]
    return None

# Creating function to get wind speed
def get_wind_speed(data, date_time):
    for entry in data["list"]:
        if entry["dt_txt"] == date_time:
            return entry["wind"]["speed"]
    return None

# Creating function to get pressure
def get_pressure(data, date_time):
    for entry in data["list"]:
        if entry["dt_txt"] == date_time:
            return entry["main"]["pressure"]
    return None

# Creating function weather data from the API
weather_data = fetch_weather_data()

if weather_data:
    while True:
        print("Options:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Choose an option: ")

        if option == "1":
            date_time = input("Enter date and time (e.g., 2019-03-27 18:00:00): ")
            temperature = get_temperature(weather_data, date_time)
            if temperature is not None:
                print(f"Temperature at {date_time}: {temperature} K")
            else:
                print("Data not found for the given date and time.")
        elif option == "2":
            date_time = input("Enter date and time (e.g., 2019-03-27 18:00:00): ")
            wind_speed = get_wind_speed(weather_data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {date_time}: {wind_speed} m/s")
            else:
                print("Data not found for the given date and time.")
        elif option == "3":
            date_time = input("Enter date and time (e.g., 2019-03-27 18:00:00): ")
            pressure = get_pressure(weather_data, date_time)
            if pressure is not None:
                print(f"Pressure at {date_time}: {pressure} hPa")
            else:
                print("Data not found for the given date and time.")
        elif option == "0":
            break
        else:
            print("Invalid option. Please choose a valid option.")

