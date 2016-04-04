from random import sample


def insertion_sort(sortme):
	"""Starting from the second element, check if the previous element is
	greater than the current.
	If yes, bump up the previous element's position and check the one after
	Keep going until no
	Put original element into that last position
	Now take the 3rd element and check again, repeat for length of list."""
	steps = 0
	listlength = len(sortme)
	print("Starting list is: {}".format(sortme))
	for jj in range(1, listlength):
	    key = sortme[jj]
	    ii = jj - 1
	    steps += 1
	    while ii >= 0 and sortme[ii] > key:
	        sortme[ii + 1] = sortme[ii]
	        ii -= 1
	        steps += 1
	    sortme[ii + 1] = key
	    print("Next iteration is: {}".format(sortme))

	print("Sorted list is: {}".format(sortme))
	print("Sorted in {} steps".format(steps))
	return sortme

if __name__ == "__main__":
	# Get a randomised list of length 10
	A = sample(range(100), 10)
	sortedlist = insertion_sort(A)
	print("Sorting sorted list")
	insertion_sort(sortedlist)
	sortedlist.reverse()
	print("Sorting reversed list")
	insertion_sort(sortedlist)