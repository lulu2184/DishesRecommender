import sys
from dish import KnowledgeBase
from dish import PickleKnowledgeBase
from dish import Dish

class InferenceEngine(object):
	def __init__(self, ffname, kbfname):
		self.base = KnowledgeBase()
		for line in open(kbfname, 'r'):
			item = Dish.load(line)
			self.base.add(item)
		#define self.facts

	def Initialize(self):
		self.dishList = []
		rawList = self.base.GetList()
		for dish in rawList:
			if dish.match(self.fact):
				self.dishList.append(dish)
		S = set()
		for dish in self.dishList:
			L = dish.GetIngredients()
			S = S | set(L)
		self.IngredientsList = [i for i in S]

	def FindMostOptimal(self):
		minimal = 0xfffffff
		for ingredient in self.IngredientsList:
			cnt = 0
			for dish in self.dishList:
				if dish.matchIngredient(ingredient):
					cnt += 1
			if cnt < minimal:
				condition = ingredient
				minimal = cnt
		if minimal == dishList.size:
			return ''
		else:
			return condition

	def CutByCondition(self, condition):
		newList = []
		for dish in dishList:
			if dish.matchIngredient(condition):
				newList.append(dish)
		return newList

	def LegalCondition(self, condition):
		return condition != ''

	def Do(self):
		while True:
			condition = FindMostOptimal()
			if not self.LegalCondition(condition):
				print self.S
				break
			self.S = self.CutByCondition(condition);	

if __name__ == '__main__':
	ie = InferenceEngine(sys.argv[1], sys.argv[2])
	ie.Initialize()
	ie.Do()