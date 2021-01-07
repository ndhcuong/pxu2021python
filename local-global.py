def hoan_doi(x, y):
    tam = x
    x = y
    y = tam
    #print(a)
    return x, y

a = 5
b = 7
print(a, b)
a, b = hoan_doi(a, b)
print(a, b)
#print(tam)