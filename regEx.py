# 38-dars: PYTHON STANDART KUTUBXONASI
# Sana: 17/08/2022
# Muallif: Nozimjon Nabiev

import re


# sample = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# while True:
#     phone_num = input("Telefon raqamingizni kiriting:\n>>> ")
#     if re.match(sample,phone_num):
#         print("Telefon raqamingiz ro'yxatdan o'tdi.")
#         break
#     else:
#         print("Bunday telefon raqam mavjud emas!")


matn = """Assalom alaykum hurmatli do'stlar. 
Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI 
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar 
va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test """

sample = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
urls = re.findall(sample, matn)
print(urls)