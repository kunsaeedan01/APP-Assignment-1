import requests

response = requests.get(url="https://api.coingecko.com/api/v3/global")
data = response.json()
top_100 = sorted(data["data"]["total_market_cap"])
list_of_crypto = []

for key in top_100:
    list_of_crypto.append(key)

order = 1
user_input = int(input("Print the number of cryptocurrencies for output:  "))

if user_input > len(list_of_crypto) or user_input < 1:
    print("Your number is out of range")
else:
    for coin in range(0, user_input):
        print(f"{order}. {list_of_crypto[coin]}")
        order += 1


