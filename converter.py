#-----------------------------------------------------------
# Currency Converter - Python Cli App
#-----------------------------------------------------------
print()
print("****************************************************")
print("      Currency Converter CLI Application  ")
print("****************************************************")
print("Note: This App converts naira to USD, EUR, GBP, XAF, GHS")

exchange_rates = {
    "USD" : 0.00073862, 
    "EUR" : 0.00062565, 
    "GBP" : 0.00054549,
    "XAF" : 0.41040250,
    "GHS" : 0.00786432  
    }

def currency_conversion(amount, rate):
    """This function convert amount in Naira into a different currency using defined rate """
    return round(float(amount)*rate,2)

print()
enteredAmount = input("Enter amount(in Naira): ")
print()
print("Conversion Outcome:")
print("----------------------------------------------------")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["USD"])} USD;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["EUR"])} EUR;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["GBP"])} GBP;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["XAF"])} XAF;")
print(f"{enteredAmount} Naira is {currency_conversion(enteredAmount,exchange_rates["GHS"])} GHS;")
print("----------------------------------------------------")
print("Thank you for using our currency converter today!")
print()