def cero(n):
    if('0' in str(n)): return True
    return False

def sumapar(n):
    k = str(n); suma=0
    for i in k:
        if(int(i)%2 ==0): suma+=int(i)
    
    return suma

def sumaimpar(n):
    k=str(n); suma=0
    for i in k:
        if(int(i)%2 != 0): suma+=int(i)
    
    return suma

while(True):
    n=int(input())
    if(n==0): break
    if(n<0): n*=-1
    if(not cero(n)):
        if(sumapar(n)>sumaimpar(n)):
            print(1); continue
    print(0)