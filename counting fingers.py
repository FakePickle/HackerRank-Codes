
def fingerCount(N):
	# code here
	rem=N%8
	if not rem:
		print(2)
	elif rem<=5:
		print(rem)
	else:
		print(5-rem%5)
N = int(input())
fingerCount(N)