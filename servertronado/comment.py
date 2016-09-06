#!python2.6
# -*- coding: utf-8 -*-
import sqlite3
import tornado.ioloop
import tornado.web
import json


conn = sqlite3.connect("test.db")
cur = conn.cursor()
num = 0
titlenubmer = []
data = {}
id = 0

#cur.execute("""SELECT title FROM comment;""")
#for title in cur.fetchall() :
#    titlenubmer.append(title)



#cur.execute("""INSERT INTO comment VALUES(100,'picture','content','','title','hayate','うどん',8)""")
#
data['commentnumber'] = titlenubmer.count

print data

# order by price desc
conn.commit()
conn.close()


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        id = self.get_argument('id')
        self.write("Hello, %s" % id)



application = tornado.web.Application([(r"/", MainHandler),])
if __name__ == "__main__":
    application.listen(10001)
    tornado.ioloop.IOLoop.instance().start()
