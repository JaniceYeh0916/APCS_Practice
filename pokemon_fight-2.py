# 輸入 0、1、2
# 0 : 火屬性寶可夢
# 1 : 水屬性寶可夢
# 2 : 草屬性寶可夢

# 火系 輸 水系
# 水系 輸 草系
# 草系 輸 火系

# 請選擇你的寶可夢
# 隨機一個對手
# 兩人對戰
# 判斷對方是什麼寶可夢
# 判斷比賽結果

# 解法一-先設定電腦出戰屬性
print('道館挑戰賽-全國大賽')
print('0 : 火屬性寶可夢，1 : 水屬性寶可夢、2 : 草屬性寶可夢')

box1 = int(input('請輸入你的對戰屬性代號:'))
box2 = 0
if box2 == 0:
    if box1 == 0:
        print('平手')
    elif box1 == 1:
        print('獲勝')
    elif box1 == 2:
        print('落敗')
elif box2 == 1:
    if box1 == 1:
        print('平手')
    elif box1 == 2:
        print('獲勝')
    elif box1 == 0:
        print('落敗')
elif box2 == 2:
    if box1 == 2:
        print('平手')
    elif box1 == 0:
        print('獲勝')
    elif box1 == 1:
        print('落敗')
else:
    print('請遵守遊戲規則選擇寶可夢')


# 解法二-隨機選屬性
print('道館挑戰賽-全國大賽')
print('0 : 火屬性寶可夢，1 : 水屬性寶可夢、2 : 草屬性寶可夢')

box1 = int(input('請輸入你的對戰屬性代號:'))
import random
box2 = random.randint(0,2)

if box1 >= 3:
    print('請遵守遊戲規則選擇寶可夢')

if box1 <= 2 and box2 == 0:
    print('電腦是火系的')
    if box1 == 0:
        print('平手')
    elif box1 == 1:
        print('獲勝')
    elif box1 == 2:
        print('落敗')
elif box1 <= 2 and box2 == 1:
    print('電腦是水系的')
    if box1 == 1:
        print('平手')
    elif box1 == 2:
        print('獲勝')
    elif box1 == 0:
        print('落敗')
elif box1 <= 2 and box2 == 2:
    print('電腦是草系的')
    if box1 == 2:
        print('平手')
    elif box1 == 0:
        print('獲勝')
    elif box1 == 1:
        print('落敗')


# 解法三-優化程式碼
print('道館挑戰賽-全國大賽')
print('0 : 火屬性寶可夢，1 : 水屬性寶可夢、2 : 草屬性寶可夢')

box1 = int(input('請輸入你的對戰屬性代號:'))
import random
box2 = random.randint(0,2)

if box1 == box2:
    print('平手')
else:
    if box2 ==0 and box1 == 1:
        print('玩家獲勝')
    elif box2 ==0 and box1 == 2:
        print('玩家落敗')
    elif box2 ==1 and box1 == 0:
        print('玩家落敗')
    elif box2 ==1 and box1 == 2:
        print('玩家獲勝')
    elif box2 ==2 and box1 == 1:
        print('玩家落敗')
    elif box2 ==2 and box1 == 0:
        print('玩家獲勝')
    else:
        print('請遵守遊戲規則')


# 解法四-優化程式碼2
print('道館挑戰賽-全國大賽')
print('0 : 火屬性寶可夢，1 : 水屬性寶可夢、2 : 草屬性寶可夢')

box1 = int(input('請輸入你的對戰屬性代號:'))
import random
box2 = random.randint(0,2)

if box1 == box2:
    print('平手')
elif (box2 ==0 and box1 == 1) or (box2 ==1 and box1 == 2) or (box2 ==2 and box1 == 0):
    print('玩家獲勝')
elif (box2 ==0 and box1 == 2) or (box2 ==1 and box1 == 0) or (box2 ==2 and box1 == 1):
    print('玩家落敗')
else:
    print('請遵守遊戲規則')