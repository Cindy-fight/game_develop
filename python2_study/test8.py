#!/usr/bin/env python
#！-*- coding:UTF-8 -*-
'''
此文件相关内容有：CGI编程

'''

from flask import Flask

app = Flask(__name__)
print(__name__)
print(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''
    <html>
    <head>
    <meta charset="utf-8">
    <title>Hello Word - 我的第一个 CGI 程序！</title>
    </head>
    <body>
    <h2>Hello Word!<br/> 我是来自菜鸟教程的第一CGI程序</h2>
    </body>
    </html>
        '''

if __name__ == '__main__':
    app.run()




