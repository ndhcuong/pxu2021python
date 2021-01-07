import numpy as np

a = [1,2,3,4,5]
print(a)
#Tạo ma trận - dạng vector (đặc biệt) có 5 chiều
vector = np.array([1, 2, 3, 4, 5])
print(vector)

#Tạo ma trận vuông 5x5
matrix5x5 = np.array([[1, 2, 3, 4, 5],
                      [6,7,8,9,0],
                      [11,12,13,14,15],
                      [1,2,3,4,5],
                      [4,5,6,7,8]])
print(matrix5x5)

#Số chiều của ma trận
print(vector.ndim)
print(matrix5x5.ndim)

#Tính tích 2 matran 3x4 4x3
A = np.array([[1,2,3,4],
              [1,2,3,4],
              [1,2,3,4]])

B = np.array([[1,2,3],
              [2,3,4],
              [3,4,5],
              [4,5,6]])

C = A.dot(B)
print(C)

#Chuyển vị ma trận
D = C.transpose()
print(D)