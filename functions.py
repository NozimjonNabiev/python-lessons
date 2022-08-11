# 19-dars: FUNKSIYALAR
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev

# def t_yil(ism, yosh):
#     """ Foydalanuvchi ismi va ysohini so'rab 
#     uni tugilgan yilini ko'rsatuvchi funksiya """
#     print(f"{ism.title()} sizning tug'ilgan yilingiz {2022 - yosh}-yil")
    
# ism = input("Ismingiz nima?\n>>> ")
# yosh = int(input("Yoshingiz nechida>\n>>> "))
# t_yil(ism, yosh)



# def kvadrat_kub(son):
#     """ Foydalanuvchidan son olib, 
#     uning kvadrati va kubini hisoblab beruvchi funksiya """
#     print(f"{son} ning kvadrati {son ** 2}")
#     print(f"{son} ning kubi {son ** 3}")

# son = float(input("Istalgan son kiriting:\n>>> "))
# kvadrat_kub(son)



# def max(son1, son2):
#     """Foydalanuvchidan ikkita son olib 
#     ularning kattasini qaytaruvchi funksiya """
#     if son1 > son2:
#         print(f"\n{son1} katta")
#     elif son2 > son1:
#         print(f"\n{son2} katta")
#     else:
#         print("Sonlar teng! ")

# son1 = float(input("1-sonni kiriting:\n>>> "))
# son2 = float(input("2-sonni kiriting:\n>>> "))
# max(son1, son2)



# def daraja(x, y=2):
#     """Foydalanuvchidan ikkita son olib 
#     birinchisini darajasini qaytaruvchi funksiya """
#     print(f"{x} ning {y}-darajasi {x ** y} ga teng.")

# son1 = float(input("x ga qiymat bering:\n>>> "))
# son2 = float(input('y ga qiymat bering:\n>>> '))
# daraja(son1, son2)


# def qoldiqsiz_bolinish(son):
#     """ Foydalanuchidan son qabul qilib
#     sonni 2 dan 10 gacha bo'lgan sonlarga qoldisiz 
#     bo'linishini tekshiruvchi funsiya"""
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo'linadi")
        
# son = float(input("Istalgan sonni kiriting:\n>>> "))
# qoldiqsiz_bolinish(son)



























