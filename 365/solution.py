class Point:
    def __init__(self, X, Y, idx):
        self.idx = idx
        self.visit = False
        self.x = X
        self.y = Y

def calc(p1, p2):
    return (abs(p1.x - p2.x)**2 + abs(p1.y - p2.y)**2)**0.5

N = int(input())
points = []
for i in range(N):
    X, Y = list(map(int, input().split()))
    points.append(Point(X, Y, i))

total = 0
curr = points[0]
while(True):
    minD = 10000000000000
    minP = None
    if curr.visit:
        continue
    curr.visit = True
    # print("->", curr.idx, curr.x, curr.y)

    for j in range(N):
        if points[j].visit:
            continue
        d = calc(curr, points[j])
        if d < minD:
            minP = points[j]
            minD = d
    if minP is None:
        total += calc(curr, points[0])
        break
    total += minD
    curr = minP
print(total)
