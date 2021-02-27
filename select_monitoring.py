import pymysql

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
con=db_connect()
cur = con.cursor()
query="select * From monitoring ;"
cur.execute(query)
test = cur.fetchall()
cur.close()
con.close()
print(test[1]['time'])
print(test[1]['mem_used'])