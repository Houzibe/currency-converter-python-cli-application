#-----------------------------------------------------------
# Currency Converter - Python Cli App
#-----------------------------------------------------------
print()
print("****************************************************")
print("      Currency Converter CLI Application  ")
print("****************************************************")
print("Note: This App converts naira to USD, EUR, GBP.")

exchange_rates = {
    "USD" : 0.00074430, 
    "EUR" : 0.00063130, 
    "GBP" : 0.00055154  
    }

def currency_conversion(amount, rate):
    return round(float(amount)*rate,2)

print()
enteredAmount = input("Enter amount(in Naira): ")
print()
print("Conversion Outcome:")
print("----------------------------------------------------")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["USD"])} USD;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["EUR"])} EUR;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["GBP"])} GBP;")
print("----------------------------------------------------")
print("Thank you for using our currency converter today!")
print()