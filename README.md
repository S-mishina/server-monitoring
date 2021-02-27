# server-monitoring
## 使用ライブラリ
* time
*  sys
*  datetime
*  daemon
*  psutil
*  pymysql

## メインの機能
<b>サーバのメモリ使用料,ディスク使用料をデータベースに書き込む.

## 現状の仕様
システムを止める時には,プロセス側から落とすこととしている.
```
    dt_now = datetime.datetime.now()
    time1=dt_now.strftime('%H:%M')//時間
    mem = psutil.virtual_memory()
    mem_used=mem.used//メモリ使用料
    mem_total=mem.total//トータルメモリ
    dsk = psutil.disk_usage('/')
    dsk_used=dsk.used//ディスク使用料
    dsk_total=dsk.total//ディスクの容量
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
python test.py 秒数
EX）
python test.py 60 //秒数
```
引数を設定しない場合には60秒で実行するように変更.

## データベースの中身
<img width="473" alt="スクリーンショット 2021-02-26 14 46 15" src="https://user-images.githubusercontent.com/45090872/109260502-90a6f400-7841-11eb-95a4-1d360900015a.png">
