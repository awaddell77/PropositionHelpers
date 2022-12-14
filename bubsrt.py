import sys
def bubsrt(lst):
	if not lst: return []
	end = len(lst)
	sorted_ptn = 0 #the sorted portion of the list, increases with each pass
	index_val = lst[0]
	temp = 0
	pass_val = 1
	sortedval = False #when swaps occur
	n = len(lst)
	while(not sortedval and (pass_val< n )):
		index = 0
		sortedval = True
		for i in range(index,n-pass_val):
			nextIndex = i+1
			if lst[i] > lst[nextIndex]:
				#if current index element is greater than next element's value then swap them
				tmp = lst[nextIndex]
				lst[nextIndex] = lst[i]
				lst[i] = tmp
				print(f"Pass #{pass_val}: {lst}")
				sortedval = False

		pass_val += 1
	return lst




if __name__ == "__main__":
	if sys.argv[1] in ("-h", 'help', 'Help', '?'): print("python bubsrt.py [insert space delimited list here (sans the brackets)]")
	else:
		lst = sys.argv[1:]
		print(lst)
		print(bubsrt(lst))

#lst = [29, 10, 14, 37, 13, 20, 41, 53]
#tst = bubsrt(lst)


