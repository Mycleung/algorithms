from random import sample


def selection_sort(sortme):
	"""Loop over the entire list, finding the minimum element and putting
	it at the front. Then loop over the rest of the list doing the same.

	Complexity:
	Same running time for best/worst case, only dependent on list length.
	O(n**2)
	"""
	def swap(a, b):
		temp = sortme[a]
		sortme[a] = sortme[b]
		sortme[b] = temp

	steps = 0
	listlength = len(sortme)
	print("Starting list is: {}".format(sortme))
	for jj in range(listlength):
		min = sortme[jj]
		mindex = jj
		steps += 1
		for ii in range(jj, listlength):
			steps += 1
			if sortme[ii] < min:
				min = sortme[ii]
				mindex = ii
		swap(jj, mindex)
		print("Next iteration is: {}".format(sortme))

	print("Sorted list is: {}".format(sortme))
	print("Sorted in {} steps".format(steps))
	return sortme

if __name__ == "__main__":
	# Get a randomised list of length 10
	A = sample(range(100), 10)
	sortedlist = selection_sort(A)
	print("Sorting sorted list")
	selection_sort(sortedlist)
	sortedlist.reverse()
	print("Sorting reversed list")
	selection_sort(sortedlist)