import pymysql
import numpy as np
import matplotlib.pyplot as plt

def db_connect():
    '''
    データベース設定
    '''
    con = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            db='seerver_m',
            port= 13306,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    return con

def select():
    con=db_connect()
    cur = con.cursor()
    query="SELECT avg(cpu),avg(mem_percent) FROM monitoring;"
    cur.execute(query)
    test = cur.fetchall()
    cur.close()
    con.close()
    print("cpu(avg):"+str(round(test[0]['avg(cpu)']))+"%")
    print("mem(avg)"+str(round(test[0]['avg(mem_percent)']))+"%")
    
if __name__ == '__main__':
    select()
    