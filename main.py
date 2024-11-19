def tarifrechner():
    
    print("Willkommen im Museum XXX - Tarifauskunft")
    gesamtpreis = 0.0 

    while True:
       
        alter = int(input("Bitte geben Sie Ihr Alter ein: "))

        if alter <= 14:
            preis = 2.50
            print("Kinderpreis: 2,50 €")
        elif 14 <= alter <= 17:
            preis = 3.50
            print("Jugendlicher: 3,50 €")
        else:
            print("Sind Sie Mitglied im Museumsclub?")
            print("1. Premiummitglied (3 €)")
            print("2. Basismitglied (4 €)")
            print("3. Keine Mitgliedschaft (5 €)")
            mitgliedschaft = input("Wählen Sie Ihre Mitgliedschaft (1/2/3): ")

            if mitgliedschaft == "1":
                preis = 3.00
                sekt = input("Möchten Sie für 0,75 € ein Glas Sekt dazu? (j/n): ").lower()
                if sekt == "j":
                    preis += 0.75
            elif mitgliedschaft == "2":
                preis = 4.00
            else:
                preis = 5.00

        print(f"Ihr Ticket kostet: {preis:.2f} €")
        gesamtpreis += preis
    
        erneut = input("Möchten Sie einen weiteren Tarif abfragen? (j/n): ").lower()
        if erneut != "j":
            break
    
    print(f"Die Gesamtsumme beträgt: {gesamtpreis:.2f} €")
    print("Vielen Dank und viel Spaß im Museum!")

tarifrechner()
