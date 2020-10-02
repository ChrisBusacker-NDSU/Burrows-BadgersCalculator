#A Calculator for the game of Burrows and Badgers to create warbands.
#By: Christopher Busacker Last Update: 10/2/2020
import numpy as np
from tkinter import *

root = Tk()
root.title('Burrows and Badgers Calculator')
root.geometry("525x360")

#Arrays with a lists of Species
#Dimesion one is the type of animal
#Dimesion 2 is the cost in pennies 
#Dimesion 3 is the size of the animal
speciesSmall = np.array([["Mouse","Shrew","Bird (S)","Bat"],
						[24,28,26,27],
						["Small","Small","Small","Small"]])
speciesMed = np.array([["Hedgehog","Squirrel","Mole","Weasel","Cat","Black Rat","Ferret","Rabbit","Toad","Frog","Adder","Bird (M)","Raptor (M)","Hound (M)","Marmot (R)","Green Lizard (R)","Siamese Cat (R)","Tortoise (R)","Platypus (R)"],
						[29,34,30,36,35,33,42,31,52,26,36,30,42,30,28,35,36,25],
						["Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium"]])
speciesLarge = np.array([["Hare","WildCat","Brown Rat","Fox","Otter","Bird (L)","Rapor (L)","Hound (L)","Racoon (R)","Armadillo (R)","Fennec Fox (R)"],
						[53,62,42,43,51,35,50,45,40,62,35],	
						["Large","Large","Large","Large","Large","Large","Large","Large","Large","Large","Large"]])
speciesMass = np.array([["Badger","Beaver","Bird (Ma)","Raptor (Ma)","Hound (Ma)"],
						[65,60,40,64,65],
						["Massive","Massive","Massive","Massive","Massive"]])
#size list
size = ["Small","Medium","Large","Massive",]					
#Array with the different Dens
denList = ["Abandoned Burrow","Ruined Farmstead","Town Building"]
#array with differnt Allegiances
allegiance = ["Royalists","Rogues","Freebeasts","Wildbeasts"]
#Weapons Array
weapon = np.array([["none","one-handed","double-handed","Polearm","Spear","Bow","Crossbow","Sling","Thowing knives","Pistols","Caliver","Blunderbuss"],
					[0,8,13,15,15,15,20,5,8,15,20,20]])
#Armour Array
armour = np.array([["none","light armour","heavy armour","very heavy armour","buckler","light shield","heavy shield"],
					[0,15,25,35,8,12,20]])
#Item array
item = np.array([["none","rope & hook","lucky charm","talisman","mage's focus","mage's pouch","camouflage cloak","scent masker","healing potion","broadhead arrows","bodkins arrows","lead slingshot","superior black powder"],	
					[0,6,15,4,15,10,15,5,5,1,1,1,1]])
#Character Special Array
special = np.array([[],
						[]])
#The max point limit for the warband is 350 points or also known as 350 pennys
maxPointLimit = 350
#Leader of the Warbands info inputs
leader = Label(root, text = "Leader").grid(row = 0, column = 1) #bg = "blue"
leaderName = Label(root, text = "Name").grid(row = 1, column = 0) #bg = "light green"
leaderSize = Label(root, text = "Size").grid(row = 2, column = 0)
leaderRace = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 0)
leaderWeapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 0)
leaderWeapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 0)
leaderArmour1 = Label(root, text = "Armour 1").grid(row = 6,column = 0)
leaderArmour2 = Label(root, text = "Armour 2").grid(row = 7, column = 0)
leaderItem = Label(root, text = "Item").grid(row = 8, column = 0)
leaderSpecial = Label(root, text = "Special").grid(row = 9, column = 0)


def selected(event):
	myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		leaderRaceField = OptionMenu(root, clicked2, *speciesSmall[0], command=selected).grid(row = 3, column = 1)
	elif clicked1.get() == "Medium":
		leaderRaceField = OptionMenu(root, clicked3, *speciesMed[0], command=selected).grid(row = 3, column = 1)
	elif clicked1.get() == "Large":
		leaderRaceField = OptionMenu(root, clicked4, *speciesLarge[0], command=selected).grid(row = 3, column = 1)
	else:
		leaderRaceField = OptionMenu(root, clicked5, *speciesMass[0], command=selected).grid(row = 3, column = 1)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

leaderSizeField = OptionMenu(root, clicked1, *size, command=selected).grid(row = 2, column = 1)

leaderWeapon1Field = OptionMenu(root, clicked6, *weapon[0], command=selected).grid(row = 4, column = 1)
leaderWeapon2Field = OptionMenu(root, clicked7, *weapon[0], command=selected).grid(row = 5, column = 1)
leaderArmour1Field = OptionMenu(root, clicked8, *armour[0], command=selected).grid(row = 6, column = 1)
leaderArmour2Field = OptionMenu(root, clicked9, *armour[0], command=selected).grid(row = 7, column = 1)
leaderItem = OptionMenu(root, clicked10, *item[0], command=selected).grid(row = 8, column = 1)

#myButton = Button(root, text="enter", command=selected)


root.mainloop()
