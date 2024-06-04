import sys
import time

#obliczyc elementy ciagu fibonacciego do elementu wiekszego od n
def fibonacciSequence(n):
    l=abs(n)
    seq=[]
    seq.append(0)
    seq.append(1)
    i=2
    while(l>=seq[i-2]+seq[i-1]):
        seq.append(seq[i-2]+seq[i-1])
        i+=1
    seq.append(seq[i - 2] + seq[i - 1])
    return(seq)

#znajduje najblizsza podanej liczbie n liczbe z ciagu fibonacciego
def findClosest(n, fib): #fib-tablica z liczbami ciągu fibonacciego
    start = 0 #indeks pierwszego elementu rozwaznej czesci
    end = len(fib)-1 #indeks ostatniego elementu rozwaznej czesci
    result=None
    cont=True

    while cont: #wykonuje sie do znalezienia najblizszej liczby fibonacciego
        #sprawdzic czy liczba znajduje sie na koncach przedzialu
        if fib[start]==n:
            result=fib[start]
            cont=False
        elif fib[end]==n:
            result=fib[end]
            cont=False
        #jesli zostaly do rozwazenia 2 liczby zwrocic blizsza n
        elif ((start-end)==1 or (start-end)==-1):
            if (n-fib[start])<fib[end]-n:
                result=fib[start]
                cont=False
            else:
                result=fib[end]
                cont=False
        #zawezic obszar poszukiwan
        elif (fib[start+(end-start)//2]>=n):
            end=start+(end-start)//2
        else:
            start=start+(end-start)//2

    return result

#znajduje minimalna liczbe liczb fibonacciego w n
def findMinFib(n,fib): #fib-tablica z liczbami ciągu fibonacciego
    k=0
    tmp=0
    l=n
    while(l!=0): #znalezc najblizsza liczbe fibonacciego do l i dodac lub odjac az l==0
        tmp=findClosest(abs(l),fib)
        if l<0:
            l+=tmp
        else:
            l-=tmp
        k+=1

    return(k)

start = time.time()
inp=sys.argv[1]
outp=sys.argv[2]
report=sys.argv[3]

n=[]
#wczytaj liczby z pliku
try:
    file=open(inp,"r")
    lines=file.readlines()
    for line in lines:
        n.append(int(line))
    file.close()
except Exception as e:
    print(e)
    sys.exit()


fib=fibonacciSequence(max(n))

file=open(outp,"w")
file.write("wejscie  - wyjscie\n")
res=[]
for i in n:
    file.write(str(i).ljust(8)+" - "+str(findMinFib(i,fib)).ljust(8)+"\n")
file.close()

end = time.time()

file=open(report,"a")
file.write(inp+";"+outp+";"+str(end-start)+"\n")
file.close()
