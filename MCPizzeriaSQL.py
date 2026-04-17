# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: Jules
#
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------

def maakTabellenAan(): 
# Maak een nieuwe tabel met 3 kolommen: id, naam, prijs 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tbl_pizzas( 
            gerechtID INTEGER PRIMARY KEY AUTOINCREMENT, 
            gerechtNaam TEXT NOT NULL, 
            gerechtPrijs REAL NOT NULL)
    ;""") 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tbl_klanten( 
            klantNr INTEGER PRIMARY KEY AUTOINCREMENT, 
            klantAchternaam TEXT);
    """) 

def printTabel(tabel_naam): 
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen 
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele 
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens af 

def voegPizzaToe(naam_nieuwe_pizza, prijs_nieuwe_pizza): 
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (naam_nieuwe_pizza, prijs_nieuwe_pizza)) 
    db.commit() #gegevens naar de database wegschrijven 

def verwijderPizza(gerechtNaam): 
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,)) 
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam ) 
    db.commit() #gegevens naar de database wegschrijven 

def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs): 
    cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", (nieuweGerechtNaam, nieuwePrijs, gerechtID )) 
    db.commit() #gegevens naar de database wegschrijven 


def voegKlantToe(naam_nieuwe_klant):  
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,)) 
    print("Klant toegevoegd")
    db.commit() 


#Zoek alle gegevens over klant met ingevoerde naam 
def zoekKlantInTabel(ingevoerde_klantnaam): 
    cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam,)) 
    zoek_resultaat = cursor.fetchall() 
    if zoek_resultaat == []: #resultaat is leeg, geen gerecht gevonden 
        print("Geen klant gevonden met achternaam", ingevoerde_klantnaam) 
        print("Klant wordt nu toegevoegd.") 
        cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ? )", (ingevoerde_klantnaam, )) 
        db.commit()#gegevens in de database zetten 
        printTabel("tbl_klanten") 

        #nu dat klant in tabel is gezet, kunnen we zijn gegevens ophalen 
        cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam, ) ) 
        zoek_resultaat = cursor.fetchall() 

    return zoek_resultaat 

def zoekPizzaInTabel(ingevoerde_pizzanaam): 
    cursor.execute("SELECT * FROM tbl_pizzas WHERE gerechtNaam = ?", (ingevoerde_pizzanaam,)) 
    zoek_resultaat = cursor.fetchall() 
    if zoek_resultaat == []: #resultaat is leeg, geen gerecht gevonden 
        print("Geen pizza gevonden met naam", ingevoerde_pizzanaam) 

    return zoek_resultaat 

def vraagOpGegevensPizzaTabel(): 
    cursor.execute("SELECT * FROM tbl_pizzas") 
    resultaat = cursor.fetchall() 
    print("Tabel tbl_pizzas:", resultaat) 
    return resultaat 

### --------- Hoofdprogramma  ---------------

#verwijderTabellen()
#maakTabellenAan()

#Voeg pizza's toe aan tabel: 
#voegPizzaToe("Margarita", 9.50)
#voegPizzaToe("Hawaii", 12.25)
#voegPizzaToe("Salami", 10.0)

#Voeg klanten toe aan tabel: 
#voegKlantToe("Coum")
#voegKlantToe("Paramaribo")

printTabel("tbl_pizzas") 
printTabel("tbl_klanten") 