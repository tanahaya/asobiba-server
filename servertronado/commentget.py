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
#
#cur.execute("""SELECT title FROM comment;""")
#for title in cur.fetchall() :
#    titlenubmer.append(title)


print data

# order by price desc
conn.commit()
conn.close()


class MainHandler(tornado.web.RequestHandler):
    def post(self):
#        self.write(data)
         comment = self.get_argument('comment')
         print comment



application = tornado.web.Application([(r"/", MainHandler),])
if __name__ == "__main__":
    application.listen(10001)
    tornado.ioloop.IOLoop.instance().start()
