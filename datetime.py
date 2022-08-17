# 38-dars: PYTHON STANDART KUTUBXONASI
# Sana: 17/08/2022
# Muallif: Nozimjon Nabiev

# import datetime as dt

# hozir = dt.datetime.now()
# next_week = dt.datetime(2022,8,24,17,15,00)
# week2 = dt.datetime(2022,9,9,17,15,15)
# week3 = dt.datetime(2022,9,15,10,15,12)
# week4 = dt.datetime(2022,9,24,22,45,15)
# print(f"{next_week}\n{week2}\n{week3}\n{week4}")

# today = dt.date.today()
# ramadan = dt.date(2023,3,22)
# qurbon_hayiti = dt.date(2023,6,28)
# farq_ramadan = today-ramadan
# farq_qurbon_hayiti = today-qurbon_hayiti 
# print(f"Ramazon hayitigacha {farq_ramadan.days} kun qoldi.\nQurbon hayitigacha {farq_qurbon_hayiti.days} kun qoldi.")

# yil = int(input("Tug'ilgan yilingizni kiriting:\n>>> "))
# oy = int(input("Tug'ilgan oyingizni kiriting:\n>>> "))
# kun = int(input("Tug'ilgan kuningizni kiriting:\n>>> "))

# def necha_kun(yil,oy,kun):
#     hozir = dt.date.today()
#     birthday = dt.date(yil,oy,kun)
#     farq = hozir - birthday
#     days = farq.days
#     year = int(days / 365)
#     months = int((days % 365) / 30)
#     kun = int(days % 365 % 30)
#     print(f"Tug'ilgan kuningizdan to bugungi kungacha {year} yil-u, {months} oy {kun} kun bo'ldi.")
    
    
natija = necha_kun(yil,oy,kun)
print(natija)