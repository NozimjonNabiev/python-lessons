# 31-dars: INKAPSULATSIYA, KLASSNING XUSUSIYAT VA METODLARI
# Sana: 14/08/2022
# Muallif: Nozimjon Nabiev

from uuid import uuid4

class Shaxs:
    __odamlar_soni = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
    
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f" {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def get_passport(self):
        return self.__passport
        

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = uuid4()
        self.bosqich = 1
        self.subjects = []
        Talaba.__talabalar_soni += 1
    
    @classmethod
    def get_student_num(cls):
        return cls.__talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan \nO'qiyotgan fanlari:{self.subjects}"
        return info
        
    def fanga_yozil(self, fan):
            return self.subjects.append(fan)
        
    def remove_fan(self, fan):
        if fan in self.subjects:
            return self.subjects.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz!"
        
    

