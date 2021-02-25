''' server-monitoring'''
import time
import datetime
import psutil
import pymysql
def instartdb(time1,mem_used,mem_total,disk_used,disk_total):
    '''
    instartdb はサーバの状態を取得してdbに出力する為の機能
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
    con.ping(reconnect=True)
    cur = con.cursor()
    query="INSERT INTO monitoring (time,mem_used,mem_total,dsk_used,dsk_total) \
        VALUES (%s,%s,%s,%s,%s) ;"
    cur.execute(query, (time1,mem_used,mem_total,dsk_used,dsk_total))
    con.commit()
    cur.close()
    con.close()
while True:
    time.sleep(60)
    dt_now = datetime.datetime.now()
    time1=dt_now.strftime('%H:%M')
    mem = psutil.virtual_memory()
    mem_used=mem.used
    mem_total=mem.total
    dsk = psutil.disk_usage('/')
    dsk_used=dsk.used
    dsk_total=dsk.total
    instartdb(time1,mem_used,mem_total,dsk_used,dsk_total)
    