# coding:utf-8
#print("hello")

import numpy as np
import math

dBref = 2e-5


#リニア値からdBへ変換
def db(a1):
    y1 = 20 * np.log10(a1 / dBref)
    return y1


def p(a1):
   y1 = dBref * np.power(10, a1 / 20) #変換式
   return y1                   #リニア値を返す

#######################################
print("==============")
print("dB変換式: 𝑆𝑃𝐿𝑑𝐵 = 20𝑙𝑜𝑔10{𝑆𝑃𝐿𝑖𝑛𝑑 / 𝐵𝑟𝑒𝑓}")
print("dB逆変換式: 𝑆𝑃𝐿𝑖𝑛 = 𝑑𝐵𝑟𝑒𝑓 * 10{𝑆𝑃𝐿𝑑𝐵 / 20}")
print("==============")
print("a1 = 1, dBref = 2e-5のとき")
print("==============")

#######################################
y_db = db(1)
print("dB表示")
print(y_db)

print("==============")
print("パワー表示")
y_pw = p(1)
print(y_pw)

print("==============")
print("リニア値表示")
# dB -> power
print(p(y_db))



#round(y_db, 2)
#第１引数に丸めたい小数
#第２引数に丸めたい桁
