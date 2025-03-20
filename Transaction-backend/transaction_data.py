import requests
from datetime import datetime, timedelta
import random


def _get_data_from_api():
    url = "https://my.api.mockaroo.com/fin2.json"
    headers = {"X-API-Key": "11fef030"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")

    data = response.json()
    return data


def _get_data():
    return [
        {
            "transaction_id": 45,
            "description": "Womens Ready To Wear Stores",
            "name": "Topiczoom",
            "type": "debit",
            "amount": 144,
            "date": "2024-11-22",
        },
        {
            "transaction_id": 44,
            "description": "Candy/Nut/Confection Stores",
            "name": "Buzzdog",
            "type": "debit",
            "amount": 84,
            "date": "2024-11-21",
        },
        {
            "transaction_id": 43,
            "description": "Grocery Stores/Supermarkets",
            "name": "Realcube",
            "type": "debit",
            "amount": 672,
            "date": "2024-11-21",
        },
        {
            "transaction_id": 42,
            "description": "Movies",
            "name": "Ozu",
            "type": "debit",
            "amount": 600,
            "date": "2024-11-21",
        },
        {
            "transaction_id": 41,
            "description": "Optometrists/Ophthalmologists",
            "name": "Meejo",
            "type": "debit",
            "amount": 659,
            "date": "2024-11-20",
        },
        {
            "transaction_id": 40,
            "description": "Piece Goods/Notions/Dry Good",
            "name": "Voonix",
            "type": "debit",
            "amount": 40,
            "date": "2024-11-18",
        },
        {
            "transaction_id": 39,
            "description": "Bowling Alleys",
            "name": "Eadel",
            "type": "debit",
            "amount": 693,
            "date": "2024-11-18",
        },
        {
            "transaction_id": 38,
            "description": "Freezer/Meat Lockers",
            "name": "Ainyx",
            "type": "debit",
            "amount": 80,
            "date": "2024-11-16",
        },
        {
            "transaction_id": 37,
            "description": "Pet Stores/food & Supply",
            "name": "Twitterbridge",
            "type": "debit",
            "amount": 658,
            "date": "2024-11-16",
        },
        {
            "transaction_id": 36,
            "description": "Fast Food Restaurants",
            "name": "Meezzy",
            "type": "debit",
            "amount": 219,
            "date": "2024-11-15",
        },
        {
            "transaction_id": 35,
            "description": "Grocery Stores/Supermarkets",
            "name": "BlogXS",
            "type": "debit",
            "amount": 425,
            "date": "2024-11-13",
        },
        {
            "transaction_id": 34,
            "description": "Fast Food Restaurants",
            "name": "Fiveclub",
            "type": "debit",
            "amount": 164,
            "date": "2024-11-11",
        },
        {
            "transaction_id": 33,
            "description": "Fast Food Restaurants",
            "name": "Divavu",
            "type": "debit",
            "amount": 469,
            "date": "2024-11-11",
        },
        {
            "transaction_id": 32,
            "description": "Grocery Stores/Supermarkets",
            "name": "Realcube",
            "type": "debit",
            "amount": 387,
            "date": "2024-11-10",
        },
        {
            "transaction_id": 31,
            "description": "Misc Home Furnishing Specialty",
            "name": "Bubbletube",
            "type": "debit",
            "amount": 658,
            "date": "2024-11-10",
        },
        {
            "transaction_id": 30,
            "description": "Shoe Stores",
            "name": "Buzzdog",
            "type": "debit",
            "amount": 92,
            "date": "2024-11-10",
        },
        {
            "transaction_id": 29,
            "description": "Florists",
            "name": "Vinte",
            "type": "debit",
            "amount": 58,
            "date": "2024-11-09",
        },
        {
            "transaction_id": 28,
            "description": "Digital Goods: Games",
            "name": "Dablist",
            "type": "debit",
            "amount": 276,
            "date": "2024-11-09",
        },
        {
            "transaction_id": 27,
            "description": "Hospitals",
            "name": "Eayo",
            "type": "debit",
            "amount": 223,
            "date": "2024-11-08",
        },
        {
            "transaction_id": 26,
            "description": "Doctors & Physicians",
            "name": "Realcube",
            "type": "debit",
            "amount": 519,
            "date": "2024-11-08",
        },
        {
            "transaction_id": 25,
            "description": "'Electrical Parts/Equipment",
            "name": "Jaxspan",
            "type": "debit",
            "amount": 577,
            "date": "2024-11-08",
        },
        {
            "transaction_id": 24,
            "description": "Hospitals",
            "name": "Twinder",
            "type": "debit",
            "amount": 498,
            "date": "2024-11-08",
        },
        {
            "transaction_id": 23,
            "description": "Amusement Parks/Circus",
            "name": "Quamba",
            "type": "debit",
            "amount": 599,
            "date": "2024-11-07",
        },
        {
            "transaction_id": 22,
            "description": "Bars/Taverns/Lounges/Discos",
            "name": "Realblab",
            "type": "debit",
            "amount": 467,
            "date": "2024-11-05",
        },
        {
            "transaction_id": 21,
            "description": "Book Stores",
            "name": "Oodoo",
            "type": "debit",
            "amount": 59,
            "date": "2024-11-03",
        },
        {
            "transaction_id": 20,
            "description": "Restaurants",
            "name": "Trupe",
            "type": "debit",
            "amount": 576,
            "date": "2024-11-02",
        },
        {
            "transaction_id": 19,
            "description": "Misc Home Furnishing Specialty",
            "name": "Voonder",
            "type": "debit",
            "amount": 414,
            "date": "2024-11-02",
        },
        {
            "transaction_id": 18,
            "description": "Stationery Stores",
            "name": "Podcat",
            "type": "debit",
            "amount": 80,
            "date": "2024-11-02",
        },
        {
            "transaction_id": 17,
            "description": "Shoe Stores",
            "name": "Rhyzio",
            "type": "debit",
            "amount": 57,
            "date": "2024-11-02",
        },
        {
            "transaction_id": 16,
            "description": "Bars/Taverns/Lounges/Discos",
            "name": "Dabtype",
            "type": "debit",
            "amount": 626,
            "date": "2024-11-01",
        },
        {
            "transaction_id": 15,
            "description": "Hospitals",
            "name": "Rooxo",
            "type": "debit",
            "amount": 597,
            "date": "2024-11-01",
        },
        {
            "transaction_id": 14,
            "description": "News Dealers/Newsstands",
            "name": "Twitterbeat",
            "type": "debit",
            "amount": 95,
            "date": "2024-10-30",
        },
        {
            "transaction_id": 13,
            "description": "Amusement Parks/Circus",
            "name": "Browsebug",
            "type": "debit",
            "amount": 182,
            "date": "2024-10-30",
        },
        {
            "transaction_id": 12,
            "description": "Book Stores",
            "name": "Kwilith",
            "type": "debit",
            "amount": 99,
            "date": "2024-10-29",
        },
        {
            "transaction_id": 11,
            "description": "Dairy Product Stores",
            "name": "Vipe",
            "type": "debit",
            "amount": 75,
            "date": "2024-10-29",
        },
        {
            "transaction_id": 10,
            "description": "Bakeries",
            "name": "Voonix",
            "type": "debit",
            "amount": 43,
            "date": "2024-10-29",
        },
        {
            "transaction_id": 9,
            "description": "Bakeries",
            "name": "Feedbug",
            "type": "debit",
            "amount": 42,
            "date": "2024-10-29",
        },
        {
            "transaction_id": 8,
            "description": "Camera & Photo Supply Stores",
            "name": "Livepath",
            "type": "debit",
            "amount": 71,
            "date": "2024-10-28",
        },
        {
            "transaction_id": 7,
            "description": "Camera & Photo Supply Stores",
            "name": "Yombu",
            "type": "debit",
            "amount": 54,
            "date": "2024-10-28",
        },
        {
            "transaction_id": 6,
            "description": "Florists",
            "name": "Realpoint",
            "type": "debit",
            "amount": 58,
            "date": "2024-10-28",
        },
        {
            "transaction_id": 5,
            "description": "Misc Apparel/Access Stores",
            "name": "Fliptune",
            "type": "debit",
            "amount": 57,
            "date": "2024-10-27",
        },
        {
            "transaction_id": 4,
            "description": "Household Appliance Stores",
            "name": "Voonix",
            "type": "debit",
            "amount": 113,
            "date": "2024-10-27",
        },
        {
            "transaction_id": 3,
            "description": "Piece Goods/Notions/Dry Good",
            "name": "Divanoodle",
            "type": "debit",
            "amount": 66,
            "date": "2024-10-25",
        },
        {
            "transaction_id": 2,
            "description": "Amusement Parks/Circus",
            "name": "Skipstorm",
            "type": "debit",
            "amount": 496,
            "date": "2024-10-25",
        },
        {
            "transaction_id": 1,
            "description": "Grocery Stores/Supermarkets",
            "name": "Topdrive",
            "type": "debit",
            "amount": 593,
            "date": "2024-10-24",
        },
    ]


def _get_dates_to_insert(no_of_dates, days=30):
    days_ago = sorted(random.choices(list(range(days)), k=no_of_dates))
    all_dates = [
        (datetime.today() - timedelta(days=x)).strftime("%Y-%m-%d") for x in days_ago
    ]

    return all_dates


def _insert_dates(data, dates):
    for elem, date in zip(data, dates):
        elem["date"] = date


def _print_dates(dates):
    print(dates[0])
    for i in range(1, len(dates)):
        if dates[i - 1] != dates[i]:
            print()
        print(dates[i])


# print_dates(dates)


def _print_data(data):
    print(len(data))
    for elem in data:
        print(elem)


def get_transactions_data(*, call_api=True, rows=None):
    data = _get_data_from_api() if call_api else _get_data()
    dates = _get_dates_to_insert(len(data), days=30 if rows is None else rows // 3)
    _insert_dates(data, dates)

    data = data[:rows] if rows is not None else data
    return data[::-1]


if __name__ == "__main__":
    data = get_transactions_data(call_api=True)
    dates = _get_dates_to_insert(len(data))
    _insert_dates(data, dates)

    print(data)

    # _print_dates(dates)
    # print(len(dates))
