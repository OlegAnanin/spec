def f2():
    from itertools import product
    print('x y z w')
    nums=product('01',repeat=4)
    for i in nums:
        x,y,z,w=i[0],i[1],i[2],i[3]
        if (not(y<=x) or (z<=w) or not(z))==False:
            print(x, y, z, w)

def f5():
    for i in range(1,100):
        num=(bin(i)[2:])
        if num.count('1')%2==0:
            chislo='10'+num[2:]+'0'

        if num.count('1')%2!=0:
            chislo='11'+num[2:]+'1'
        if int(chislo,2)>40:
            print (i, int(chislo,2))
            break

def f6():
    #from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(2)
    done()

def f8():
    from itertools import product
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    nums=product('01234567',repeat=5)
    for n in nums:
        numb=''.join(n)
        if numb.count('6')==1 and numb[0]!='0':
            if all(not(x in numb) for x in nn):
                k+=1
    print(k)

def f12():
    for n in range(4, 10000):
        s = '5' + n*'2'
        while '52' in s or '2222' in s or '1122' in s:
            s = s.replace('52','11',1)
            s = s.replace('2222','5',1)
            s = s.replace('1122','25',1)
        if sum(map(int, s)) == 64:
            print(n)
def f16():
    #sys.setrecursionlimit(2500)
    itog1=itog2=1
    for x1 in range(1,2024):
       itog1=itog1*x1
    for x2 in range(1,2021):
       itog2=itog2*x2
    print(itog1/itog2)

def f162():
    def F(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n > 1:
            return F(n - 1) * F(n - 2) + 1
    print(F(6))
    #https://www.youtube.com/watch?v=hX0nGyja4gA 27:33

def f163():
    def f(n):
        if n > 2024:
            return n
        else:
            return n * f(n + 1)
    print(f(2022) / f(2024))


def f17():
    with open('17_4705.txt') as f:
        nums=[int(x) for x in f]
        maxi=[]
        s=[]
       
        for i in range(len(nums)):
          if nums[i]%10==3:
             maxi.append(nums[i])
        maximum=0
        for i in range(len(nums)-1):
            a=abs(nums[i])%10
            b=abs(nums[i+1])%10
            if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
                if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
                    s.append(nums[i]+nums[i+1])
                    if nums[i]**2+nums[i+1]**2>maximum:
                        maximum=nums[i]**2+nums[i+1]**2
    print(len(s), maximum)

def f192021():
    def f(a,m):
        if a>77: return m%2==0
        if m==0: return 0
        actions=(a+1),(a+4),(a*4)
        steps=[f(a,m-1) for a in actions]
        if m%2==0: return all(steps)
        else: return any(steps)

        s20=[s for s in range(1,78) if not f(s,1) and f(s,3) ]
        print(s20)

        s21=[s for s in range(1,78) if f(s,4) ]
        print(min(s21))

def f23():
    def f(x,y):
        if x>y or x==17:
            return 0
        elif x==y:
            return 1
        return f(x+1,y) +f(x*2,y)
    print(f(1,10)*f(10,35))

def f24():
    #файл с компегэ  № 4710 Демоверсия 2023 (Уровень: Базовый)
    with open('24_4710.txt') as f:
        s=f.readline().replace('C','S').replace('D','S').replace('F','S')
        s=s.replace('A','G').replace('O','G')
        s=s.replace('SG','*')
        k=kmax=0
        for i in s:
            if i=='*':
                k+=1
                kmax=max(k,kmax)
            else:k=0
    print(kmax)

def f25():
    for i in range(2023,10**10,2023):
        num=str(i)
        if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
            print(i,i//2023)
def f251():
    for i in range(2025,10**10,2024):
        if re.match('^1.2157.*4$',str(i)):
            print(i,i//2024)
def f252():
    for i in range(2025,10**10,2024):
    num=str(i)
    if fnmatch.fnmatch(num,"1?2157*4"):
        print(i,i//2024)


#24
'''
import re
'''
#20.06
import re
pat = re.compile(r'[1-9A-F][0-9A-F]+')
m = pat.findall(open("24_9791.txt").readline())
print(m[:5])
print(len(max(m,key=len)))
'''
'''
#27.06
pat = re.compile(r'((8|9)?([ABC][89])+(A|B|C)?)')
m = pat.findall(open("24_9845.txt").readline())
m=[x[0] for x in m]
print(m[:5])
print(len(max(m,key=len)))
print(max(m,key=len))
'''

'''
#16.12
pat = re.compile(r'(((SQ|Q|)?(RSQ)+(RS|R)?))')
m = pat.findall(open("24_12254.txt").readline())
m=[x[0] for x in m]
print(m[:5])
print(len(max(m,key=len)))
print(max(m,key=len))
'''
'''
(?<=abc).+
.+(?=123)
'''

'''
#Поляков генератор 5646
#((?<=KK).+43\d\d78\d\d\d34.+(?=KK))
pat = re.compile(r'(?<=KK).+(43\d\d78\d\d\d34).+(?=KK)')
m = pat.findall(open("24-230.txt").readline())
m = [int(x) for x in m]
print(m[:10])
#p = [x for x in m if x%2!=0]
p=1
for x in m:
    if x%2!=0:
        p = p*x
print(p)
'''



#10105 Демоверсия 2024
#(?=(([^T]*[T]){101}))
pat = re.compile(r'(?=(([^T]*[T]){101}))')
m = pat.findall(open("24_10105.txt").readline())
m=[x[0] for x in m]
print(len(max(m,key=len))-1)
'''





