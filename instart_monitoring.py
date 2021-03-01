''' server-monitoring'''
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import datetime
import psutil
import pymysql
import schedule
import daemon
import select_monitoring

dc = daemon.DaemonContext(stdout=sys.stdout)

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

def job():
    '''
    jobの設定
    例えば,データベースを消去するとか...
    '''
    print(datetime.datetime.now())
    print("プログラムを実行します.")
    select_monitoring.select()

def Regular():
    '''
    マルチプロセスである時間の時に処理を行うためのプログラム
    '''
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()


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
        mem_percent=(mem.used/mem.total)*100
        dsk = psutil.disk_usage('/')
        dsk_used=dsk.used
        dsk_total=dsk.total
        cpu=psutil.cpu_percent()
        con=db_connect()
        cur = con.cursor()
        query="INSERT INTO monitoring (time,mem_used,mem_total,dsk_used,dsk_total,cpu,mem_percent) \
            VALUES (%s,%s,%s,%s,%s,%s,%s) ;"
        cur.execute(query, (now_time,mem_used,mem_total,dsk_used,dsk_total,cpu,mem_percent))
        con.commit()
        cur.close()
        con.close()
        time.sleep(p_stoptime)

with dc:
    stop_time=hiki()
    p_stoptime= stop_time
    #システムのマルチプロセス化とデーモン化
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(main)
    executor.submit(Regular)
