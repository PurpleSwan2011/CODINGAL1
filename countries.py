class India():
    def capital(self):
        print("new Delhi is the capital of India")
    def language(self):
        print("Hindi is the widely spoken language of India")
    def type(self):
        print("India is a develop country")
class USA():
    def capital(self):
        print("Washington,D.C. is the capital of USA")
    def language(self):
        print("eng is the primary language")
    def type(self):
        print("USA is a developed country")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
    