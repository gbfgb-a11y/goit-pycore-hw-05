def caching_fibonacci():
    ceshlist={}
    def fibonacci(numb):
        if numb <= 0:
            return 0
        if numb == 1:
            return 1
        if numb in ceshlist:
            return ceshlist.get(numb)
        else: 
            ceshlist[numb] = fibonacci(numb - 1)+fibonacci(numb-2)
        return ceshlist[numb]
    return fibonacci
f = caching_fibonacci()
print(f(10))