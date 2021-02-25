import psutil 

# メモリ容量を取得
mem = psutil.virtual_memory() 
print(mem.used/mem.total)
