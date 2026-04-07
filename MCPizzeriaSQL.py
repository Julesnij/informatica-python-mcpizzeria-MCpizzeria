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
        gerechtPrijs REAL NOT NULL);""") 

print("Tabel 'tbl_pizzas' aangemaakt.") 


### --------- Hoofdprogramma  ---------------

