# -*- coding: utf-8 -*-
import sys
from dish import KnowledgeBase
from dish import PickleKnowledgeBase
from dish import Sqlite3KnowledgeBase
from dish import Dish

class InferenceEngine(object):
	def __init__(self, dbname):
		self.base = Sqlite3KnowledgeBase(dbname, 'dishes')
		self.fact = []
		self.fact.append(raw_input('Input the category: '))
		self.fact.append(raw_input('Input the main ingredient: '))
		self.fact.append(raw_input('Input the taste: '))
		self.fact.append(raw_input('Input the effect: '))

	def Initialize(self):
		self.dishList = []
		rawList = self.base.list()
		for dish in rawList:
			if dish.match(self.fact):
				self.dishList.append(dish)
		S = set()
		for dish in self.dishList:
			L = dish.getIngredients()
			S = S | set(L)
		self.IngredientsList = [i for i in S]

	def FindMostOptimal(self):
		minimal = 0xfffffff
		for ingredient in self.IngredientsList:
			cnt = 0
			for dish in self.dishList:
				if dish.isMatchedIngredient(ingredient):
					cnt += 1
			if cnt < minimal:
				condition = ingredient
				minimal = cnt
		if minimal == len(self.dishList):
			return ''
		else:
			return condition

	def CutByCondition(self, condition, yn):
		newList = []
		for dish in self.dishList:
			if yn == dish.isMatchedIngredient(condition):
				newList.append(dish)
		return newList

	def LegalCondition(self, condition):
		return condition != ''

	def Do(self):
		while True:
			condition = self.FindMostOptimal()
			if not self.LegalCondition(condition):
				for dish in self.dishList:
					dish.display()
				break
			T = raw_input('你要吃 %s 吗？ '.decode('utf-8')%(condition.decode('utf-8')))
			self.dishList = self.CutByCondition(condition, T == 'YES');	

if __name__ == '__main__':
	ie = InferenceEngine(sys.argv[1])
	ie.Initialize()
	ie.Do()