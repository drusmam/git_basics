print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

precition = float(input('Введите точность: '))
x = float(input('Введите x: '))
result = 1
countRank = 1 
factorial = 1
summRank = 1

while summRank > precition:
  for i in range(1, countRank * 2 + 1):
    factorial *= i
  summRank = x ** (2*countRank) / factorial
  if countRank % 2 != 0:
    result -= summRank
  else:
    result += summRank
  factorial = 1
  countRank += 1  

print('Сумма ряда = ', result)
