from PIL import Image
import numpy as np
import sympy as sp
import random
import math
import sys

C1 = random.randrange(256)
C2 = random.randrange(256)
C3 = random.randrange(256)

# C1, C2, C3 = 255, 255, 255

N_list = []

sys.stdout.write("your number : ")
N = int(input())
d = len(str(N))

fact_dict = sp.factorint(N)
if len(fact_dict) == 1 and N in fact_dict :
    prime_flag = 1
    N_list = list(map(int,str(N)))
    N_list.reverse()
else :
    prime_flag = 0

while len(N_list) < 5 :
    N_list.append(0)

img = Image.open('/home/zzzzzz908/Cat_Z.png')
width, height = img.size
img2 = Image.new('RGBA', (width, height))
img_pixels = np.array([[img.getpixel((x,y)) for x in range(width)] for y in range(height)])

stock_part = []
stock_all = []

print(img_pixels[511][511])
print(np.size(img_pixels))

def paint(place_j,place_i,color) :
    if img_pixels[place_j][place_i][3] == 0 :
        img_pixels[place_j][place_i] = [C1, C2, C3, 255]
    elif color == 0 :
        img_pixels[place_j][place_i] = [255,255,255,255]
    elif color == 1 :
        img_pixels[place_j][place_i] = [250,125,200,255]
    elif color == 2 :
        img_pixels[place_j][place_i] = [250,150, 50,255]
    elif color == 3 :
        img_pixels[place_j][place_i] = [250,250, 50,255]
    elif color == 4 :
        img_pixels[place_j][place_i] = [125,250, 25,255]
    elif color == 5 :
        img_pixels[place_j][place_i] = [ 25,150, 25,255]
    elif color == 6 :
        img_pixels[place_j][place_i] = [ 25,250,225,255]
    elif color == 7 :
        img_pixels[place_j][place_i] = [ 50,200,250,255]
    elif color == 8 :
        img_pixels[place_j][place_i] = [ 25, 75,200,255]
    elif color == 9 :
        img_pixels[place_j][place_i] = [  0,  0,  0,255]

for i in range(height):
    for j in range(width):
        if img_pixels[j][i][0] not in stock_part :
            print(str(img_pixels[j][i]) + " : x = " + str(j) + " : y = " + str(i))
            stock_part.append(img_pixels[j][i][0])
            stock_all.append(img_pixels[j][i])
        if img_pixels[j][i][0] > 200 and img_pixels[j][i][0] != 255 :
            if prime_flag == 0 :
                img_pixels[j][i] = [225,0,0,255] # neck ring
            else :
                paint(j,i,N_list[3])
        elif img_pixels[j][i][0] == 255 :
            if prime_flag == 0 :
                img_pixels[j][i] = [175,0,0,255] # four toes
            else :
                paint(j,i,N_list[1])
        elif img_pixels[j][i][0] == 0 and img_pixels[j][i][3] == 255 :
            if prime_flag == 0 :
                img_pixels[j][i] = [150,0,0,255] # eyes and mouth
            else :
                paint(j,i,N_list[0])
        elif img_pixels[j][i][0] > 145 and img_pixels[j][i][0] < 154 :
            if prime_flag == 0 :
                img_pixels[j][i] = [250,0,0,255] # ears
            else :
                paint(j,i,N_list[4])
        elif img_pixels[j][i][3] != 0 :
            if prime_flag == 0 :
                img_pixels[j][i] = [200,0,0,255] # body
            else :
                paint(j,i,N_list[2])
        elif img_pixels[j][i][3] == 0 :
            paint(j,i,9-N_list[2])

if prime_flag == 1 :
    for h in range(6,len(str(N))+1) :
        if h % 2 == 0 :
            for i in range(244,382) :
                for j in range(12*h+168,12*h+198) :
                    img_pixels[i][j] = [150,75,25,255]
            for i in range(250,376) :
                for j in range(12*h+174,12*h+192) :
                    paint(i,j,N_list[h-1])
        else :
            for i in range(244,382) :
                for j in range(-12*h+300,-12*h+330) :
                    img_pixels[i][j] = [150,75,25,255]
            for i in range(250,376) :
                for j in range(-12*h+306,-12*h+324) :
                    paint(i,j,N_list[h-1])

for y in range(height):
  for x in range(width):
    # 反転した色の画像を作成する
    r,g,b,a = img_pixels[y][x]
    img2.putpixel((x,y), (r,g,b,a))

# img2.show()

if len(str(N)) < 10 :
    img2.save('Cat_0' + str(len(str(N))) + '_' + str(N) + '.png')
else :
    img2.save('Cat_' + str(len(str(N))) + '_' + str(N) + '.png')

if prime_flag == 0 :
    print(str(N) + " = " + str(fact_dict))

N_list.reverse()
print(N_list)
