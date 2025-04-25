from random import choice
#from data import export_to_csv
from weather_oop import WeatherApp

city = input("Please enter the city: ").strip()
country = input("Please enter the country: ").strip()
weather = WeatherApp(city, country)
# weather.get_coordinates()
# weather.get_weather()
# print(weather.temperatur)
# print(weather.windspeed)

while True:
    print("\n MENU")
    print("1. get coordinates")
    print("2. get current weather")
    print("3. suggest clothing")
    print("4. get weekly forecast")
    print("5  export db to csv")
    print("0. exit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        weather.get_coordinates()
        print(f"latitude: {weather.latitude}, longitude: {weather.longitude}")
    elif choice == "2":
        weather.get_coordinates()
        weather.get_weather()
        print(f"""\nThe weather report in {weather.city},{weather.country} is:
              - temperature:{weather.temperatur}
              - windspeed:{weather.windspeed}""")
    elif choice == "3":
        weather.get_coordinates()
        weather.get_weather()
        weather.suggest_clothing()
    elif choice == "4":
        weather.get_weekly_forecast()
    #elif choice == "5":
    #    export_to_csv()
    elif choice == "0":
        break
    else: print("the input is invalid, please enter a correct option")
