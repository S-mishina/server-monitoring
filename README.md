# server-monitoring
## 使用ライブラリ

time<br>
sys<br>
datetime<br>
psutil<br>
pymysql<br>

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
    con = pymysql.connect(
            host='127.0.0.1',//IPアドレス
            user='root',//user名
            password='root',//pass
            db='seerver_m',//データベース名
            port= 13306,//ポート指定
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
```
## 実行方法
```
python test.py 秒数
EX）
python test.py 60 //秒数
```
引数を設定しない場合には60秒で実行するように変更.
