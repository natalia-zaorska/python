
cenaSamochodu = input("podaj cenę samochodu ")
print (cenaSamochodu)
cenaSamochodu = int(cenaSamochodu)


podatek = (0.15*cenaSamochodu)
podatek = int (podatek)
oplataRejestracyjna = (0.5*cenaSamochodu)
oplataRejestracyjna = int(oplataRejestracyjna)
prowizjaPrzygotowawcza = 300
prowizjaPrzygotowawcza = int(prowizjaPrzygotowawcza)
oplataZaDostarczenie = 200
oplataZaDostarczenie = int(oplataZaDostarczenie) 


print("Faktyczna cena samochodu to " + str(cenaSamochodu) +" "+ str(podatek) +" "+ str(oplataRejestracyjna)+" "+ str(prowizjaPrzygotowawcza)+" "+ str(oplataZaDostarczenie))

