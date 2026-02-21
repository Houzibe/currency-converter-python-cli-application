#-----------------------------------------------------------
# Currency Converter - Python Cli App
#-----------------------------------------------------------
print()
print("****************************************************")
print("      Welcome to Currency Converter Application  ")
print("****************************************************")
print("Note: This App converts naira to USD, EUR, GBP.")

exchange_rates = {
    "USD" : 0.00074430, 
    "EUR" : 0.00063130, 
    "GBP" : 0.00055154  
    }

def currency_conversion(amount, rate):
    return round(amount*rate,2)

print()
enteredAmount = float(input("Enter amount(in Naira): "))
print("Conversion Outcome:")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["USD"])} USD;")


print()
print("****************************************************")