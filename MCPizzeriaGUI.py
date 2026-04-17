# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: Jules                                                                                                                                                                                                                                                                                                  
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------

def zoekKlant(): 
    #haal de ingevoerde_klantnaam op uit het invoerveld 
    #     en gebruik dit om met SQL de klant in database te vinden 
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get()) 
    print(gevonden_klanten) # om te testen 

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!") 
labelIntro.grid(row=0, column=0, sticky="W") 

labelKlantnaam = Label(venster, text="Klantnaam:")
labelKlantnaam.grid(row=1, column=0, sticky="W")

labelKlantnummer = Label(venster, text="Klantnummer:")
labelKlantnummer.grid(row=2, column=0, sticky="W")

ingevoerde_klantnaam = StringVar() 
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam) 
invoerveldKlantnaam.grid(row=1, column=1, sticky="W") 

invoerveldKlantNr = Entry(venster) 
invoerveldKlantNr.grid(row=2, column=1, sticky="W") 

knopSluit = Button(venster, text="Sluiten",width=12,command=venster.destroy) 
knopSluit.grid(row=17, column=4) 

knopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command= zoekKlant)
knopZoekOpKlantnaam.grid(row=1, column=4)



#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
