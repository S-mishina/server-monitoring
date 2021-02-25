import time
import psutil
import datetime

while True:
    # メモリ容量を取得
    time.sleep(60)
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%H:%M'))
    mem = psutil.virtual_memory() 
    print((mem.used/mem.total)*100)
