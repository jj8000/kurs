class User:

    def __init__(self, imie, dataurodzenia):
        self.imie = imie
        self.dataurodzenia = dataurodzenia

    def wiek(self):
        dzis = datetime.datetime.now()
        yyyy = int(self.dataurodzenia[0:4])
        wiek = dzis.year - yyyy
        return wiek

user = User("Tomek", 19990623)
print(user.wiek)