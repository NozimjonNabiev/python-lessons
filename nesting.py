# 16 -dars: Nesting
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev

# =============================Task 1================================================
# person1 = {
#     "ism":"Elon Musk",
#     "tugilgan yili":"1969",
#     "sohasi":"Engineering",
#     "tugilgan joyi":"JAR"
#     }
# 
# person2 = {
#     "ism":"Bill Gates",
#     "tugilgan yili":"1950",
#     "sohasi":"Computer Software",
#     "tugilgan joyi":"USA"
#     }
# 
# person3 = {
#     "ism":"Cristiano Ronaldo",
#     "tugilgan yili":"1985",
#     "sohasi":"Futbol",
#     "tugilgan joyi":"Portugal"
#     }
# 
# famous_people = [person1, person2, person3]
# 
# for person in famous_people:
#     print(f"{person['ism']} {person['tugilgan yili']}-yilda {person['tugilgan joyi']}da tavallud topgan. Uning sohasi {person['sohasi']}\n")
# =============================================================================
    
    
# ================================Task 2=============================================
# person1 = {
#     "ism":"Elon Musk",
#     "tugilgan yili":"1969",
#     "sohasi":"Engineering",
#     "tugilgan joyi":"JAR",
#     "asari":["Elon Musk","Engineering"]
#     }
# 
# person2 = {
#     "ism":"Bill Gates",
#     "tugilgan yili":"1950",
#     "sohasi":"Computer Software",
#     "tugilgan joyi":"USA",
#     "asari":["How to become millionare?", "Microsoft"]
#     }
# 
# person3 = {
#     "ism":"Cristiano Ronaldo",
#     "tugilgan yili":"1985",
#     "sohasi":"Futbol",
#     "tugilgan joyi":"Portugal",
#     "asari":["G.O.A.T.", "Legend"]
#     }
# 
# famous_people = [person1, person2, person3]
# 
# # for person in famous_people:
# #    print(f"{person['ism']} quyidagi asarlarni yozgan: {person['asari']}\n")
# 
# for person in famous_people:
#     ism = person['ism']
#     asarlari = person['asari']
#     print(f"{ism} quyidagi asarlarni yozgan:")
#     for asar in asarlari:
#         print(asar.title())
#     print("\n")
# =============================================================================

# ========================Task 3=====================================================
# ism = input("Ismingzini kiriting:\n>>> ").lower()
# 
# kinolar = {ism:[]}
# 
# print("\n3 ta sevimli kinolaringiz nomini kiriting:")
# 
# for kino in range(3):
#     kinolar[ism].append(input(f"{kino+1}- sevimli kinongizni nomi: "))
# 
# print(f"\nSizning ismingiz: {ism.title()}")
# print("Siz yoqtirgan kinolar:")
# 
# for i in kinolar[ism]:
#     print(i.title())
# =============================================================================



# ==========================Task 4===================================================
# davlatlar ={
#     "Germany": { "capital":"Berlin",
#                  "dialing code":"+49",
#                  "president":"Frank-Walter Steinmeir",
#                  "population":"83.24 million",
#                  "currency":"Euro"
#                },
#     
#     "Italy": {  "capital":"Rome",
#                 "dialing code":"+39",
#                 "president":"Sergio Matarella",
#                 "population":"59.55 million",
#                 "currency":"Euro"
#              },
#     
#     "France": {  "capital":"Paris",
#                  "dialing code":"+33",
#                  "president":"Emmanuel Macron",
#                  "population":"67.39 million",
#                  "currency":["Euro", "CFP franc"]
#              },
#     
#     "Portugal":{ "capital":"lisbon",
#                  "dialing code":"+351",
#                  "president":"Marcelo Rebelo de Sousa",
#                  "population":"10.31 million",
#                  "currency":"Euro"
#              }
#     }
# 
# for key, values in davlatlar.items():
#     print(f"\nCountry name:{key}")
#     print(f"Dialing code: {values['dialing code']}")
#     print(f"President: {values['president']}")
#     print(f"Population: {values['population']}")
#     if key == 'France':
#         print("Currency: ")
#         for i in values['currency']:
#             print(f"{i} ")
#     else:
#         print(f"Currency: {values['currency']}")
# =============================================================================
        
        

davlatlar ={
    "germany": { "capital":"Berlin",
                 "dialing code":"+49",
                 "president":"Frank-Walter Steinmeir",
                 "population":"83.24 million",
                 "currency":"Euro"
               },
    
    "italy": {  "capital":"Rome",
                "dialing code":"+39",
                "president":"Sergio Matarella",
                "population":"59.55 million",
                "currency":"Euro"
             },
    
    "france": {  "capital":"Paris",
                 "dialing code":"+33",
                 "president":"Emmanuel Macron",
                 "population":"67.39 million",
                 "currency":["Euro", "CFP franc"]
             },
    
    "portugal":{ "capital":"lisbon",
                 "dialing code":"+351",
                 "president":"Marcelo Rebelo de Sousa",
                 "population":"10.31 million",
                 "currency":"Euro"
             }
    }

key = input("Enter the name of any country you would like to know about:\n>>> ").lower()

if key in davlatlar:
    davlat = davlatlar[key]
    print(f"\nCountry name:{key.title()}")
    print(f"Dialing code: {davlat['dialing code']}")
    print(f"President: {davlat['president']}")
    print(f"Population: {davlat['population']}")
    print(f"Currency: {davlat['currency']}")
else:
    print(f"Unfortunately, we don't have any information about {key.title()}.")































