import random
def binaria(lista,x):
    low=0
    high=len(lista)-1
    i=1
    while low<=high:
        print(f"CICLO {i}")
        i+=1
        mid=round(low+(high-low)/2)
        if lista[mid]==x:
            return mid

        if lista[mid]<x:
            low=mid+1
        else:
            high=mid-1

    return -1

if __name__=='__main__':
    #lista=[2,4,5,7,11,14,17,22]
    lista=list([random.randint(-200000,200000) for x in range(0,1000000)])
    #print(lista)
    #print(len(lista))
    lista=sorted(lista)
    #print(lista)
    print(f'Longitud {len(lista)}')
    x=binaria(lista,22)
    print(f"Hallado en {x}")