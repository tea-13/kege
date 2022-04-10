# Answer: 2261 5087

a = []
n = 0

with open('26.txt') as f:
	n = int(f.readline())
	a = [ [] for i in range(n) ]

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
