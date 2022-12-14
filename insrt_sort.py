#insertion sort

def insrt_sort(lst):
	#unsorted = 1
	print(f"Start: {lst} ")
	for unsorted in range(1, len(lst)):
		nextItem = lst[unsorted]
		loc = unsorted
		while ((loc > 0) and (lst[loc-1] > nextItem)):
			lst[loc] = lst[loc-1]
			loc-= 1
		tmp = lst[loc]

		lst[loc] = nextItem
		print(f"Step #{unsorted} (Inserted {nextItem} on {tmp}: {lst}")
	return lst

lst = [29, 10, 14, 37, 13, 20, 41, 53]
tst = insrt_sort(lst)

