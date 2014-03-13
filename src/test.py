from hearth import *
import hero as H
import minion as M
import effect as E

import sys

def test(func):
	"""
	Testing Suite Wrapper
	"""
	def wrapper(*args, **kwarges):
		log("BEGINNING TEST SUITE FOR %s" % func.__name__)
		for hero in [H.Druid, H.Paladin, H.Hunter, H.Mage, H.Priest, H.Warrior, H.Warlock, H.Shaman, H.Rogue]:
			with RedirectStdStreams(stdout=open("output",'wb'), stderr=None):
				hero, enemy = setupBoard(hero)
			div()
			print "Testing %s" % (hero.name)
			print
			res = func(hero, enemy, **kwarges)
			print
			print "%s passed" % (hero.name)
			div()

		return res
	return wrapper

"""
TESTS
"""

@shutup
def setupBoard(hero):
	enemy = H.Druid()
	hero = hero()
	enemy.enemy = hero
	hero.enemy = enemy
	hero.turnUpdate()
	enemy.turnUpdate()
	return hero, enemy

@test
def attackWithHeroPower(hero,enemy):
	# log(hero, enemy)
	hero.heroPower(enemy)
	hero.attack_(enemy)
	# log(hero, enemy)

@test
def summoningMinion(hero,enemy, minion = M.silver_hand_recruit):
	hero.summon(minion, 0)


if __name__ == "__main__":
	attackWithHeroPower()

	
