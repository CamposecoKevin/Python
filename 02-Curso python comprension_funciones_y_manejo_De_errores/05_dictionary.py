'''
dict = {}
for i in range(1, 11):
    dict[i] = i * 2
print(dict)


dict_V2 = {i: i * 2 for i in range(1, 11)}
print(dict_V2)
'''
import random
countries = {"col", "mex", "bol", "per", "gt"}
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)


population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)


# unir dos listas

name = {"Kevin", "Rubeli", "Harli"}
year = {12, 56, 98}

print(list(zip(name, year)))


new_dict = {name: year for (name, year) in zip(name, year)}
