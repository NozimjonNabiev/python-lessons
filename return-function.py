# 20-dars: QIYMAT QAYTARUVCHI FUNKSIYA
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev



# def oraliq(min,max,qadam=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# son = oraliq(10,20,2)
# print(son)

# def info(ism, familiya, t_yili, t_joyi, email_manzili='',tel_raqam=None):
#     """Foydalanuvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#     email manaili va telefon raqamini qabul qilib, 
#     lug'at ko'rinishida qaytaruvchi funksiya """
    
#     mijoz = {
#         "ismi":ism,
#         "familiyasi":familiya,
#         "tugilgan yili":t_yili,
#         "tugilgan joyi":t_joyi,
#         "email manzili":email_manzili,
#         "telefon raqami":tel_raqam
#         }
#     return mijoz

# ism = input("Ismingizni kiriting:\n>>> ")
# familiya =input("Familiyangizni kiriting:\n>>> ")
# t_yili = int(input("Tug'ilgan yilingizni kiriting\n>>> "))
# t_joyi = input("Tug'ilgan joyingizni kiriting\n>>> ")
# email_manzili = input("Emai manzilingizni kiriting(ixtiyoriy):\n>>> ")
# tel_raqam = input("telefon raqamingizni kiriting(ixtiyoriy):\n>>> ")

# mijoz = info(ism, familiya, t_yili, t_joyi, email_manzili,tel_raqam)
# print(mijoz)





# def info(ism, familiya, t_yili, t_joyi, email_manzili='',tel_raqam=None):
#     """Foydalanuvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#     email manaili va telefon raqamini qabul qilib, 
#     lug'at ko'rinishida qaytaruvchi funksiya """
    
#     mijoz = {
#         "ismi":ism,
#         "familiyasi":familiya,
#         "tugilgan yili":t_yili,
#         "tugilgan joyi":t_joyi,
#         "email manzili":email_manzili,
#         "telefon raqami":tel_raqam
#         }
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting: ")
# mijozlar =[]
# while True: 
#     ism = input("Ismi:\n>>> ")
#     familiya =input("Familiyasi:\n>>> ")
#     t_yili = int(input("Tug'ilgan yili:\n>>> "))
#     t_joyi = input("Tug'ilgan joyi:\n>>> ")
#     email_manzili = input("Email manzili(ixtiyoriy):\n>>> ")
#     tel_raqam = input("Telefon raqami(ixtiyoriy):\n>>> ")

#     mijozlar.append(info(ism, familiya, t_yili, t_joyi, email_manzili,tel_raqam))
#     javob = input("Davom ettirishni xohlaysizmi?(ha/yo'q)\n>>> ")
#     if javob != 'ha':
#         break
# print("Mijozlar: ")
# for mijoz in mijozlar:
#     print(f"{mijoz['ismi'].title()} {mijoz['familiyasi'].title()} {mijoz['tugilgan yili']}-yilda {mijoz['tugilgan joyi']}da tug'ilgan"
#           f" Email manzili: {mijoz['email manzili']} Telefon raqami: {mijoz['telefon raqami']}")






# def eng_katta(son1, son2, son3):
#     """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
#     # if son1>son2 and son1>son3:
#     #     return son1
#     # elif son2>son1 and son2>son3:
#     #     return son2 
#     # elif son3>son1 and son3>son2:
#     #     return son3 
#     # else:
#     #     return "Sonlar teng!"
#     sonlar = [son1, son2, son3]
#     katta_son = 0
#     for son in sonlar:
#          if son > katta_son:
#             katta_son = son
#     return katta_son
        


# print("\n3 ta son kiriting eng kattasini chiqarib beraman:")
# son1 = float(input("1-son: "))
# son2 = float(input("2-son: "))
# son3 = float(input("3-son: "))

# max_son= eng_katta(son1, son2, son3)
# print(f"\n{max_son}")





# def aylana(radius):
#     """Foydalanuvchidan aylananing radiusini qabul qilib, uning radiusini diametrini 
#     perimetrini va yuzini lug'at ko'rinishida chiqarib beruvchi funksiya """
#     diametr = radius * 2
#     PI = 3.14
#     perimetr = 2 * PI * radius
#     yuzi = PI * (radius ** 2)
#     aylana = {
#                 "radius":radius,
#                 "diametr":diametr,
#                 "perimetri":perimetr,
#                 "yuzi":yuzi
#             }
#     return aylana

# radius = float(input("\nAylananing radiusini kiriting:\n>>> "))
# javob = aylana(radius)
# print(javob)

# def prime_number(min_num,max_num):
#     """Berilgan oraliqdagi tub sonlar ro'yxatini ko'rsatuvchi funksiya"""
#     prime_numbers = []
#     for i in range(min_num, max_num+1):
#         prime = True
#         if i == 1:
#             prime = False
#         if i == 2:
#             prime = True
#         else:
#             for n in range(2,i):
#                 if i % n == 0:
#                     prime = False
#         if prime:
#             prime_numbers.append(i)
            
#     return prime_numbers

# answer = prime_number(1, 55)
# print(answer)


# def fibonacci(n):
#     """ Foydalanuvchidan son qabul qilib shu songacha bo'lgan 
#     oraliqdagi Fibonachchi sonlar ro'yxatini qaytaruvchi funksiya """
#     fibonacci_numbers = []
#     for i in range(n):
#         if i == 1 or i==0:
#             fibonacci_numbers.append(1)
#         else:
#             fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    
#     return fibonacci_numbers

# test = fibonacci(10)
# print(test)