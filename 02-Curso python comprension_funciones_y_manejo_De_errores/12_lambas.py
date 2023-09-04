'''
def message_creator(text):
   # Escribe tu solución 👇
   if text.lower() == 'computadora':
      return 'Con mi computadora puedo programar usando Python'
   elif text.lower() == 'celular':
      return 'En mi celular puedo aprender usando la app de Platzi'
   elif text.lower() == 'cable':
      return '¡Hay un cable en mi bota!'
   else:
      return 'Artículo no encontrado'
   return 'computadora'



text = 'celular'
response = message_creator(text)
print(response)

'''

# lambda


def increment(x):
    return x+1


def increment_V2(x): return x+1


result = increment(10)
print(result)
result = increment_V2(20)
print(result)


def full_name(
    name, last_name): return f'Full name es {name.title()} {last_name.title()}'


text = full_name('KEVIN', 'CAMPOSECO')
print(text)


def increment_v3(x): return x+2


result = increment_v3(4)
print(result)
