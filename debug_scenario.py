# debug_scenario.py
from yahoo_finance import Share
# user input macro
##while 1:
## [statements]	

def debug():
	# create character
	print("Welcome, brave adventurer!")
	name = input("What is your name?")
	print("Ah, I see. So your name is", name, "?")
	share1 = input("Pick a share.")
	option1 = Share(share1)
	print("Ah, so you chose", option1.get_info(), "?")
	share2 = input("Pick a second share")
	option2 = Share(share2)
	print("Ah, so you chose", option2.get_info(), "?")
	name = characters.character(name, 100, 10, 10, 100, Share1, Share2)
	while(1):
		a = 1