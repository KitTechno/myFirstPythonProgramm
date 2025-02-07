# Autor:                Elia Ressl
# Place:                Homeoffice
# Date:                 08.02.2025
# Filename:             speed.py
# Short description:    sobald die geschwindigkeit über 50 ist geht das programm in die anderen fälle nicht hinein. Für die Fälle >55 bis >65 ist deadcode.

while(1):
    speed = float(input("Wie schnell war das Fahrzeug unterwegs (in km/h)? "))
    if speed > 50:
        print("Die Busse beträgt CHF 40.-")
    elif speed > 55:
        print("Die Busse beträgt CHF 120.-")
    elif speed > 60:
        print("Die Busse beträgt CHF 250.-")
    elif speed > 65:
        print("Der Lenker / die Lenkerin wird angezeigt.")
    else:
        print("Die Höchstgeschwindigkeit wurde eingehalten.")
