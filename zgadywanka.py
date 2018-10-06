#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
liczba = random.randint(1,10)
# print("Wylosowana liczba ", liczba)
#odp = input(:Jaka liczbe od 1 do 49 wylosowano")

for i in range(6):

	odp = input("Jaka liczbe od 1 do 10 wylosowano")
	print ("zgadujesz po raz ", (i+1) )
	if liczba == int(odp):
		print("Hurrrraaa")
		break
	else:
		print ("Niestety")
		if (int(odp) > liczba):
			print ("Liczba jest wieksza od zgadywanej")
		else:
			print("Liczba jest mniejsza od zgadywanej")
		
	
print(liczba)




