'''from PIL import Image, ImageDraw, ImageFont
import time, ctypes
def hex(s):
        n = int(s.lstrip('#'), 16)
        return (n >> 16, (n >> 8) & 0xff, n & 0xff)
print('start')
# Создаем белый квадрат
# Easter Sweet.ttf

font = ImageFont.truetype("C:\\Users\\maste\\Desktop\\Easter Sweet\\Easter Sweet.ttf", size=18)
speed = 10
curr = 0
time.sleep(10)
for i in range(100):
	img = Image.open('bg color.png')    
	idraw = ImageDraw.Draw(img)
	#idraw.rectangle((curr, 10, 100, 100), fill='blue')
	text = f'Count: {curr//10}'
	idraw.text((940, 520), text, font=font)
	img.save('1.png')
	ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, 'C:\\Users\\maste\\Desktop\\1.png', 2)
	curr+=speed
	time.sleep(0.1)
#img.save('rectangle.png')'''


# 2261 5087

a = []
n = 0

with open('26.txt') as f:
	n = int(f.readline())
	for i in range(n):
		a.append([])

	for i in f:
		c = list(map(int, i.split()))
		if len(c) == 2: a[c[0]].append(c[1])

def search11(n):
	for i in range(len(n)-1):
		for j in range(i+1, len(n)):
			if abs(n[i]-n[j]) == 12:
				yield [n[i],n[j]]

for i in a:
	if len(i) > 1 and len(list(search11(i))) > 0:
		m = [min(j) for j in list(search11(i))]
		print(a.index(i), min(m)+1)