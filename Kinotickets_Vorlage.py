alter = int(input("Wie alt sind Sie?"))
anzahl = int(input("Wieviele tickets möchten Sie haben?"))



if alter <= 18:
    print(5 * anzahl) 
elif alter > 65:
    print(7.50 * anzahl)
    
else:
    print(10 * anzahl)
