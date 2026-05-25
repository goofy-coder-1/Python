# ==============================================================================
#  THE LIVE WEATHER DASHBOARD CLI ENGINE
# ==============================================================================
import requests

# Static coordinate mapper dictionary database
city_catalog = {
    # --- South Asia & East Asia ---
    "KATHMANDU":   {"lat": 27.7172, "lon": 85.3240,  "country": "Nepal"},
    "POKHARA":     {"lat": 28.2096, "lon": 83.9856,  "country": "Nepal"},
    "NEW DELHI":   {"lat": 28.6139, "lon": 77.2090,  "country": "India"},
    "MUMBAI":      {"lat": 19.0760, "lon": 72.8777,  "country": "India"},
    "TOKYO":       {"lat": 35.6762, "lon": 139.6503, "country": "Japan"},
    "BEIJING":     {"lat": 39.9042, "lon": 116.4074, "country": "China"},
    "SEOUL":       {"lat": 37.5665, "lon": 126.9780, "country": "South Korea"},
    "BANGKOK":     {"lat": 13.7563, "lon": 100.5018, "country": "Thailand"},

    # --- Europe ---
    "LONDON":      {"lat": 51.5074, "lon": -0.1278,  "country": "UK"},
    "BERLIN":      {"lat": 52.5200, "lon": 13.4050,  "country": "Germany"},
    "PARIS":       {"lat": 48.8566, "lon": 2.3522,   "country": "France"},
    "ROME":        {"lat": 41.9028, "lon": 12.4964,  "country": "Italy"},
    "MADRID":      {"lat": 40.4168, "lon": -3.7038,  "country": "Spain"},
    "MOSCOW":      {"lat": 55.7558, "lon": 37.6173,  "country": "Russia"},

    # --- Americas ---
    "NEW YORK":    {"lat": 40.7128, "lon": -74.0060,  "country": "USA"},
    "LOS ANGELES": {"lat": 34.0522, "lon": -118.2437, "country": "USA"},
    "TORONTO":     {"lat": 43.6532, "lon": -79.3832,  "country": "Canada"},
    "MEXICO CITY": {"lat": 19.4326, "lon": -99.1332,  "country": "Mexico"},
    "SAO PAULO":   {"lat": -23.5505, "lon": -46.6333, "country": "Brazil"},
    "BUENOS AIRES":{"lat": -34.6037, "lon": -58.3816, "country": "Argentina"},

    # --- Middle East & Africa ---
    "DUBAI":       {"lat": 25.2048, "lon": 55.2708,  "country": "UAE"},
    "CAIRO":       {"lat": 30.0444, "lon": 31.2357,  "country": "Egypt"},
    "CAPE TOWN":   {"lat": -33.9249, "lon": 18.4241,  "country": "South Africa"},

    # --- Oceania ---
    "SYDNEY":      {"lat": -33.8688, "lon": 151.2093, "country": "Australia"},
    "AUCKLAND":    {"lat": -36.8485, "lon": 174.7633, "country": "New Zealand"}
}

while True:
    print("\n====================================")
    print("      LIVE METEO WEATHER ENGINE      ")
    print("=====================================")
    print("Available Cities:")
    for city, info in city_catalog.items():
        print(f"  • {city.title()} ({info['country']})")
    print("-------------------------------------")
    print("[G] Fetch Live Weather | [E] Exit Engine")
    print("=====================================")

    choice = input("Enter Operation to perform: ").upper().strip()

    match choice:
        case 'G':
            city = input("Enter name of city: ").upper().strip()
            if city not in city_catalog:
                print("City not found in our index")
                continue

            lat = city_catalog[city]["lat"]
            lon = city_catalog[city]["lon"]

            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
            print(f"\n Fetching tempreature of {city.title()}...")

            try:
                # Fire an HTTP GET request across the internet stream
                response = requests.get(api_url, timeout=5)

                response.raise_for_status()
                weather_data = response.json()

                current_temp = weather_data["current"]["temperature_2m"]
                wind_speed = weather_data["current"]["wind_speed_10m"]
                temp_unit = weather_data["current_units"]["temperature_2m"]
                wind_unit = weather_data["current_units"]["wind_speed_10m"]

                print("\n --- LIVE WEATHER REPORT --- ")
                print(f"City:        {city.title()}")
                print(f"Temperature: {current_temp}{temp_unit}")
                print(f"Wind Speed:  {wind_speed} {wind_unit}")
                print("--------------------------------")

            except requests.exceptions.ConnectionError:
                print("Could not connect to the server, check your internet connection")
            except requests.exceptions.Timeout:
                print("Server took long to fetch data")
            except requests.exceptions.HTTPError as http_err:
                print(f"Server responded with bad status {http_err}")
            except Exception as e:
                print(f" Unexpected Engine Exception: {e}")

        case 'E':
            print("Shutting down the program")
        case _:
            print("Invalid Command")