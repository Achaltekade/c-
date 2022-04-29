class India():
     def capital(self):
         print("New Dilhi is the capital for India.")
     def language(self):
         print("Hindi ismost widly spoken language of India.")
     def type(self):
         print("India is a developing country.")
class Usa():
     def capital(self):
         print("Washington, D.C. is the capital of USA.")
     def language(self):
         print("English is primary language of USA.")
     def type(self):
         print("USA is a developed country.")
     obj_ind = India()
     obj_usa = Usa()
     for country in (obj_ind, obj_usa):
       country.capital()
       country.language()
       country.type()
 
