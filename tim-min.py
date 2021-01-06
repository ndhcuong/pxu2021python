a = [1,3,5,-9,-15,0, 7,100]
gia_tri_min = a[0]
for item in a:
    if gia_tri_min > item:
        gia_tri_min = item
print('Gia tri nho nhat la: ', gia_tri_min)