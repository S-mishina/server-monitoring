''' server-monitoring'''
import sys
import time
import datetime
import daemon
import psutil
import pymysql

def hiki():
    '''
    秒数指定関数
    '''
    p_h1 = sys.argv
    if(len(sys.argv) <= 1):
        print('デフォルト60秒になります.')
        hikisu = 60
        return hikisu
    else:
        hikisu = int(p_h1[1])
        print(hikisu)
        return hikisu

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

dc = daemon.DaemonContext(stdout=sys.stdout)
stop_time=hiki()
p_stoptime= stop_time
def main():
    '''
    mainプログラム
    '''
    while True:
        dt_now = datetime.datetime.now()
        now_time=dt_now.strftime('%H:%M')
        mem = psutil.virtual_memory()
        mem_used=mem.used
        mem_total=mem.total
        dsk = psutil.disk_usage('/')
        dsk_used=dsk.used
        dsk_total=dsk.total
        print(dsk_total)
        con=db_connect()
        cur = con.cursor()
        query="INSERT INTO monitoring (time,mem_used,mem_total,dsk_used,dsk_total) \
            VALUES (%s,%s,%s,%s,%s) ;"
        cur.execute(query, (now_time,mem_used,mem_total,dsk_used,dsk_total))
        con.commit()
        cur.close()
        con.close()
        time.sleep(p_stoptime)

with dc:
    main()
