import time
scale=50
print("开始打印".center(scale,"="))
start=time.perf_counter()
for i in range(scale+1):
    time.sleep(0.3)
    a="#"*i
    b="-"*(scale-i)
    c=i/scale*100
    end=time.perf_counter()
    print("\r{2:3.0f}%{0}->{1}{3:.2f}S".format(a,b,c,end-start),end="")
print()
print("打印结束".center(scale,"="))

