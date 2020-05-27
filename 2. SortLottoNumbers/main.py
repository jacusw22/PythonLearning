#!/usr/bin/env python3

print("Podaj 6 liczb z zakresu 1 - 49 oddzielone spacjami a ja je posortuje:")

numbers = input("Moje liczny to: ")

tab_numbers = numbers.split(" ")
sorted_numbers = []
for number in tab_numbers:
    print(int(number))
    sorted_numbers.append(number)


print(sorted_numbers)


