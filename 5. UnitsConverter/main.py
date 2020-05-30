#!/usr/bin/env python3

def powerConverter(val):
    print("%fKM = %fkW" %(val, val * 0.73))
    print("%fkW = %fKM" %(val, val * 1.359622))

def massConverter(val):
    print("%fkg = %flbs" %(val, val*2.204623))
    print("%flbs = %fkg" %(val, val*0.453592))

def temperatureCOnverter(val):
    print("%fC = %fK" %(val, val+273.15))
    print("%fK = %fC" %(val, val-273.15)) 

def energyConverter(val):
    print("%fJ = %fkWh" %(val, val*0.000000278))
    print("%fkWh = %fJ" %(val, val*3600))

def drawMenu():
    print("Hello. Choose one of:")
    print("1. Power             KM/kW")
    print("2. Energy            J/kWh")
    print("3. Mass              lbs/kg")
    print("4. Temperature       C/K")
    print("")
    print("Your choice is: ")



drawMenu()
chosenOption = input()

if chosenOption == "1":
    powerConverter(float(input("Input value:")))
elif chosenOption == "2":
    input("Input value:")
elif chosenOption == "3":
    input("Input value:")
elif chosenOption == "4":
    input("Input value:")
elif chosenOption == "0":
    exit()
