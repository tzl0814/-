#coding=utf-8
import matplotlib.pyplot as plt
import sqlite3

import os, os.path
import random
import string
import cherrypy
    
class StringGenerator(object):
    @cherrypy.expose
    def diplayData(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        
        time = []
        temp = []
        humidy = []
        
        ##########打开数据库############
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        print("Opened database successfully")

        cursor = c.execute("SELECT time, temp, humidy  from COMPANY")
        for row in cursor:
            time.append(row[0])
            temp.append(row[1])
            humidy.append(row[2])
        
        print("Operation done successfully")

        #####折线图#####

        plt.plot(time, temp, color='red', label='温度')
        plt.plot(time, humidy, color='blue', label='湿度')

        plt.title('温湿度数据')
        plt.xlabel('湿度')
        plt.ylabel('温度')
        plt.legend()
        plt.savafig('./public/test.png')

        #3.返回客服端
        return '''<html>
                   <body>
                     <form method="get" action="generate"
                         <img src="./static/test.png" alt="Smiley face" width="600" height="400">
                     </form>
                   </body>
                  </html>'''
                
                
        

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port':8800})
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
    print(os.path.abspath(os.getcwd()))
    
conn.close()  