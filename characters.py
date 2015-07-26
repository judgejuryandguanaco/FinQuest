from yahoo_finance import *
from decimal import *
import csv
import math

def generate_character():
	# create character
	print("Welcome, brave adventurer!")
	#name = input("What is your name?")
	name = 'mitch'
	print("Ah, I see. So your name is", name, "?")
	#share1 = input("Pick a share.")
	share1 = 'YHOO'
	option1 = Share(share1)
	print("Ah, so you chose", option1.get_info(), "?")
	#share2 = input("Pick a second share")
	share2 = 'MAS'
	option2 = Share(share2)
	print("Ah, so you chose", option2.get_info(), "?")
	return character(name, 100, 10, 10, 100, share1, share2)

class investment(object):
	def __init__(self, name):
		self.data = Share(name)
		self.stat = self.calc_stat()
	def calc_stat(self):
		# Treat the price as a decimal, find the log10 of it and return as a float
		return float(Decimal(self.data.get_price()).log10())
	def get_price(self):
		return self.price
	def get_stat(self):
		return self.stat

class character(object):
	def __init__(self, name, hp, str, vit, cash, share1, share2):
		self.name = name
		self.cash = cash
		self.hp = hp
		self.str = str
		self.str_inv = investment(share1)
		self.str_mul = self.str_inv.get_stat()
		self.vit = vit
		self.vit_inv = investment(share2)
		self.vit_mul = self.vit_inv.get_stat()
	def lose_health(self, loss):
		self.hp -= loss
	def gain_health(self, gain):
		self.hp += gain
	def pay_cash(self, pay):
		self.cash -= pay
	def paid_cash(self, paid):
		self.cash += paid
		
def fight(player, monster):
	n = 1
	print(player.name, '(', player.hp, ')', 'encounters', monster.name, '(', monster.hp, ')')
	while (player.hp > 0 and monster.hp > 0):
		monster_damage = damage_calc(player.str, player.str_mul, monster.vit, monster.vit_mul)
		monster.lose_health(monster_damage)
		player_damage = damage_calc(monster.str, monster.str_mul, player.vit, monster.vit_mul)
		player.lose_health(player_damage)
		print(n, player_damage, player.hp, monster_damage, monster.hp)
		n+=1
		
def damage_calc(strength, strength_multiplier, vitality, vitality_multiplier):
	return round(strength * strength_multiplier) 

def heal_calc(vitality, vitality_multiplier):
	return round(vitality * vitality_multiplier)