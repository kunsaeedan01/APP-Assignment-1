from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
data = cg.get_global()

print(data)
top_100 = sorted(data["total_market_cap"])
list_of_crypto = []

for key in top_100:
    list_of_crypto.append(key)


def crypto_list():
    user_input = int(input("Print the number of cryptocurrencies for output:  "))
    order = 1
    if user_input > len(list_of_crypto) or user_input < 1:
        print("Your number is out of range")
    else:
        for coin in range(0, user_input):
            print(f"{order}. {list_of_crypto[coin]}")
            order += 1
