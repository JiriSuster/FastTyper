import json

file = open("orders.json", "r")

json_file = json.load(file)
dict_orders = {}

for order in json_file:
    price = order["Quantity"] * order["Product Price"]
    if order["Order Number"] in dict_orders:
        dict_orders[order["Order Number"]].append(price)
    else:
        dict_orders[order["Order Number"]] = [price]

for key, prices_list in dict_orders.items():
    avg_price = sum(prices_list)/len(prices_list)
    print(f"objednavka cislo: {key} ma prumerno cenu: {avg_price}")


from datetime import datetime
dict_month = {}

for order in json_file:
    if order["Item Name"] == "Mango Chutney":
        key = datetime.strptime(order["Order Date"], "%d/%m/%Y %H:%M").strftime("%B")
        if key in dict_month.keys():
            dict_month[key] += order["Quantity"]
        else:
            dict_month[key] = order["Quantity"]


for month, quantity in dict_month.items():
    print(f"{month} se prodalo {quantity} Mango Chutney")