#!/usr/bin/env python3
import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        i += 1
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


drawedNumbers = []


while len(drawedNumbers) < 6:
    number = random.randint(1,49)
    if number in drawedNumbers:
        continue
    else:
        drawedNumbers.append(int(number))


bubbleSort(drawedNumbers)
print("Wylosowałem 6 liczb. Zgaduj!")

# line below should be removed to play (just4manualTests)
print(drawedNumbers)

print("Podaj 6 liczb z zakresu 1 - 49 oddzielone spacjami:")

numbers = input("Moje liczny to: ")

tab_numbers = numbers.split(" ")
numbers = []
for number in tab_numbers:
    while (int(number) > 49) or (int(number) < 1):
        print("Liczka %d jest nieprawidłowa (poza zakresem 1-49)." %(int(number)))
        number = int(input("Podaj inną liczbę : "))
    print(number)
    numbers.append(int(number))
    if len(numbers) == 6:
        break

print(numbers)

bubbleSort(numbers)

print("Posortowane liczby: ")
print(numbers)

print("Moje liczby to: ")
print(drawedNumbers)

n = 0

for i in range(len(drawedNumbers)):
    if numbers[i] in drawedNumbers:
        n += 1

print("Brawo, odgadłeś aż %d liczb" %(n))
