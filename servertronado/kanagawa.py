#!python2.6
# -*- coding: utf-8 -*-
import sqlite3
import tornado.ioloop
import tornado.web
import json


jsonStr = {}
conn = sqlite3.connect("test.db")
cur = conn.cursor()
data = {}
num = 0
number = ""

cur.execute("""SELECT name, price, category, Evaluation,shopid FROM shop  WHERE location = '神奈川' order by Evaluation desc limit 10 ;""")
for name, price, category, all_Evaluation,shopid in cur.fetchall() :
    print u"%s はだいたい %s 円でカテゴリーは %s で、評価は　%s　点です" % (name, price,category,all_Evaluation)
    num = num + 1
    number = "shopnum_" + str(num)
    jsonStr['number'] = num
    jsonStr['name'] = name
    jsonStr['price'] = price
    jsonStr['category'] = category
    jsonStr['Evaluation'] = all_Evaluation
    print jsonStr
    data[number] = jsonStr
    jsonStr = {}

# order by price desc
conn.commit()
conn.close()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(data)


application = tornado.web.Application([(r"/", MainHandler),])
if __name__ == "__main__":
    application.listen(10002)
    tornado.ioloop.IOLoop.instance().start()
