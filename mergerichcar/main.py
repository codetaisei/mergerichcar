from re import A, search
from tkinter import S
from turtle import position
from unittest import result
import android_auto_play_opencv as am
import math
import random


adbpath = '/Users/ogawa/Library/Android/sdk/platform-tools/'
aapo = am.AapoManager(adbpath)
IMG_PATH = "./img"

TIME_RANGE = 0.3
TAP_RANGE = 20
SWIPE_RANGE = 20

# 待機時間のランダム化
# def random(x, y):

def rand(data, max): 
    if type(max) == float:
        return data + random.uniform(0, max) # float
    if type(max) == int:
        return data + random.randint(0, max) # int

# タップ
def tap(x, y): 
    sleep(0)
    aapo.touchPos(rand(x, TAP_RANGE), rand(y, TAP_RANGE))

# スワイプ
def swipe(x1, y1, x2, y2, time): aapo.swipeTouchPos(rand(x1, SWIPE_RANGE), rand(y1, SWIPE_RANGE), rand(x2, SWIPE_RANGE), rand(y2, SWIPE_RANGE), int(rand(time, TIME_RANGE*1000)))

# 座標検索（1つ）
def search(num):
    aapo.screencap()
    result, x, y = aapo.chkImg2(f'{IMG_PATH}/{num}.jpg')  # 画像認識
    return result, x, y

# 座標検索（複数）
def search_multi(num):
    aapo.screencap()
    result, data = aapo.chkImg2(f'{IMG_PATH}/{num}.jpg', _multi=True)  # 画像認識
    return result, data

# 待機
def sleep(time):
    aapo.sleep(rand(time, TIME_RANGE))


# =====================================================================================================
# 合成
def tint():
    for i in range(6):

        sleep(0.3)

        num = 54 + i  # 54から検索

        result, data = search_multi(num)


        print(f'-------------({num}番)------------')

        if num == 57: del data[-1]  # 57の時に最後のリストアイテムを削除する

        # 戻り値からTrueかつリストが空でない場合
        if result and not len(data) == 0:


            print(f'{len(data)}個発見！！！！！')

            cnt = 0
            for h in range(math.floor(len(data)/2)):

                swipe(data[0+cnt][0], data[0+cnt][1], data[1+cnt][0], data[1+cnt][1], 500)
                cnt = cnt + 2
        
        if num == 59 and len(data) >= 2:
            sleep(7)
            tap(550, 1460)
            sleep(5)
            

# SHOP
def shop():
    tap(650, 1700)
    result, x, y = search("shop")
    print(result)
    if result:
        swipe(545, 570, 545, 870, 500) # 54が見えるまでスワイプ
        tap(545, 1900) # スワイプを止める
        sleep(0.5)
        result, x, y = search("54-price")
        for i in range(12):  # 購入
            tap(x, y)
            
        tap(950, 450) # SHOPを出る
        sleep(1)
        swipe(770, 1500, 870, 1500, 100) # 手を消すためにスワイプ

def gem():
    result, x, y = search("gem")
    if result:
        tap(420, 690)
        tap(830, 1130)
        tap(540, 1470)
        sleep(0.5)
        tap(670, 720)

def main():
    
    while True:

        # gem()
        tint()
        shop()
        
        # return False

if __name__ == '__main__':
    main()
