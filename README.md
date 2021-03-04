


# server-monitoring
* instart_monitoring.py データベース書き込み
* select_monitoring.py データベース取得
# instart_monitoring

## プログラム実行の為のshell
```
#!/bin/sh

nohup python3 instart_monitoring.py $1 &
```
こうすることでsshが落ちてもプログラムは動き続ける.
## 使用ライブラリ
* ThreadPoolExecutor
* schedule
* time
*  sys
*  datetime
*  daemon
*  psutil
*  pymysql
# GUI画面

## メインの機能
<b>サーバのメモリ使用料,ディスク使用料をデータベースに書き込む.

## 現状の仕様
システムを止める時には,プロセス側から落とすこととしている.
```
def job():
    '''
    jobの設定
    例えば,データベースを消去するとか...
    '''
    print(datetime.datetime.now())
    print("I'm working...") 

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
        dsk = psutil.disk_usage('/')
        dsk_used=dsk.used
        dsk_total=dsk.total
        cpu=psutil.cpu_percent()
        con=db_connect()
        cur = con.cursor()
        query="INSERT INTO monitoring (time,mem_used,mem_total,dsk_used,dsk_total,cpu) \
            VALUES (%s,%s,%s,%s,%s,%s) ;"
        cur.execute(query, (now_time,mem_used,mem_total,dsk_used,dsk_total,cpu))
        con.commit()
        cur.close()
        con.close()
        time.sleep(p_stoptime)
```
秒数のデフォルトを変更する.

```
def hiki():
    '''
    プログラム実行時に引数を取得してメインプログラムへ返します.
    '''
    p_h1 = sys.argv
    if(len(sys.argv) <= 1):
        print('デフォルト60秒になります.')
        hikisu = 60 //ここの秒数を変更するとデフォルトが変わる.
        return hikisu
    print(p_h1)
    return hikisu
```
## データベースのリセットについて
毎日23:59分にデータがリセットされるように修正を加える.

```
def job1():
    '''
    jobの設定
    例えば,データベースを消去するとか...
    '''
    print(datetime.datetime.now())
    print("データベース消去を行います")
    con=db_connect()
    cur = con.cursor()
    query="DELETE FROM monitoring;"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()
```

```
def Regular():
    '''
    マルチプロセスである時間の時に処理を行うためのプログラム
    '''
    schedule.every(1).minutes.do(job)
    schedule.every().day.at("23:59").do(job1)#時間の設定をここで行うことができる.
    while True:
        schedule.run_pending()
```

## データベースの設定
```
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
```
## 実行方法
```
python側から実行をかける場合

python test.py 秒数
EX）
python test.py 60 //秒数

shell側から実行をかける場合

#!/bin/sh

nohup python3 instart_monitoring.py $1 &
```
引数を設定しない場合には60秒で実行するように変更.

## データベースの中身
<img width="473" alt="スクリーンショット 2021-02-26 14 46 15" src="https://user-images.githubusercontent.com/45090872/109260502-90a6f400-7841-11eb-95a4-1d360900015a.png">
