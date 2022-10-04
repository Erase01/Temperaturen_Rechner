# Temperatur in Grad Celsius C
# Temperatur in Grad Kelvin K
# K = C + 273.15



def cel():
    kelvin = float(input("Geben Sie den Grad Kelvin ein, den Sie in Celsius umrechnen möchten: "))
    celsius = kelvin - 273.15
    print(kelvin, "Grad Kelvin, sind", celsius, "Grad Celsius.")

def kel():
    celsius = float(input("Geben Sie den Grad Celsius ein, den Sie in Kelvin umrechnen möchten: ")) 
    kelvin = celsius + 273.15
    print(celsius, "Grad Celsius, sind", kelvin, "Grad Kelvin.") 
       
def menu():
    print("1: In Grad Celsius")
    print("2: In Grad Kelvin")
    print("3: Exit")

def quit():
    print("Over and Out")
    exit()

while True:
    print("")
    menu()
    grad = int(input("Wählen Sie die gewünschte Rechenmetode aus: "))
    
    if grad == 1:
        cel() 
    elif grad == 2:
        kel()
    elif grad == 3:
        quit()
    else:
        print("Error: wählen Sie eine der zur Auswahl stehenden Möglichkeiten!")
