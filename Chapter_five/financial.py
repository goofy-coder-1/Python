# ==============================================================================
#                           F I N A N C E
# ==============================================================================
import requests

while True:
    print("\n----------------------------------")
    print("------ Currency Converter ---------")
    print("----------------------------------")
    print("[G] to convert | [E] to exit program")
    choice = input("Enter operation to perform: ").upper().strip()

    api_url = "https://open.er-api.com/v6/latest/USD"
    
    match choice:
        case 'G':
            # Collect user parameters ONLY when they actively choose to convert
            try:
                dollar = float(input("\nEnter amount in dollars ($): "))
                
                print("\nSupported: [INR] Indian | [NPR] Nepali | [EUR] Euro | [AUD] Australian")
                targeted_currency = input("Enter targeted currency code: ").upper().strip()

                print(f" Fetching live exchange sheets from API stream...")
                response = requests.get(api_url, timeout=5)
                response.raise_for_status()
                
                finance_data = response.json()
                
                # Verify if the currency code actually exists in the API's rate database
                if targeted_currency not in finance_data['rates']:
                    print(f"[-] Validation Error: Currency code '{targeted_currency}' unmapped in rate sheets.")
                    continue
                    
                rate = finance_data['rates'][targeted_currency]
                total = dollar * rate
                
                print("\n --- CONVERSION COMPLETED ---")
                print(f"Base Amount:     ${dollar:.2f} USD")
                print(f"Exchange Rate:   1 USD = {rate:.4f} {targeted_currency}")
                print(f"Final Balance:   {total:.2f} {targeted_currency}")
                print("--------------------------------")

            except ValueError:
                print("[-] Data Type Error: Dollar value must register as a valid decimal number.")
            except requests.exceptions.ConnectionError:
                print("[-] Network Error: Could not connect to the server. Check your internet link.")
            except requests.exceptions.Timeout:
                print("[-] Timeout Error: The remote exchange server took too long to respond.")
            except requests.exceptions.HTTPError as http_err:
                print(f"[-] HTTP Protocol Error: Bad status response ({http_err}).")
            except Exception as e:
                print(f"[-] Unexpected Engine Exception: {e}")
        
        case 'E':
            print("\nShutting down conversion engine metrics. Goodbye!")
            break
            
        case _:
            print("[-] Error: Operation identifier reference unmapped.")