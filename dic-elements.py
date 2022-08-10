# 15 -dars: Lug'at elementlari bilan ishlash
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev

# ==========================Task 1===================================================
# python_dic ={
#     "integer":"butun son",
#     "loop":"tsikl",
#     "for":"uchun",
#     "float":"o'nlik son",
#     "list":"ro'yxat",
#     "tuple":"o'zgarmas ro'yxat",
#     "if":"agar",
#     "dictionary":"lug'at",
#     "print":"ekranga chiqarish",
#     "elif":"agar masa"
#     }
# 
# for key, value in sorted(python_dic.items()):
#     print(f"Kalit so'z {key}")
#     print(f"Tarjimasi: {value}")
# =============================================================================

# ===========================Task 2==================================================
# countries = {
#     "USA":"Washington DC",
#     "Uzbekistan":"Tashkent",
#     "China":"Beijing",
#     "Great Britain":"London",
#     "Russia":"Moscow",
#     "Germany":"Berlin",
#     "France":"Paris",
#     "Spain":"Madrid",
#     "Italy":"Rome",
#     "India":"New Delhi"
#     }
# 
# for key in sorted(countries.keys()):
#     print(key)
# 
# for value in sorted(countries.values()):
#     print(value)
# =============================================================================

# ===============================Task 3==============================================
# countries = {
#     "usa":"Washington DC",
#     "uzbekistan":"Tashkent",
#     "china":"Beijing",
#     "great britain":"London",
#     "russia":"Moscow",
#     "germany":"Berlin",
#     "france":"Paris",
#     "spain":"Madrid",
#     "italy":"Rome",
#     "india":"New Delhi"
#     }
# 
# country = input("Enter the name of any country:\n>>> ").lower()
# 
# if country in countries:
#     print(f"The capital of {country.title()} is {countries[country]} city")
# else:
#     print(f"Unfortunately, there isn't any information about {country.title()}.")
# =============================================================================



# ===============================Task 4==============================================
# menu = {
#         "osh":"20000",
#         "sho'rva":"18000",
#         "qozonkabob":"25000",
#         "mastava":"15000",
#         "norin":"30000",
#         "lag'mon":"21000",
#         "somsa":"7000",
#         "shashlik":"60000"
#         }
# zakaz = []
# print("3 ta ovqat buyurtma bering:")
# for taom in range(3):
#     zakaz.append(input(f"{taom+1}-ovqat nomini kiriting:").lower())
# 
# for ovqat in zakaz:
#     if ovqat in menu:
#         print(f"{ovqat.title()} - {menu[ovqat]} UZS")
#     else:
#         print(f"Afsuski bizda {ovqat.title()} yo'q.")
# =============================================================================


















