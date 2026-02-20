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
choice = int(input("Enter selection(between 1 to 3): "))
print()

if choice == 1:
    print("You want to convert Naira to USD")
    print(f"The exchange rate is {exchange_rates['USD']}")
elif choice == 2:
    print("You want to convert Naira to EUR")
    print(f"The exchange rate is {exchange_rates['EUR']}")
elif choice == 3:
    print("You want to convert Naira to GBP")
    print(f"The exchange rate is {exchange_rates['GBP']}")
else:
    print("Sorry, you enter a wrong option. Try again...")
    choice = int(input("Enter selection(between 1 to 3): "))