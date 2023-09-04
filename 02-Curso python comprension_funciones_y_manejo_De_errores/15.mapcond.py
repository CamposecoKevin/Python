items = [
    {
        'producto': 'camisa',
        'price': 200
    },
    {
        'producto': 'pantalon',
        'price': 300
    },
    {
        'producto': 'patalon 3',
        'price': 100
    }
]


price = list(map(lambda item: item['price'], items))
print(items)
print(price)


# agregar una nuev list llamada impuestos

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price']*.19
    return new_item


new_items = list(map(add_taxes, items))
print("new lista")
print(new_items)
print("Old list")
print(items)
