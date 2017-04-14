from PIL import Image, ImageDraw, ImageFont
import sys
import random
import codecs

#폰트 키워드 리스트 열기
font_list = ["a바람새B", "NanumBarunGothic","a가을운동회B","HanS Calli","12롯데마트드림Bold","NanumBrush"]

# 키워드 파일 열어, 리스트에 담기
f = codecs.open("keyword.txt", "r", "utf-8")
key = f.readlines()
new_key = []

for keyword in key:
    name = keyword.strip()
    new_key.append(name)

for num in range(0,10): #num이 10번 돌아감
    print("----------------------%d번째 훈련데이터 생성"%(num))
    img = Image.open("C:/PycharmProjects/untitled/Imggenerator/living_500.jpg") #이미지 오픈
    key_num = random.randint(1,15) # 뽑을 키워드 수 랜덤 생성
    selected_key = random.sample(new_key, key_num)  # new_key 리스트에서, 랜덤 수 만큼 키워드수 selected_key list에 담기
    print(selected_key)
    for i in range(0,key_num): # key_num 만큼 글자를 생성해야하니까
        # 키워드, 폰트, 사이즈, 위치 랜덤하게 생성
        matrix500x500 = [[0 for col in range(500)] for row in range(500)] # 500 * 500 이차원 배열 생성
        while True:
            txt = selected_key[i]
            font = random.choice(font_list)
            size = random.randint(15, 50)
            x = random.randint(1, 300)
            y = random.randint(1, 300)
            draw = ImageDraw.Draw(img)
            fnt = ImageFont.truetype("C:/Windows/Fonts/" + str(font) + ".ttf", size)
            txt_inf = draw.textsize(str(txt), font=fnt)
            a = (x, y)
            b = (x + txt_inf[0], y)
            c = (x, y + txt_inf[1])
            d = (x + txt_inf[0], y + txt_inf[1])
            print(txt, (a, b, c, d))

            for txt_i in range(a[0], b[0] + 1):
                for txt_j in range(c[1], d[1] + 1):
                    if matrix500x500[txt_i][txt_j] == 1:continue

            for txt_i in range(a[0], b[0] + 1):
                for txt_j in range(c[1], d[1] + 1):
                    matrix500x500[txt_i][txt_j] = 1

                    draw.text((x, y), str(txt), font=fnt, fill=(0, 0, 0, 0))
                    draw.rectangle((x, y) + (x + txt_inf[0], y + txt_inf[1]), outline="red")
            print((txt, x, y, txt_inf[0],txt_inf[1]))
            del draw
            img.save('C:/PycharmProjects/untitled/Imggenerator/글자/test_' + str(num) + '.jpg')
            break

    print("----------------------%d번째 훈련데이터 생성 완료" % (num))


# 디폴트 박스의 좌표
# a = (x,y)
# b = (x + txt_inf[0],y)
# c = (x,y+txt_inf[1])
# d = (x+txt_inf[0],y+txt_inf[1])

# 다음