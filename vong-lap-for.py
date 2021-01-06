a = [('Hung', 18), ('Tuan', 20), ('Quang', 21)]

print("Kieu lap thu nhat")
for item in a:
    print(item)
print('-----------------')
print('Kieu lap thu 2')
for idx, (name, age) in enumerate(a):
    print(name, '--', age)
print('-----------------')