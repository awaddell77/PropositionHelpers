

def findMaxIndex(lst, last):
	if not lst: return -1
	maxVal = lst[0]
	maxIndex = 0
	for i in range(0, last+1):
		if lst[i] > maxVal:
			maxVal = lst[i]
			maxIndex = i
	#print(lst[maxIndex])
	return maxIndex


def selsrt(lst):
	last = len(lst)
	swapcnt = 0
	for i in range(last-1,-1,-1 ):
		largest = findMaxIndex(lst, i)
		tmp = lst[i]
		lst[i] = lst[largest]
		lst[largest] = tmp
		swapcnt += 1
		print(f"Swap #{swapcnt}:  Swapped {lst[i]} for {tmp}: {lst}")
	return lst


#lst = [29, 10, 14, 37, 13, 20, 41, 53]
#tst = selsrt(lst)


if __name__ == "__main__":
	if sys.argv[1] in ("-h", 'help', 'Help', '?'): print("python selsrt.py [insert space delimited list here (sans the brackets)]")
	else:
		lst = sys.argv[1:]
		print(lst)
		print(selsrt(lst))