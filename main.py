BLAU = "\033[34m"
RESET = "\033[0m"

großer_text = """
DDDD   U   U  III  SSSSS  BBBB  Y   Y  TTTTT  EEEEE
D   D  U   U   I   S      B   B  YYY     T    E
D   D  U   U   I   SSSSS  BBBB    Y      T    EEEE
D   D  U   U   I       S  B   B   Y      T    E
DDDD   UUUUU  III  SSSSS  BBBB    Y      T    EEEEE
"""

def tarifrechner():
    print(BLAU + großer_text + RESET)

    sprache = input("Möchten Sie die Anwendung auf Englisch verwenden? (j/n): ").lower()
    sprache_deutsch = sprache != "j"
    
    gesamtpreis = 0.0 

    while True:
        if sprache_deutsch:
            print("")
            alter = int(input("Bitte geben Sie Ihr Alter ein: "))
        else:
            print("")
            alter = int(input("Please enter your age: "))

        if alter < 14:
            preis = 2.50
            print("")
            print("Kinderpreis: 2,50 €" if sprache_deutsch else "Child price: 2.50 €")
        elif 14 <= alter <= 17:
            preis = 3.50
            print("")
            print("Jugendlicher: 3,50 €" if sprache_deutsch else "Teenager: 3.50 €")
        else:
          
            if sprache_deutsch:
                print("")
                print("Sind Sie Mitglied im Museumsclub?")
                print("1. Premiummitglied (3 €)")
                print("2. Basismitglied (4 €)")
                print("3. Keine Mitgliedschaft (5 €)")
                mitgliedschaft = input("Wählen Sie Ihre Mitgliedschaft (1/2/3): ")
            else:
                print("")
                print("Are you a member of the museum club?")
                print("1. Premium member (3 €)")
                print("2. Basic member (4 €)")
                print("3. No membership (5 €)")
                mitgliedschaft = input("Choose your membership (1/2/3): ")

            if mitgliedschaft == "1":
                preis = 3.00
                print("")
                sekt = input("Möchten Sie für 0,75 € ein Glas Sekt dazu? (j/n): ").lower() if sprache_deutsch else input("Would you like a glass of champagne for 0.75 €? (y/n): ").lower()
                if sekt == "j" or sekt == "y":
                    preis += 0.75
            elif mitgliedschaft == "2":
                preis = 4.00
            else:
                preis = 5.00

        print("")
        print(f"Ihr Ticket kostet: {preis:.2f} €" if sprache_deutsch else f"Your ticket costs: {preis:.2f} €")
        
        if alter >= 18:
            if sprache_deutsch:
                print("")
                tagesticket = input("Möchten Sie ein Tagesticket für den halben oder ganzen Tag? (halber/ganzer): ").lower()
            else:
                print("")
                tagesticket = input("Would you like a day ticket for half or full day? (half/full): ").lower()

            if tagesticket not in ["halber", "ganzer", "half", "full"]:
                print("")
                print("Ungültige Eingabe. Bitte geben Sie 'halb' oder 'ganzer' ein." if sprache_deutsch else "Invalid input. Please enter 'half' or 'full'.")
                continue

            if tagesticket == "halber" or tagesticket == "half":
                if mitgliedschaft == "1":
                    preis_tag = 6.00  
                elif mitgliedschaft == "2":
                    preis_tag = 8.00  
                else:
                    preis_tag = 10.00  
            else:
                if mitgliedschaft == "1":
                    preis_tag = 10.00  
                elif mitgliedschaft == "2":
                    preis_tag = 12.00  
                else:
                    preis_tag = 15.00  

            print("")
            print(f"Das Tagesticket kostet: {preis_tag:.2f} €" if sprache_deutsch else f"The day ticket costs: {preis_tag:.2f} €")
            preis += preis_tag

        gesamtpreis += preis

        if sprache_deutsch:
            print("")
            erneut = input("Möchten Sie einen weiteren Tarif abfragen? (j/n): ").lower()
        else:
            print("")
            erneut = input("Would you like to check another tariff? (y/n): ").lower()

        if erneut != "j" and erneut != "y":
            break

    print("")
    print(f"Die Gesamtsumme beträgt: {gesamtpreis:.2f} €" if sprache_deutsch else f"The total amount is: {gesamtpreis:.2f} €")
    print("Vielen Dank und viel Spaß im Museum!" if sprache_deutsch else "Thank you and enjoy your visit to the museum!")

tarifrechner()
