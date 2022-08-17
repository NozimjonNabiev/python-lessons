from googletrans import Translator

tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
print("Tarjimon - uz-eng")

matn_uz = input("Tarjima qilish uchun matn kiriting: ")
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)
