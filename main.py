#main.py
import sys


import statemachine
import shops
import characters
from yahoo_finance import Share
import hero

import site

# 
import shops

# Geographical locations
# import gulden
import debug

def start_menu():
	options = {'New Game', 'Load', 'Options', 'Exit'}
	option_chars = {'n', 'l', 'o', 'e'}
	return input_menu(options, option_chars)
	
def input_menu(text, chars):
    for n in text:
		print(text(n), " (", chars(n), ") ")
	
	while 1:
		selection = input()
		if selection in chars: break;
	
	for n in chars:
		if selection is chars[n]: nextState = text[n]
	
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
