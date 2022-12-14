import math

def objectSwap(lhs, rhs):
	tmp = lhs
	lhs = rhs
	rhs = tmp
	return lhs, rhs
def choosePivot(lst, first, last):
	middle = math.floor((first+last)/2)
	lst[first], lst[middle] = objectSwap(lst[first] , lst[middle])
def partition(lst, first, last, pivotIndex):
	choosePivot(lst, first, last)
	pivot = lst[first]
	#print(f"Pivot = {pivot} , {lst}" )
	lastS1 = first
	firstUnknown = first + 1
	while(firstUnknown <= last):
		if lst[firstUnknown] < pivot:
			lastS1 += 1
			print(f"Adding {lst[firstUnknown]} to S1")
			lst[firstUnknown], lst[lastS1] =  objectSwap(lst[firstUnknown], lst[lastS1])

		firstUnknown += 1
		#if firstUnknown <= last: break
	print(f"S1: {lst[first+1:last]} ")
	print(f"Swapping {lst[first]} with {lst[lastS1]}")
	lst[first], lst[lastS1] = objectSwap(lst[first], lst[lastS1])
	pivotIndex = lastS1

	return pivotIndex

def quickSort(lst, first='', last=''):
	#if not first and not last: quickSort(lst, 0, len(lst)-1)
	pivotIndex = -1
	if first < last:
		print(f"list: {lst}")
		pivotIndex = partition(lst, first, last, pivotIndex)
		print(f"Pivot: {lst[pivotIndex]}")
		quickSort(lst, first, pivotIndex -1)
		quickSort(lst, pivotIndex +1, last )


lst = [38, 16, 27, 39, 12, 17, 24, 5]
print(lst)
quickSort(lst, 0, len(lst)-1)

