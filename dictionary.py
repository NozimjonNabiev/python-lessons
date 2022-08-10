# 14 -dars: Dictionary(Lug'at)
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev

# =================================Task 1============================================
# dadam = {"ism" : "Nusrat", "tugilgan yili" : "1975", "manzili":"Buxoro viloyati"}
# onam = {"ismi":"Marg'uba", "tugilgan yili":"1977", "manzili":"Buxoro viloyati"}
# singlim ={"ismi":"Maftuna", "tugilgan yili": "2007", "manzili":"Buxoro viloyati"}
# 
# print(f"Otamning ismi {dadam['ism']}, {dadam['tugilgan yili']}-yilda, {dadam['manzili']}da tavallud topgan")
# print(f"Onamning ismi {onam['ismi']}, {onam['tugilgan yili']}-yilda, {onam['manzili']}da tavallud topgan")
# print(f"Singlimning ismi {singlim['ismi']}, {singlim['tugilgan yili']}-yilda, {singlim['manzili']}da tavallud topgan")
# 
# =============================================================================


# ===========================Task 2==================================================
# sevimli_taomlar = {"dadam":"grechka palov", "onam":"shashlik", "singlim":"manti","kichik singlim":"grill","me":"norin"}
# print(f"Dadamning sevimli taomlari {sevimli_taomlar['dadam'].title()}")
# print(f"Oyimning sevimli taomlari {sevimli_taomlar['onam'].title()}")
# print(f"Mening sevimli taomim {sevimli_taomlar['me'].title()}")
# =============================================================================

# ==============================Task 3===============================================
# python_dic ={"integer":"butun son", "float":"o'nlik son", "string":"matn", "boolean":"rost, yolg'on", "function":"funktsiya","if-else":"agar masa"}
# user_input = input("Python kursida tushunmagan birorta atamani kiriting:\n>>> ").lower()
# # print(f"{user_input.title()} so'zining ma'nosi {python_dic[user_input]}")
# 
# print(python_dic.get(user_input, "Afsuski, lug'atda bunday so'z mavjud emas:("))
# =============================================================================


# =================================Task 4============================================
# python_dic ={"integer":"butun son", 
#              "float":"o'nlik son", 
#              "string":"matn", 
#              "boolean":"rost, yolg'on",
#              "function":"funktsiya",
#              "if-else":"agar masa"
#              }
# user_input = input("Python kursida tushunmagan birorta atamani kiriting:\n>>> ").lower()
# 
# if user_input in python_dic:
#     print(f"{user_input.title()} so'zining ma'nosi {python_dic[user_input]}")
# else:
#     print("Bunday so'z lug'atimizda mavjud emas!")
# =============================================================================
