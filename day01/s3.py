import cv2 
import numpy as np 
import math
#############图形的平移
img = cv2.imread('3.jpg')
# 构造移动矩阵H
# 在x轴方向移动多少距离，在y轴方向移动多少距离
H = np.float32([[1, 0, 50], [0, 1, 25]])
rows, cols = img.shape[:2]
print(img.shape)
print(rows, cols)
res = cv2.warpAffine(img, H, (cols, rows))  # 注意这里rows和cols需要反置，个人感觉这里是一个坑
cv2.imshow('origin_picture', img)
cv2.imshow('new_picture', res)
cv2.waitKey(0)


