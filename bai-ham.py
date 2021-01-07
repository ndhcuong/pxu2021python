def tong_tich_hieu_thuong(a, b):
    tong = a + b
    hieu = a  - b
    tich = a*b
    thuong = a/b
    return tong, tich, hieu, thuong

x = 5
y = 7

print(tong_tich_hieu_thuong(x,y))

