import requests

def stage_1_2():
    mycoins = float(input("Enter the number of mycoins: "))

    ars_rate = 0.82
    hnl_rate = 0.17
    aud_rate = 1.9622
    mad_rate = 0.208

    ars = round(mycoins * ars_rate, 2)
    hnl = round(mycoins * hnl_rate, 2)
    aud = round(mycoins * aud_rate, 2)
    mad = round(mycoins * mad_rate, 2)

    print(f"I will get {ars} ARS from the sale of {mycoins} mycoins.")
    print(f"I will get {hnl} HNL from the sale of {mycoins} mycoins.")
    print(f"I will get {aud} AUD from the sale of {mycoins} mycoins.")
    print(f"I will get {mad} MAD from the sale of {mycoins} mycoins.")

def stage_3():
    currency_code = input("Enter your currency code (e.g. AUD): ").lower()
    url = f"http://www.floatrates.com/daily/{currency_code}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        usd = data.get('usd')
        eur = data.get('eur')

        if usd:
            print(f"USD: {usd['rate']}")
        else:
            print("USD data not found")

        if eur:
            print(f"EUR: {eur['rate']}")
        else:
            print("EUR data not found")

    except requests.RequestException:
        print("Error: Unable to get data from FloatRates.")

def stage_4():
    cache = {}

    base_currency = input("Enter the base currency code: ").lower()
    url = f"http://www.floatrates.com/daily/{base_currency}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json()
    except requests.RequestException:
        print("Error: Unable to get data from FloatRates.")
        rates = {}

    while True:
        target_currency = input("Enter the currency to convert to (empty to quit): ").lower()
        if not target_currency:
            break

        amount_str = input("Enter the amount to exchange: ")
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount. Try again.")
            continue

        print("Checking the cache...")
        if target_currency in cache:
            print("It is in the cache!")
            rate = cache[target_currency]
        else:
            print("Sorry, but it is not in the cache!")
            if target_currency in rates:
                rate = rates[target_currency]['rate']
                cache[target_currency] = rate
            else:
                print("Currency not found in rates.")
                continue

        exchanged = round(amount * rate, 2)
        print(f"You received {exchanged} {target_currency.upper()}.")

if __name__ == "__main__":
    stage_1_2()
    stage_3()
    stage_4()
