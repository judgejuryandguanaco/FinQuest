import yahoo_finance
import csv
import statemachine

#Create the mechanicals to buy and sell
#Shops in different towns should be customisable: what they sell? what the shopkeeper says?

def shop(Location, Name):
	with open('shops.csv', 'r') as shops:
		shops_csv = csv.reader(shops)
		
		# Search for the row 
		for row in shops_csv:
				if row[0] == Location:
					if row[1] == Name:
						Introduction = row[2]
						Talk = row[3]
						break;
					
	shop_machine = statemachine.StateMachine()
	
	shop_machine.add_state('Introduction', state1(Introduction))
	
	shop_machine.set_start('Introduction')
	shop_machine.run()
	return

def state1(Introduction):
	print(Introduction)
	
	return input_menu(["Talk", "See Items", "Exit"], ["t", "i", "e"])
	
def talk():
	print(Talk)
		
def input_menu(text, chars):
	for n in text:
		print(text[n], " (", chars[n], ') ')
	
	while 1:
		selection = input()
		if selection in chars: break;
	
	for n in chars:
		if selection is chars[n]: nextState = text[n]
	
	return nextState
		
	
# This is the store where you can buy and sell your shares. Currently FTSE100 is accessible. In the future more markets can be added.
class stockmarket:
	def __init__(self):
		self.description = 'The store'
	def buy_stock(player, share_name):
		share_price = Share(share_name).get_price()
		player.pay(share_price)
	def sell_stock(player, share_name):
		share_price = Share(share_name).get_price()
		player.paid(share_price)
	def inspect_stock():
		for row in ftsefile:
			content = list(row[2] for i in included_cols)
		print(content)