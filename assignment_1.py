flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

cities = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def search_flights_by_city(city_code):
    city_flights = [flight for flight in flight_data if flight["From"] == city_code or flight["To"] == city_code]
    if city_flights:
        print(f"Flights involving {cities[city_code]}:")
        print("{:<10} {:<10} {:<10} {:<10}".format("Flight ID", "From", "To", "Price"))
        for flight in city_flights:
            print("{:<10} {:<10} {:<10} {:<10}".format(flight["Flight ID"], cities[flight["From"]], cities[flight["To"]], flight["Price"]))
    else:
        print(f"No flights involving {cities[city_code]} found.")

def search_flights_from_city(city_code):
    city_flights = [flight for flight in flight_data if flight["From"] == city_code]
    if city_flights:
        print(f"Flights from {cities[city_code]}:")
        print("{:<10} {:<10} {:<10} {:<10}".format("Flight ID", "From", "To", "Price"))
        for flight in city_flights:
            print("{:<10} {:<10} {:<10} {:<10}".format(flight["Flight ID"], cities[flight["From"]], cities[flight["To"]], flight["Price"]))
    else:
        print(f"No flights from {cities[city_code]} found.")

def search_flights_between_cities(from_code, to_code):
    city_flights = [flight for flight in flight_data if flight["From"] == from_code and flight["To"] == to_code]
    if city_flights:
        print(f"Flights from {cities[from_code]} to {cities[to_code]}:")
        print("{:<10} {:<10} {:<10} {:<10}".format("Flight ID", "From", "To", "Price"))
        for flight in city_flights:
            print("{:<10} {:<10} {:<10} {:<10}".format(flight["Flight ID"], cities[flight["From"]], cities[flight["To"]], flight["Price"]))
    else:
        print(f"No flights from {cities[from_code]} to {cities[to_code]} found.")

while True:
    print("\nMenu:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        city_code = input("Enter city code (e.g., BLR, BOM, BBI, HYD, JLR): ").upper()
        if city_code in cities:
            search_flights_by_city(city_code)
        else:
            print("Invalid city code. Please try again.")

    elif choice == '2':
        city_code = input("Enter city code (e.g., BLR, BOM, BBI, HYD, JLR): ").upper()
        if city_code in cities:
            search_flights_from_city(city_code)
        else:
            print("Invalid city code. Please try again.")

    elif choice == '3':
        from_code = input("Enter source city code (e.g., BLR, BOM, BBI, HYD, JLR): ").upper()
        to_code = input("Enter destination city code (e.g., BLR, BOM, BBI, HYD, JLR): ").upper()
        if from_code in cities and to_code in cities:
            search_flights_between_cities(from_code, to_code)
        else:
            print("Invalid city codes. Please try again.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
