class client:
    def __init__(self,name,lastname,age,adresse):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.adresse = adresse

    def showclient(self):
        print(f"{self.name} {self.lastname} born in {2021-self.age}, he live in {self.adresse}")

#--------------------------------------#
name=input("client name: ")
lastname=input("client lastname: ")
age=int(input("client age (should be integer): "))
adresse=input("client adresse: ")


c1 = client(name,lastname,age,adresse)
c1.showclient()
