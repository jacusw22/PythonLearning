#!/usr/bin/env python3

# This program draw number from 1 to 100 and ask user what number was drawed.

import random

number = random.randint(1,100)

usernumber = 0

print("Wylosowałem liczbę. Możesz zgadywać!")
print()

while usernumber != number:
    print("Podaj liczbę: ")
    usernumber = int(input())
    print ("Podałeś %d" %(usernumber))
    if usernumber > number:
        print("Wylosowana liczba jest mniejsza, próbuj dalej!")
    else:
        print("Wylosowana liczba jest większa, próbuj dalej!")

print("Brawo, liczba która została wylosowana to %d" %(usernumber))

