# 37-dars: KLASSNI TEKSHIRISH
# Sana: 16/08/2022
# Muallif: Nozimjon Nabiev

import unittest 
from dunder import Shaxs, Talaba

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = "Vali"
        familiya = "Aliyev"
        passport = "AC4545454"
        tyil = 2002
        self.shaxs1 = Shaxs(ism, familiya,passport,tyil)
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        
    def test_get_age(self):
        self.assertEqual(self.shaxs1.get_age(2022), 2022 - self.shaxs1.tyil)

class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = "Karim"
        familiya = "Salimov"
        passport = "AC4500004"
        tyil = 2004
        bosqich = 2
        self.subjects = []
        self.talaba1 = Talaba(ism, familiya, passport, tyil, bosqich)
    
    def test_create(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.bosqich)
        
    def test_set_bosqich(self):
        self.talaba1.set_bosqich(3)
        self.assertEqual(self.talaba1.bosqich, 3)
    
    def test_fanga_yozil(self):
        fan =  "Algebra"
        self.talaba1.fanga_yozil(fan)
        self.assertIsNotNone(self.subjects)
        
unittest.main()