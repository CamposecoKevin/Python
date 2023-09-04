
import random
countries = {"col", "mex", "bol", "per", "gt"}
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)


resultado = {country: population for (
    country, population) in population.items() if population > 20}
print(resultado)


text = 'Hola, soy Kevin'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)
