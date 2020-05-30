#!/usr/bin/env python3

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


print("Podaj 6 liczb z zakresu 1 - 49 oddzielone spacjami a ja je posortuje:")

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