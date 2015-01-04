# -*- coding: utf-8 -*-
import sys
import os
import pickle
import sqlite3

class Dish(object):
    def __init__(self, name, category, mainIngredient, taste, effect, ingredients):
        self.name = name
        self.category = category
        self.mainIngredient = mainIngredient
        self.taste = taste
        self.ingredients = ingredients
        self.effect = effect

    def display(self):
        return '菜名:%s\n类型:%s\n主要成分:%s\n味道:%s\n功效:%s\n原料:%s\n'.decode('utf-8') % (
                self.name,
                self.category,
                self.mainIngredient,
                self.taste,
                self.effect,
                ','.join(self.ingredients)) + '-' * 80

    def __str__(self):
        return "'%s', '%s', '%s', '%s', '%s', '%s'" % (
                self.name,
                self.category,
                self.mainIngredient,
                self.taste,
                self.effect,
                '$%s$' % '$'.join(self.ingredients))

    def getIngredients(self):
        pass

    def match(self, fact):
        pass

    def isMatchedIngredients(self, ingredient):

    @staticmethod
    def parse(str_):
        fields = str_.split()
        return Dish(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5:])

    @staticmethod
    def assemble(fields):
        return Dish(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5][1:-1].split('$'))

class KnowledgeBase(object):
    def add(self, item):
        pass


class PickleKnowledgeBase(KnowledgeBase):
    def __init__(self, fname):
        if not os.path.isfile(fname):
            self.content = []
        else:
            self.file_ = open(fname, 'r')
            self.content = pickle.load(self.file_)

    def add(self, item):
        self.content.append(item)

    def dump(self):
        self.file_ = open(fname, 'w+')
        pickle.dump(self.content, self.file_)

    def list(self):
        for item in self.content:
            yield item.display()

class Sqlite3KnowledgeBase(KnowledgeBase):
    def __init__(self, dbname, tablename):
        self.conn = sqlite3.connect(dbname)
        self.tablename =  tablename

    def add(self, item):
        c = self.conn.cursor()
        c.execute("insert into %s VALUES (%s)" % (self.tablename, str(item)))

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def list(self):
        c = self.conn.cursor()
        c.execute("select * from %s" % self.tablename)
        for result in c:
            yield Dish.assemble(result)

    def getItemList(self):
        pass

if __name__ == '__main__':
    # kb = PickleKnowledgeBase(sys.argv[1])
    kb = Sqlite3KnowledgeBase(sys.argv[1], sys.argv[2])
    while True:
        try:
            item = Dish.parse(raw_input('>'))
        except EOFError:
            # kb.dump()
            break
        kb.add(item)

    for item in kb.list():
        print item.display()
    kb.commit()
    kb.close()


