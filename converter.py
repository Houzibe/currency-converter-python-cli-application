# Currency Converter - Python Cli App
exchange_rates = {
    "USD" : 0.00074430,
    "EUR" : 0.00063130,
    "GBP" : 0.00055154
    }
print()
print("****************************************************")
print("      Welcome to Currency Converter Application  ")
print("****************************************************")
print("Note: you can only convert naira to USD, EUR, GBP.")
print()
print("Please select currency for conversion.")
print("1. USD")
print("2. EUR")
print("3. GBP")
print()
choice = input("Enter selection(between 1 to 3): ")
print()
print(f"You choice is {choice}")