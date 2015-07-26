from yahoo_finance import *
from decimal import *
import csv

def create_ftse100():
	ftsefile = open(ftse100.csv, 'r')
	ftsereader = csv.read(ftsefile, delimiter='	')

class investment(object):
	def __init__(self, name):
		self.data = Share(name)
		self.price = self.data.get_price()
		self.stat = self.calc_stat()
	def calc_stat(self):
		return Decimal(self.price).log10()
	def get_price(self):
		return self.price
	def get_stat(self):
		return self.stat

class character(object):
	def __init__(self, name, hp, str, vit, cash):
		self.name = name
		self.cash = cash
		self.hp = hp
		self.str = str
		self.str_inv = investment('RIO')er
		self.str_mul = self.str_inv.get_stat()
		self.vit = vit
		self.vit_inv = investment('YHOO')
		self.vit_mul = self.vit_inv.get_stat()
	def lose_health(self, loss):
		self.hp -= loss
	def gain_health(self, gain)
		self.hp += gain
		
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