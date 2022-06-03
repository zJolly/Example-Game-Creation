#! /usr/bin/python3
import os


Polpoverace=['Polpo verace','Spuma di patate, peperoni, pane alle cipolle di Tropea']
Truciolidiseppia=['Trucioli di seppia', 'Seppioline arrostite in salsa cacio e pepe']
Gambericroccanti=['Gamberi croccanti', 'con salsa cocktail, lattuga di mare']
AlicidelCantabrico=['Alici del cantabrico', 'con focaccia, puntarelle, burro fatto in casa']
Tartare=['Tartare', 'Battuta di fassone, prosciutto, polvere di salvia']
Crudodinverno=['Crudo d’inverno', 'Tonno rosso, castagne e melograno']
Trigliadiscoglio=['Triglia di scoglio', 'Finte lenticchie, tartufo nero, infuso all’alloro']

Gnocchi=['Gnocchi' , 'di ceci, baccala e limone candito']
Zucca=['Zucca' , 'Tortelli, astice, brodo di Culatello']
MilanoRoma=['Milano Roma' , 'Risotto allo zafferano, coda alla vaccinara']
BurroEAlici=['Burro e alici' , 'Spaghettone “ARTE Agricola”, burro, alici del Cantabrico']
CarbonaraOroNero=['Carbonara oro nero' , 'Mezze maniche “A.R.T.E. Agricola“, uovo bio, pecorino “Gennari” (consigliata per n. 3 ospiti)']
PolloRuspanteAlGirarrosto=['Pollo ruspante al girrarosto' , 'con patate croccanti e spinacetti']
PescatoDelGiorno=['Pescato del giorno' , 'con carciofi croccanti ripieni alla bufala']
FilatoDiFassone=['Filato di fassone' , 'con radicchio di Treviso al barolo']

Margherita=['Margherita' , 'Polpa Mutti, mozzarella, basilico fresco']
Pugliese=['Pugliese' , 'Polpa Mutti, mozzarella, cipolla rossa']
Wurstel=['Wurstel' , 'Polpa Mutti, mozzarella, wurstel del Trentino']
SalaminoPiccante=['Salamino piccante' , 'Polpa Mutti, mozzarella, salamino piccante']
Zucchine=['Zucchine' , 'Polpa Mutti, mozzarella, zucchine, grana']
Melanzane=['Melanzane' , 'Polpa Mutti, mozzarella, melanzane grigliate, grana']
Romana=['Romana' , 'Polpa Mutti, mozzarella, acciughe, capperi']
Caprese=['Caprese' , 'Polpa Mutti, mozzarella, pomodorini, basilico fresco']

TagliataDiFruttaDiStagione=['Tagliata di frutta di stagione']
GelatiArtigianali=['Gelati artigianali']
MonteblancDiCastagne=['Monteblanc di castagne']
SemifreddoAllaVaniglia=['Semifreddo alla vaniglia']
CrostatinaAllaMela=['Crostatina alla mela ']
Tiramisù=['Tiramisù' , 'con crumble al caffè, mascarpone, cioccolato extra fondente']
Zabaione=['Zabaione' , 'Con uova bio']

Birra=['Birra']
CocaCola=['Coca Cola']
Fanta=['Fanta']
Vino=['Vino']
Acqua=['Acqua']

def InfoGenerali():
	somma=0
	os.system('clear')
	scelta=input("Premi 3 per aprire il menù: ")
	while scelta=="3":
		os.system('clear')
		print("--------------------------------------------------------------------------------")
		print("1 - Antipasti")
		print("2 - Primi Piatti")
		print("3 - Pizza")
		print("4 - Dolce")
		print("5 - Bevande")
		print("6 - Vedi il tuo scontrino")
		print("--------------------------------------------------------------------------------")
		scelta=input("Scelta: ")
		while scelta=="6":
			print("Il tuo scontrino per adesso è di un totale di €", somma)
			scelta=input("Premi 3 per continuare a scegliere i tuoi piatti\nPremi 4 per pagare: ")
			if scelta=="4":
				scelta=input("Con che metodo vuoi pagare\n1 - Contanti\n2 - Carta di credito\n3 - Assegno\n4 - Lava piatti\n")
				if scelta=="2":
					ncarta=input("Inserisci il numero della carta: ")
					scadenza=input("Inserisci la scadenza: ")
					cvv=input("Inserisci il CVV: ")
				print("Grazie per essere stati al ristorante da Hoxha")
				exit(0)

		while scelta=="1" :
			os.system('clear')
			print("--------------------------------------------------------------------------------")
			print(Polpoverace[0], "-----> €17\n")
			print(Truciolidiseppia[0], "-----> €17\n")
			print(Gambericroccanti[0], "-----> €18\n")
			print(AlicidelCantabrico[0], "-----> €18\n")
			print(Tartare[0], "-----> €20\n")
			print(Crudodinverno[0], "-----> €20\n")
			print(Trigliadiscoglio[0], "-----> €22\n")
			print("--------------------------------------------------------------------------------")
			scelta=input("\nScrivi 2 per vedere gli ingredienti \n\nScrivi 3 per tornare al menù precedente: ")
			while scelta=="2":
				os.system('clear')
				print("--------------------------------------------------------------------------------")
				print (Polpoverace[0], ":", Polpoverace[1], "\n")
				print (Truciolidiseppia[0], ":", Truciolidiseppia[1], "\n")
				print (Gambericroccanti[0], ":", Gambericroccanti[1], "\n")
				print (AlicidelCantabrico[0], ":", AlicidelCantabrico[1], "\n")
				print (Tartare[0], ":", Tartare[1], "\n")
				print (Crudodinverno[0], ":", Crudodinverno[1], "\n")
				print (Trigliadiscoglio[0], ":", Trigliadiscoglio[1], "\n")
				print("--------------------------------------------------------------------------------")
				scelta=input("\nScrivi il nome del piatto che vuoi ordinare: ")
				if scelta=="Polpo verace":
					somma=int(somma)+17
				if scelta=="Trucioli di seppia":
					somma=int(somma)+17
				if scelta=="Gamberi croccanti":
					somma=int(somma)+18
				if scelta=="Alici del Cantabrico":
					somma=int(somma)+18
				if scelta=="Tartare":
					somma=int(somma)+20
				if scelta=="Crudo d'inverno":
					somma=int(somma)+20
				if scelta=="Triglia di scoglio":
					somma=int(somma)+22
				scelta=input("Premi 1 per tornare al menù precedente \n\nPremi 2 per scegliere un altro antipasto: ")

		while scelta=="2":
			os.system('clear')
			print("--------------------------------------------------------------------------------")
			print(Gnocchi[0], "-----> €16\n")
			print(Zucca[0], "-----> €16\n")
			print(MilanoRoma[0], "-----> €18\n")
			print(BurroEAlici[0], "-----> €18\n")
			print(CarbonaraOroNero[0], "-----> €20\n")
			print(PolloRuspanteAlGirarrosto[0], "-----> €20\n")
			print(PescatoDelGiorno[0], "-----> €22\n")
			print(FilatoDiFassone[0], "-----> €17\n")
			print("--------------------------------------------------------------------------------")
			scelta=input("\nScrivi 1 per vedere gli ingredienti \nScrivi 3 per tornare al menù precedente: ")
			while scelta=="1":
				os.system('clear')
				print(Gnocchi[0], ":", Gnocchi[1], "\n")
				print(Zucca[0], ":", Zucca[1], "\n")
				print(MilanoRoma[0], ":", MilanoRoma[1], "\n")
				print(BurroEAlici[0], ":", BurroEAlici[1], "\n")
				print(CarbonaraOroNero[0], ":", CarbonaraOroNero[1], "\n")
				print(PolloRuspanteAlGirarrosto[0], PolloRuspanteAlGirarrosto[1], ":" )
				print(PescatoDelGiorno[0], ":", PescatoDelGiorno[1], "\n")
				print(FilatoDiFassone[0], ":", FilatoDiFassone[1], "\n")
				scelta=input("\nScrivi il nome del piatto che vuoi ordinare: ")
				if scelta=="Gnocchi":
					somma=int(somma)+16
				if scelta=="Zucca":
					somma=int(somma)+16
				if scelta=="Milano Roma":
					somma=int(somma)+18
				if scelta=="Burro e Alici":
					somma=int(somma)+18
				if scelta=="Carbonara oro nero":
					somma=int(somma)+20
				if scelta=="Pollo ruspante al girarrosto":
					somma=int(somma)+20
				if scelta=="Pescato del giorno ":
				 somma=int(somma)+22
				if scelta=="Filato di fassone":
				    somma=int(somma)+17
				scelta=input("Premi 2 per tornare al menù precedente \n\nPremi 1 per scegliere un altro primo piatto: ")

			while scelta=="3":
				os.system('clear')
				print("--------------------------------------------------------------------------------")
				print([0], "Margherita-----> €16\n")
				print([0], "Pugliese-----> €16\n")
				print([0], "Wurstel-----> €18\n")
				print([0], "SalaminoPiccante-----> €18\n")
				print([0], "Zucchine-----> €20\n")
				print([0], "Melanzane-----> €20\n")
				print([0], "Romana-----> €22\n")
				print([0], "Caprese-----> €17\n")
				print("--------------------------------------------------------------------------------")
				scelta=input("\nScrivi 1 per vedere gli ingredienti \nScrivi 3 per tornare al menù precedente: ")
				while scelta=="1":
					os.system('clear')
					print(Margherita[0], ":", Margherita[1], "\n")
					print(Pugliese[0], ":", Pugliese[1], "\n")
					print(Wurstel[0], ":", Wurstel[1], "\n")
					print(SalaminoPiccante[0], ":", SalaminoPiccante[1], "\n")
					print(Zucchine[0], ":", Zucchine[1], "\n")
					print(Melanzane[0], ":", Melanzane[1], ":" )
					print(Romana[0], ":", Romana[1], "\n")
					print(Caprese[0], ":", Caprese[1], "\n")
					scelta=input("\nScrivi il nome del piatto che vuoi ordinare: ")
					if scelta=="Margherita":
						somma=int(somma)+16
					if scelta=="Pugliese":
						somma=int(somma)+16
					if scelta=="Wurstel":
						somma=int(somma)+18
					if scelta=="Salamino piccante":
						somma=int(somma)+18
					if scelta=="Zucchine":
						somma=int(somma)+20
					if scelta=="Melanzane":
						somma=int(somma)+20
					if scelta=="Romana":
					 somma=int(somma)+22
					if scelta=="Caprese":
						somma=int(somma)+17
					scelta=input("Premi 3 per tornare al menù precedente \n\nPremi 1 per scegliere un altra pizza: ")

			while scelta=="4":
				os.system('clear')
				print("--------------------------------------------------------------------------------")
				print([0], "-----> €16\n")
				print([0], "-----> €16\n")
				print([0], "-----> €18\n")
				print([0], "-----> €18\n")
				print([0], "-----> €20\n")
				print([0], "-----> €20\n")
				print([0], "-----> €22\n")
				print([0], "-----> €17\n")
				print("--------------------------------------------------------------------------------")
				scelta=input("\nScrivi 1 per vedere gli ingredienti \nScrivi 3 per tornare al menù precedente: ")
				while scelta=="1":
					os.system('clear')
					print([0], ":", [1], "\n")
					print([0], ":", [1], "\n")
					print([0], ":", [1], "\n")
					print([0], ":", [1], "\n")
					print([0], ":", [1], "\n")
					print([0], ":", [1], ":" )
					print([0], ":", [1], "\n")
					scelta=input("\nScrivi il nome del piatto che vuoi ordinare: ")
					if scelta=="":
						somma=int(somma)+16
					if scelta=="":
						somma=int(somma)+16
					if scelta=="":
						somma=int(somma)+18
					if scelta=="":
						somma=int(somma)+18
					if scelta=="":
						somma=int(somma)+20
					if scelta=="":
						somma=int(somma)+20
					if scelta=="":
					 somma=int(somma)+22
					scelta=input("Premi 3 per tornare al menù precedente \n\nPremi 1 per scegliere un altro dolce: ")

				while scelta=="5":
					os.system('clear')
					print("--------------------------------------------------------------------------------")
					print([0], "-----> €16\n")
					print([0], "-----> €16\n")
					print([0], "-----> €18\n")
					print([0], "-----> €18\n")
					print([0], "-----> €20\n")
					print([0], "-----> €20\n")
					print([0], "-----> €22\n")
					print([0], "-----> €17\n")
					print("--------------------------------------------------------------------------------")
					scelta=input("\nScrivi 1 per vedere gli ingredienti \nScrivi 3 per tornare al menù precedente: ")
					while scelta=="1":
						os.system('clear')
						print([0], ":", [1], "\n")
						print([0], ":", [1], "\n")
						print([0], ":", [1], "\n")
						print([0], ":", [1], "\n")
						print([0], ":", [1], "\n")
						scelta=input("\nScrivi il nome del piatto che vuoi ordinare: ")
						if scelta=="":
							somma=int(somma)+16
						if scelta=="":
							somma=int(somma)+16
						if scelta=="":
							somma=int(somma)+18
						if scelta=="":
							somma=int(somma)+18
						if scelta=="":
							somma=int(somma)+20
						scelta=input("Premi 3 per tornare al menù precedente \n\nPremi 1 per scegliere un altra bevanda: ")
InfoGenerali()
