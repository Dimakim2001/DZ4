
# Вычислить число c заданной точностью d

# import math
# from math import pi

# n = pi
# print(n)

# n = 100
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(my_pi)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import math

# def is_prime(n):
#     primes = [2]
#     for num in range(3, n + 1, 2):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
#             primes.append(num)
#     return primes

# def get_prime_factors(n, primes):
#     fact = []
#     for i in primes:
#         while n % i == 0:
#             n = n / i
#             fact.append(i)
#     return fact

# n = int(input('Введите число: '))

# primes = is_prime(n)
# factors = get_prime_factors(n, primes)
# print(factors)

# def testing(n, factors):
#     return math.prod(factors) == n       

# print(testing(n, factors))

# def task31 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)

# print (task31 (5))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint

# def create_list(size, m, n):
#     return [randint(m, n) for i in range(size)]

# def get_unic_value(list):
#     return [i for i in set(list)]

# size = 10
# m = 1
# n = 10

# origin = create_list(size, m, n)
# print(origin)
# print(get_unic_value(origin))


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)


# # Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('33_Polynomial2.txt', 'w') as data:
#     data.write(polynom2)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# def prepare(s:str):
#     result = {}
#     temp = ''
#     for ch in s:
#         if (ch != '-' and ch != '+'):
#             temp = temp + ch
#         else:

#             if len(temp) > 1:

#                 elements = temp.split('*')
#                 result[elements[1]] = int(elements[0])
#             temp = ch
#     result['const'] = int(temp)
#     return result

# def sumPolinoms(d1, d2):
#     temp_dict = d2
#     result = {}
#     if len(d1) >= len(d2):
#         temp_dict = d1

#     for key in temp_dict.keys():
#         result[key] = d1.get(key,0) + d2.get(key,0)

#         return result

# s1 = '-3*x^3-4*x^2+55*x+10'
# s2 = '4*x^3+2*x^2-5*x-30'

# s1_dict = prepare(s1)
# s2_dict = prepare(s2)

# result = sumPolinoms(s1_dict, s2_dict)

# res=''
# for key, item in result.items():
#     if key != 'const':
#         res = res + (str(item) if item < 0 else "+" + str(item)) + '*' + key
#     else:
#         res = res + str(item)

# print(res)





