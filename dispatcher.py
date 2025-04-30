def menu():
    if not setup():
        print("Error setting up the application. Exiting.")
        sys.exit(1)

    display_header()
    weather = get_city()

    def switch_city():
        nonlocal weather
        weather = get_city()

    dispatcher = {
        "1": lambda: handle_coordinates(weather),
        "2": lambda: handle_weather(weather),
        "3": lambda: handle_clothing_suggestion(weather),
        "4": lambda: handle_forecast(weather),
        "5": handle_export,
        "6": handle_recent_history,
        "7": switch_city,
        "0": lambda: print("\nThank you for using the Weather App. Goodbye!")
    }

    while True:
        display_menu()
        choice = input("Enter your choice (0-7): ").strip()

        try:
            action = dispatcher.get(choice)
            if action:
                action()
                if choice == "0":
                    break
            else:
                print("Invalid input. Please enter a number between 0-7.")
        except Exception as error:
            print(f"An error occurred: {error}")

        input("\nPress Enter to continue...")
        display_header()