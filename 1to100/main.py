#!/usr/bin/env python3

# This program draw number from 1 to 100 and ask user what number was drawed.

import random

number = random.randint(1,100)

usernumber = 0
i = 0

print("Wylosowałem liczbę. Możesz zgadywać!")
print()

while usernumber != number:
    i += 1
    print("Podaj liczbę: ")
    usernumber = int(input())
    print ("Podałeś %d" %(usernumber))
    if usernumber > number:
        print("Wylosowana liczba jest mniejsza, próbuj dalej!")
    elif usernumber > number:
        print("Wylosowana liczba jest większa, próbuj dalej!")
    else:
        print("Brawo, liczba która została wylosowana to %d. Próbowałeś %d razy!" %(usernumber, i))
        break