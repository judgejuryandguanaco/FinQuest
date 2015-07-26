#main.py
import sys


import statemachine
import stockmarket
import characters
from yahoo_finance import Share
import hero

import site

# Geographical locations
# import gulden
import debug

def start_menu():
	options = ('New Game (n)', 'Load (l)', 'Options (o)', 'Exit (e)')
	option_chars = {'n', 'l', 'o', 'e'}
	print(options)
	while 1:
		selection = input()
		if selection in option_chars: break;
	if selection is 'n': nextState = 'New Game'
	if selection is 'l': nextState = 'Load Menu'
	if selection is 'o': nextState = 'Option Menu'
	if selection is 'e': nextState = 'Exit'
	return(nextState)
	
def new_game():
	# preprocessor statement thing? if debug then this, otherwise normal option
	# Create your character
	hero.user = characters.generate_character()
	# Go to DEBUG ROOM
	return('Debug')

def load_menu():
        return('Start Menu')

def option_menu():
        return('Start Menu')
	
def done_here():
		exit()
		#sys.exit
	
def unpack_states():
	machine.add_state('Start Menu', start_menu)
	machine.add_state('Load Menu', load_menu)
	machine.add_state('Option Menu', option_menu)
	machine.add_state('Exit', done_here)
	machine.add_state('New Game', new_game)
	machine.add_state('Debug', debug.debug)
	
if __name__ == "__main__":
	machine = statemachine.StateMachine()
	unpack_states()
	
	title = open('title_logo.txt', 'r')
	print(title.read())
	
	machine.set_start('Start Menu')
	machine.run()
