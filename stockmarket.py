import yahoo_finance

#Create the mechanicals to buy and sell
#Shops in different towns should be customisable: what they sell? what the shopkeeper says?

def create_shop(Location, Name):
	with open('shops.csv', 'r') as shops:
		shops_csv = csv.reader(shops)
		for row in shop_csv:
				if row[0] == Location:
					if row[1] = Name
						# Load vital stats of shop
						row[2] = Type # stock market? potion shop?
					break;
	return characters.character(Name, HP, Strength, Vitality, 0, 'MAS', 'MAS') # lazy: not sure if monsters have shares yet. use M&S until then


def create_ftse100():
	ftsefile = open(ftse100.csv, 'r')

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