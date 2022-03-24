t=int(input())
for i in range(t):
    a,b,c,n=map(int,input().split())
    for i in range(n-3):
        n=a+b+c
        a=b
        b=c
        c=n
    print(n)
