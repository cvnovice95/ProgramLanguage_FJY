# _*_ coding:utf-8 _*_
def trangle():
    a=[1]
    n=0
    while True:
        yield(a)
        a.insert(0,0)
        a.insert(len(a),0)
        b=[]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        a=b
        n=n+1
'''
g=trangle()
print(g)
for t in trangle():
    print(t)
'''
g = trangle()
print(next(g))
print(next(g))
print(next(g))
