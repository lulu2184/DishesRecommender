# -*- coding: utf-8 -*-
import sys
import os
import pickle

class Dish(object):
    def __init__(self, name, category, mainIngredient, taste, effect, ingredients):
        self.name = name
        self.category = category
        self.mainIngredient = mainIngredient
        self.taste = taste
        self.ingredients = ingredients
        self.effect = effect

    def __str__(self):
        return '菜名:%s\n类型:%s\n主要成分:%s\n味道:%s\n功效:%s\n原料:%s\n' % (
                self.name,
                self.category,
                self.mainIngredient,
                self.taste,
                self.effect,
                ','.join(self.ingredients)) + '-' * 80

    def GetIngredients(self):
        pass

    def match(self, fact):
        pass

    def matchIngredient(self, ingredient):
        pass

    @staticmethod
    def load(str_):
        fields = str_.split()
        return Dish(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5:])


class KnowledgeBase(object):
    def __init__(self):
        self.content = []

    def add(self, item):
        pass

    def list(self):
        for item in self.content:
            print item

    def GetList(self):
        pass


class PickleKnowledgeBase(KnowledgeBase):
    def __init__(self, fname):
        if not os.path.isfile(fname):
            self.file_ = open(fname, 'w+')
            self.content = []
        else:
            self.file_ = open(fname, 'r')
            self.content = pickle.load(self.file_)
            self.file_.close()
            self.file_ = open(fname, 'w')

    def add(self, item):
        self.content.append(item)

    def dump(self):
        pickle.dump(self.content, self.file_)

if __name__ == '__main__':
    kb = PickleKnowledgeBase(sys.argv[1])
    while True:
        try:
            item = Dish.load(raw_input('>'))
        except EOFError:
            kb.dump()
            break
        kb.add(item)

