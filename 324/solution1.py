A = list(map(int, input().split()))

# If文を書きたくないので、左右に余白を作る

# 1行目
prevRow = [0, A[0], A[1], A[2], A[3], 0]

for i in range(3):
	# 前の行のデータから計算して、次の行を作る
	nextRow = [0, 0, 0, 0, 0, 0]
	for j in range(1, 5):
		nextRow[j] = prevRow[j - 1] + prevRow[j] + prevRow[j + 1]

	# 計算結果を次の計算の材料にする
	prevRow = nextRow
print(prevRow[4])
