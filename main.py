BLAU = "\033[34m" #farbcodes von ChatGPT, macht Consolenausgaben farbig oder resettet sie
RESET = "\033[0m"

großer_text = """
DDDD   U   U  III  SSSSS  BBBB  Y   Y  TTTTT  EEEEE
D   D  U   U   I   S      B   B  YYY     T    E
D   D  U   U   I   SSSSS  BBBB    Y      T    EEEE
D   D  U   U   I       S  B   B   Y      T    E
DDDD   UUUUU  III  SSSSS  BBBB    Y      T    EEEEE
""" #""" ist ür mehrzeilige ausgaben da

def tarifrechner(): #das is die Funktion, also nur die definition, die unktion wird in der letzten Zeile ausgeführt
    print(BLAU + großer_text + RESET) #Variable aus Zeile 4 wird ausgegeben

    sprache = input("Möchten Sie die Anwendung auf Englisch verwenden? (j/n): ").lower() #sprache ist eine variable und beinhaltet ein input. das .lower ist nur dass es in kleinbuchstaben formatiert wird
    sprache_deutsch = sprache != "j" #wenn man nicht j eingibt (!=) ist die sprache deutsch, sonst ist es standartmäßig false, also englisch 
    
    gesamtpreis = 0.0 #deklaration ür den gesamtpreis der bei 0 ist

    while True:  #schleife für die alters abfrage die unendlich geht, solange der benutzer nicht fertig mit der eingabe ist oder break genutzt wurde
        if sprache_deutsch: #wenn die sprache deutsch ist =>
            print("") #Platzhalter wegen der ordnung
            alter = int(input("Bitte geben Sie Ihr Alter ein: "))# <= dann soll der benutzer sein alter, eine zahl eingeben welche in "alter" gespeichert wird
        else: #anderfalls wenn die sprache englisch ist das gleiche au englich
            print("") #Wieder platzhalter
            alter = int(input("Please enter your age: ")) #wieder altersabfrage

        if alter < 14: #wenn das alter kleiner als 14 ist =>
            preis = 2.50 #deklaration preis wird nur ausgegeben wenn alter kleiner als 14 ist
            print("") #Platzhalter
            print("Kinderpreis: 2,50 €" if sprache_deutsch else "Child price: 2.50 €") #<= dann wird Kinderpreis auf deutsch oder auf englisch ausgegeben
        elif 14 <= alter <= 17: #falls alter zwischen 14 und 17 ist ist der preis 
            preis = 3.50 #3.5€
            print("") #platzhalter
            print("Jugendlicher: 3,50 €" if sprache_deutsch else "Teenager: 3.50 €") #Ausgabe jugentlicher au beiden sprachen
        else: #ANDERNFALLS (also weder noch wenn das alter alles über 17 ist
          
            if sprache_deutsch: #if für deutsche sprache, hier wird alles ausgegeben mit print
                print("")
                print("Sind Sie Mitglied im Museumsclub?")
                print("1. Premiummitglied (3 €)")
                print("2. Basismitglied (4 €)")
                print("3. Keine Mitgliedschaft (5 €)")
                mitgliedschaft = input("Wählen Sie Ihre Mitgliedschaft (1/2/3): ") #variable mitgliedschat speicher einen input, die zahl der mitgliedschat
            else: #wenn sprache nicht deutsch ist das gleiche auf englisch
                print("")
                print("Are you a member of the museum club?")
                print("1. Premium member (3 €)")
                print("2. Basic member (4 €)")
                print("3. No membership (5 €)")
                mitgliedschaft = input("Choose your membership (1/2/3): ")

            if mitgliedschaft == "1": #wenn mitgliedschaft (input) 1 ist
                preis = 3.00 # betr#gt der preis 3 euro
                print("") # platzhalter
                sekt = input("Möchten Sie für 0,75 € ein Glas Sekt dazu? (j/n): ").lower() if sprache_deutsch else input("Would you like a glass of champagne for 0.75 €? (y/n): ").lower() # frage nach sekt, au beiden sprachen wieder
                if sekt == "j" or sekt == "y": # wenn der input der variable sekt j für ja oder  y für yes ist 
                    preis += 0.75 #wird 0,75 cent auf den preis gerechnet
            elif mitgliedschaft == "2": #wenn die mitgliedschaft 2 ist
                preis = 4.00 # ist der preis 4 euro
            else: #anderfalls ist der
                preis = 5.00 #5 Euro

        print("")
        print(f"Ihr Ticket kostet: {preis:.2f} €" if sprache_deutsch else f"Your ticket costs: {preis:.2f} €") 
        # Hier oben wird der ticketpreis berechnet. .2f heit auf 2 nachkommastellen aurunden wegen 0,00 euro foramt und das gleiche auf englisch

        
        if alter >= 18: # wenn das alter 18 oder höher ist
            if sprache_deutsch: #wird nochmal die sprache vom priogramm gecheckt
                print("") #paltzhalter 
                tagesticket = input("Möchten Sie ein Tagesticket für den halben oder ganzen Tag? (halber/ganzer): ").lower() # hier wird dann gefragt ob man einen halben oder ganzen tag bleiben mlchte
            else: # auf englisch das ganze nochmal
                print("")
                tagesticket = input("Would you like a day ticket for half or full day? (half/full): ").lower()

            if tagesticket not in ["halber", "ganzer", "half", "full"]: # falls die eingabe was anderes als die 4 wörter ist
                print("") # platzhalter
                print("Ungültige Eingabe. Bitte geben Sie 'halb' oder 'ganzer' ein." if sprache_deutsch else "Invalid input. Please enter 'half' or 'full'.")#wird ein fehler ausgegeben
                continue #das ganze nochmal vonvorn

            if tagesticket == "halber" or tagesticket == "half": #wenn du ein halben tag ausgewählt hast
                if mitgliedschaft == "1": # wird hier die mitgliedschaft 1 abgeragt
                    preis_tag = 6.00  #der preis ist dann 6 euro
                elif mitgliedschaft == "2": #andernfalls dann bei 2
                    preis_tag = 8.00  #sind es 8 euro
                else:    #mochmal andernfalls ist es 
                    preis_tag = 10.00  # 10 € | Hinweis: elif kann für beliebig viele möglichkeiten genutzt werden
            else: #wenn der andere fall autritt, also der ganze tag gewählt wurde beginnt wieder das gleiche. also die abfrage mit den preisen
                if mitgliedschaft == "1":
                    preis_tag = 10.00  
                elif mitgliedschaft == "2":
                    preis_tag = 12.00  
                else:
                    preis_tag = 15.00  

            print("") # platzhalter
            print(f"Das Tagesticket kostet: {preis_tag:.2f} €" if sprache_deutsch else f"The day ticket costs: {preis_tag:.2f} €") #hier wird der ticketpreis ausgegeben
            preis += preis_tag #hier wird alles addiert

        gesamtpreis += preis

        if sprache_deutsch: #wenn die sprache deutsch ist wird nach noch einem ticket gefragt
            print("")
            erneut = input("Möchten Sie einen weiteren Tarif abfragen? (j/n): ").lower() #erneut ist die variable wo deine eingabe gespeichert wird
        else: # wenn sprache nicht deutsch, wird es auf englisch ausgegeben
            print("")
            erneut = input("Would you like to check another tariff? (y/n): ").lower()

        if erneut != "j" and erneut != "y": #wenn variable erneut ungleich j oder y für ja und yes ist, wird die schleife mit break beendet
            break

    print("") #wenn die schlefie zu ende ist wird nochmal der gesamtpreus auf den sprachen ausgegeben
    print(f"Die Gesamtsumme beträgt: {gesamtpreis:.2f} €" if sprache_deutsch else f"The total amount is: {gesamtpreis:.2f} €")
    print("Vielen Dank und viel Spaß im Museum!" if sprache_deutsch else "Thank you and enjoy your visit to the museum!")

tarifrechner() # hier wird die funktion tarifrechner aufgerufen, der code davor war nur was ist der funktion passieren soll
