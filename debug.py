# debug.py
import csv
import characters
import hero
import shops
# user input macro
##while 1:
## [statements]	

Location = "gulden"

def debug():
	# create a grue
	monster = create_monster('Grue')
	characters.fight(hero.user, monster)
	monster = create_monster('Llama')
	characters.fight(hero.user, monster)
	shops.shop(Location, "Stock Exchange")
	return('Start Menu')
		
def create_monster(Name):
	with open('bestiary.csv', 'r') as bestiary:
		bestiary_csv = csv.reader(bestiary)
		for row in bestiary_csv:
				if row[0] == Name:
					HP = int(row[1])
					Strength = int(row[2])
					Vitality = int(row[3])
					break;
	return characters.character(Name, HP, Strength, Vitality, 0, 'MAS', 'MAS') # lazy: not sure if monsters have shares yet. use M&S until then