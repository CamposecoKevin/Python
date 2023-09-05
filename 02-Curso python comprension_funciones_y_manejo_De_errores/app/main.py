import mod

keys, values = mod.get_population()
print(keys, values)


data = [
    {
        'Country': 'Guatemala',
        'Population': 300
    },
    {
        'Country': 'USA',
        'Population': 200
    }
]

country = input('Typo country = >')
result = mod.population_by_country(data, country)
print(result)
