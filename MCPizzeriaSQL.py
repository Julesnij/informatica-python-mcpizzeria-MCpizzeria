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


### --------- Hoofdprogramma  ---------------

#verwijderTabellen()
maakTabellenAan()

voegPizzaToe("Margarita", 9.50)
voegPizzaToe("Hawaii", 12.25)
voegPizzaToe("Salami", 10.0)

voegKlantToe("Coum")
voegKlantToe("Paramaribo")

printTabel("tbl_pizzas") 
printTabel("tbl_klanten") 