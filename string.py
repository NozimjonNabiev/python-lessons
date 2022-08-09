# 6-dars
# STRING (MATN)
# SANA: 09/08/2022
# Muallif: Nozimjon

# 1-mashq

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

kocha = input("Ko'changizni nomini kiriting: \n>>>")
mahalla = input("Mahallangiz nomini kiriting: \n>>>")
tuman = input("Tumaningiz nomini kiriting: \n>>>")
viloyat = input("Viloyatingiz nomini kiriting: \n>>>")

print(f"Siz {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyatida yashaysiz.")

print(f"Siz {kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyatida yashaysiz.")

manzil = f"Siz {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyatida yashaysiz."

print(manzil.title())
print(manzil.capitalize())
print(manzil.lower())
print(manzil.upper())