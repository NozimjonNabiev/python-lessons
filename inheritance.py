# 30-dars: VORISLIK VA POLIMORFIZM
# Sana: 13/08/2022
# Muallif: Nozimjon Nabiev

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.subjects = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"ID raqam: {self.idraqam}, {self.tyil}-yilda tug`ilgan \nO'qiyotgan fanlari:{self.subjects}"
        return info
        
    def fanga_yozil(self, fan):
            return self.subjects.append(fan)
        
    def remove_fan(self, fan):
        if fan in self.subjects:
            return self.subjects.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz!"

class Fan:
    def __init__(self, nomi):
        self.name = nomi 
        
    def get_name(self):
        return self.name

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, fan, kafedra):
        super().__init__(ism, familiya, passport, tyil)
        self.fan = fan 
        self.kafedra = kafedra 
        
    def get_info(self):
        info = f"Professor haqida ma'lumotlar:\nIsmi: {self.ism}\nFamiliyasi: {self.familiya}"
        info += f"\nTug'ilgan yili: {self.tyil}-yil, \nDars beradigan fani: {self.fan} \nKafedra: {self.kafedra}"
        return info

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, jinsi, yoshi):
        super().__init__(ism, familiya, passport, tyil)
        self.gender = jinsi 
        self.age = yoshi 
        
        def get_info(self):
            info = f"Foydalanuvchi haqida ma'lumotlar:\nIsmi: {self.ism}\nFamiliyasi: {self.familiya}"
            info += f"\nTug'ilgan yili: {self.tyil}-yil, \nJinsi: {self.gender} \nYoshi: {self.age}"
            return info

class Admin(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, parol, login):
        super().__init__(ism, familiya, passport, tyil)
        self.parol = parol 
        self.login = login
        
    def get_info(self):
        info = f"Admin haqida ma'lumotlar:\nIsmi: {self.ism}\nFamiliyasi: {self.familiya}"
        info += f"\nTug'ilgan yili: {self.tyil}-yil, \nJinsi: {self.gender} \nYoshi: {self.age}"
        return info
        
    def ban_user(self):
        return "Foydalanuvchi bloklandi!"
            
            
# Objects
talaba1 = Talaba("Qodir", "Sobirov", "AB55554441", 2000, "1212555")
talaba2 = Talaba("Ali", "valiyev", "Ac5502488", 2001, "12125444")
talaba3 = Talaba("Anvar", "Sanayev", "AA45454545", 2003, "1000222")

fan1 = Fan("Algebra")
fan2 = Fan("Geometry")
fan3 = Fan("English")
fan4 = Fan("IT")

professor1 = Professor("Otajon", "Xudoyorov", "AB5454564", 1985, "Calculus", "Applied Science")
professor2 = Professor("Aneesh", "Pradeep", "AC4484845",1980, "Computer Science", "Software Engineering")
professor3 = Professor("Sirojiddin", "Jurayev", "AA74789787",1978, "Intro to programming", "Software engineering")

user1 = Foydalanuvchi("Qodir", "Sobirov", "AB55554441", 2000, "Erkak", 22)
user2 = Foydalanuvchi("Asal", "Valiyeva", "Ac5502488", 2001, "Ayol", 21)
user3 = Foydalanuvchi("Anvar", "Sanayev", "AA45454545", 2003, "Erkak", 19)

admin1 = Admin("Admin", "Super", "AC45454454", 1999, "74544545aCds", "admin_5454")

talaba1.fanga_yozil(fan1.name)
talaba2.fanga_yozil(fan3.name)
talaba1.fanga_yozil(fan2.name)

# print(admin1.ban_user())

# print(talaba1.get_info())