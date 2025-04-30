from random import choice
from weather_oop import WeatherApp
from data import create_table, export_to_csv

# Initialize database table
create_table()


def get_city():
    """Prompt user for city and country and return a WeatherApp instance."""
    city = input("Please enter the city: ").strip()
    country = input("Please enter the country: ").strip()
    return WeatherApp(city, country)


def menu():
    weather = get_city()  # Getting initial city

    while True:
        print("\n MENU")
        print("1. Get coordinates")
        print("2. Get current weather")
        print("3. Suggest clothing")
        print("4. Get weekly forecast")
        print("5. Export database to CSV")
        print("6. Choose another city")
        print("0. Exit")

        choice = input("Choose an option (0-6): ").strip()

        try:
            if choice == "1":
                weather.get_coordinates()
                print(f"Latitude: {weather.latitude}, Longitude: {weather.longitude}")

            elif choice == "2":
                weather.get_coordinates()
                weather.get_weather()
                print(f"""\nThe weather report in {weather.city}, {weather.country} is:
                      - Temperature: {weather.temperatur}
                      - Wind speed: {weather.windspeed}""")

            elif choice == "3":
                weather.get_coordinates()
                weather.get_weather()
                weather.suggest_clothing()

            elif choice == "4":
                num = int(input("Please enter the number of days: "))
                weather.get_coordinates()
                weather.get_weekly_forecast(num)  # Uncomment when implemented

            elif choice == "5":
                export_to_csv()
                print("Data exported to CSV successfully!")

            elif choice == "6":
                weather = get_city()  # Update the weather variable with new city

            elif choice == "0":
                print("Thank you for using the Weather App. Goodbye!")
                break

            else:
                print("Invalid input. Please enter a number between 0-6.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    menu()