# 31-dars: INKAPSULATSIYA, KLASSNING XUSUSIYAT VA METODLARI
# Sana: 14/08/2022
# Muallif: Nozimjon Nabiev

from encapsulation import Shaxs, Talaba

shaxs1 = Shaxs("Asror", "Valiyev", "AC4554854", 1996)
shaxs2 = Shaxs("Qodir", "Samandarov", "AA100255", 1999)
shaxs3 = Shaxs("Javlon", "Ahmadov", "AB78852520", 2002)

talaba1 = Talaba("Hojimat", "Erkinov", "AC55645440", 2001)
talaba2 = Talaba("Jaloliddin", "Toshmatov", "AB0784454", 2003)
talaba3 = Talaba("Gulchiroy", "Asadova", "AA5564540", 2002)
talaba4 = Talaba("Asaloy", "Kamolova", "AA5444789", 2002)

print(Shaxs.get_odamlar_soni())
print(Talaba.get_student_num())
print(talaba2.get_id())
print(talaba2.get_info())