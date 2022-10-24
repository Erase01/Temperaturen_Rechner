# Temperatur in Grad Celsius C
# Temperatur in Grad Kelvin K
# Temperatur in Grad Fahrenheit F
# K = C + 273.15
# F = C * 1.8 + 32
# C = (F - 32) / 1.8 



def KiC():                                                                                                     # Kelvin in Celsius 
    kelvin = float(input("Geben Sie den Grad Kelvin ein, den Sie in Celsius umrechnen möchten: "))
    celsius = kelvin - 273.15
    if kelvin < 0:
        print(kelvin, "Grad Kelvin, sind", celsius, "Grad Celsius.")
        print("Achtung!:", kelvin, "Grad Kelvin /", celsius, "Grad Celsius, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(kelvin, "Grad Kelvin, sind", celsius, "Grad Celsius.")

def FiC():                                                                                                     # Fahrenheit in Celsius
    fahrenheit = float(input("Geben Sie den Grad Fahrenheit ein, den Sie in Celsius umrechnen möchten: "))
    celsius = (fahrenheit - 32) / 1.8
    if fahrenheit < -459.67:
        print(fahrenheit, "Grad Fahrenheit, sind", celsius, "Grad Celsius.")
        print("Achtung!:", fahrenheit, "Grad Fahrenheit /", celsius, "Grad Celsius, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(fahrenheit, "Grad Fahrenheit, sind", celsius, "Grad Celsius.")

def CiK():                                                                                                     # Celsius in Kelvin
    celsius = float(input("Geben Sie den Grad Celsius ein, den Sie in Kelvin umrechnen möchten: ")) 
    kelvin = celsius + 273.15
    if celsius < -273.15:
        print(celsius, "Grad Celsius, sind", kelvin, "Grad Kelvin.")
        print("Achtung!:", celsius, "Grad Celsius /", kelvin, "Grad Kelvin, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(celsius, "Grad Celsius, sind", kelvin, "Grad Kelvin.") 

def FiK():                                                                                                     # Fahrenheit in Kelvin
    fahrenheit = float(input("Geben Sie den Grad Fahrenheit ein, den Sie in Kelvin umrechnen möchten: "))
    kelvin = (fahrenheit + 459.67) / 1.8
    if fahrenheit < -459.67:
        print(fahrenheit, "Grad Fahrenheit, sind", kelvin, "Grad Kelvin.")
        print("Achtung!", fahrenheit, "Grad Fahrenheit /", kelvin, "Grad Kelvin, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(fahrenheit, "Grad Fahrenheit, sind", kelvin, "Grad Kelvin.")

def CiF():                                                                                                     # Celsius in Fahrenheit
    celsius = float(input("Geben Sie den Grad Celsius ein, den Sie in Grad Fahrenheit umrechnen möchten: "))
    fahrenheit = celsius * 1.8 + 32
    if celsius < -273.15:
        print(celsius, "Grad Celsius, sind", fahrenheit, "Grad Fahrenheit.")
        print("Achtung!:", celsius, "Grad Celsius /", fahrenheit, "Grad Kelvin, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(celsius, "Grad Celsius, sind", fahrenheit, "Grad Fahrenheit.")

def KiF():                                                                                                     # Kelvin in Fahrenheit
    kelvin = float(input("Geben Sie den Grad Kelvin ein, den Sie in Grad Fahrenheit umrechnen möchten: "))
    fahrenheit = kelvin * 1.8 - 459.67
    if kelvin < 0:
        print(kelvin, "Grad Kelvin, sind", fahrenheit, "Grad Fahrenheit.")
        print("Achtung!:", kelvin, "Grad Celsius /", fahrenheit, "Grad Kelvin, sind physikalisch nicht zu erreichende Temperaturen!")
    else:
        print(kelvin, "Grad Kelvin, sind", fahrenheit, "Grad Fahrenheit.")


def mainmenu():
    print("1: In Grad Celsius")
    print("2: In Grad Kelvin")
    print("3: In Grad Fahrenheit")
    print("4: Exit")

def submenu(unit):
    s = True
    if  unit == 1:                  # celsius
        def vc():
            nonlocal s
            s = True
            while s == True:
                print("\n1: Von Kelvin")
                print("2: Von Fahrenheit")
                print("3: Zurück zum Hauptmenue")
                value = int(input("Wählen Sie die Temperatureinheiten aus, welche Sie in Celsius umrechnen möchten: "))
           
                if value == 1:
                    KiC()
                elif value == 2:
                    FiC()           
                elif value == 3:
                    s = False
                else:
                    print(error)
        vc()
    elif unit == 2:                # kelvin
        def vk():
            while s == True:
                print("\n1: Von Celsius")
                print("2: Von Fahrenheit")
                print("3: Zurück zum Hauptmenue")
                value = int(input("Wählen Sie die Temperatureinheiten aus, welche Sie in Kelvin umrechnen möchten: "))

                if value == 1:
                    CiK()
                elif value == 2:
                    FiK()           
                elif value == 3:
                    s = False
                else:
                    print(error)
        vk()
    elif unit == 3:                # fahrenheit
        def vf():
            while s == True:
                print("\n1: Von Celsius")
                print("2: Von Kelvin")
                print("3: Zurück zum Hauptmenue")
                value = int(input("Wählen Sie die Temperatureinheiten aus, welche Sie in Fahrenheit umrechnen möchten: "))

                if value == 1:
                    CiF()
                elif value == 2:
                    KiF()           
                elif value == 3:
                    s = False
                else:
                    print(error)
        vf()            
    else:
        print(error)

def quit():
    print("Wird beendet...")
    exit()

while True:
    print("")
    mainmenu()
    grad = int(input("\nWählen Sie die gewünschte Rechenmetode aus: "))
    error = "Error: wählen Sie eine der zur Auswahl stehenden Möglichkeiten!"
    
    if grad == 1:
        submenu(1) 
    elif grad == 2:
        submenu(2)
    elif grad == 3:
        submenu(3)
    elif grad == 4:
        quit()
    else:
        print(error)
        