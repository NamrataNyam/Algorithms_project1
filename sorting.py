# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
import random as rand
from collections.abc import Iterable

class MergeSort:
	def __init__(self):
		self.time = 0

	def sort(self, data):
		'''
		Sort the list data using MergeSort
	 	@param list data to be sorted
		'''
		self.sortHelper(data, 0, len(data) - 1)

	def sortHelper(self, data, low, high):
		'''
		MergeSort helper method.  Sorts data >= start and < end
		
		@param list data to be sorted
		@param low start of the data to be sorted
		@param high end of the data to be sorted (exclusive)
		'''
		if low < high:
			mid = low + (high-low)//2
		
			# TODO: finish recursive calls to 2 halves
			self.sortHelper(data, low, mid)	
			self.sortHelper(data, mid+1, high)

			self.merge(data, low, mid, high)

	def merge(self, data, low, mid, high):
		'''
		Merge data >= low and < high into sorted data.  Data >= low and < mid are in sorted order.
		Data >= mid and < high are also in sorted order
		
		@param data the partially sorted data
		@param low bottom index of the data to be merged
		@param mid midpoint of the data to be merged
		@param high end of the data to be merged (exclusive)
		
		Note: the merged data must be in the same data array that
		      was passed as a parameter.
		'''
		temp = []
		
		i = low
		j = mid + 1

		while (i <= mid and j <= high):
			# TODO: Compare elements from the 2 sorted sublist and insert
			# 		correct value into temp. Update index accordingly.
			if data[i] <= data[j]:
				temp.append(data[i])
				i += 1
			else:
				temp.append(data[j])
				j += 1

		# TODO
		# copy over the remaining data on the i to mid side if there
		# is some remaining.  
		while i <= mid:
			temp.append(data[i])
			i += 1

		# TODO
		# copy over the remaining data on the j to high side if there
		# is some remaining.
		while j <= high:
			temp.append(data[j])
			j += 1

		# TODO: copy the data back from the temporary list to the original list
		data[low:high + 1] = temp


class QuickSort:
	def __init__(self):
		self.time = 0

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data):
		'''
		Sort the list data using QuickSort
	 	@param list data to be sorted
		'''
		rand.shuffle(data)
		self.sortHelper(data, 0, len(data)-1)

	def sortHelper(self, data, low, high):
		'''
 		Helper method for Quicksort.  Sorts data so that data[lo .. j-1] <= data[j] <= data[j+1 .. hi]
	 	
	 	@param data data to be sorted
	 	@param low start of the data to be sorted (inclusive)
	 	@param high end of the data to be sorted (exclusive)
		'''
		if high <= low:
			return
		
		pivot = self.partition(data, low, high)

		# TODO: Finish recursive calls to sortHelpter
		self.sortHelper(data, low, pivot-1)	
		self.sortHelper(data, pivot+1, high)

	def partition(self, data, low, high):
		i = low - 1
		pivot = data[high]
		for j in range(low, high):
			if data[j] <= pivot:
				i += 1
				self.swap(data, i, j)
		i += 1
		self.swap(data,i,high)
		return i

class InsertionSort:
	def __init__(self):
		self.time = 0

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data):
		'''
		Sort the list data using InsertionSort
	 	@param list data to be sorted
		'''
		# TODO - complete implementation
		for i in range(0, len(data)):
			for j in range(i+1, len(data)):
				if data[i] > data[j]:
					self.swap(data, i, j)

class ShellSort:
	def __init__(self, gap_list):
		self.time = 0
		self.gap_list = gap_list

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data):
		'''
		Sort the list data using ShellSort
	 	@param list data to be sorted
		Gap sequence is stored in self.gap_list upon construction
		'''
		# TODO - complete implementation
		for gap in self.gap_list:
			for i in range(gap, len(data)):
				temp = data[i]
				j = i
				while j >= gap and data[j-gap] > temp:
					data[j] = data[j-gap]
					j -= gap
				data[j] = temp


class BucketSort:
	def __init__(self, range):
		self.time = 0
		self.range = range + 1
		self.table = [None]*self.range
		self.max = 0

	def insert(self, elem):
		if self.table[elem] == None:
			self.table[elem] = [elem]
		else:
			self.table[elem].append(elem)

	def sort(self, data):
		'''
		Sort the list data using BucketSort
	 	@param list data to be sorted
		bucket table is self.table
		'''
		# TODO - complete implementation
  
		temp = []
		for i in range(len(data)):
			self.insert(data[i])
		
		for ele in self.table:
			if ele is not None:
				temp += ele
		
		for i in range(len(data)):
			data[i] = temp[i]

class RadixSort:
	def __init__(self):
		self.time = 0
		self.table = [[]]*10
		self.max = 0
		self.digits = 0

	def insert(self, elem, iter):
		# TODO - complete implementation
		# Refer to insert for BucketSort
		idx = (elem // iter) % 10
		self.table[idx].append(elem)

	def sort(self, data):
		'''
		Sort the list data using RadixSort
	 	@param list data to be sorted
		bucket table is self.table with 10 entries
		'''
		# TODO - complete implementation
		self.max = max(data)
		iter = 1

		while self.max // iter > 0:
			self.table = [[] for _ in range(10)]
			for elem in data:
				self.insert(elem, iter)

			idx = 0
			for bucket in self.table:
				for elem in bucket:
					data[idx] = elem
					idx += 1
			iter *= 10

class CustomSort2:
	def __init__(self):
		self.time = 0

	def sort(self, data):
		rand.shuffle(data)
		self.sortHelper(data, 0, len(data) - 1)

	def sortHelper(self, data, low, high):
		if low < high:
			# Partition the array
			pivot_index = self.hoare_partition(data, low, high)
			
			# Recursively sort the partitions
			self.sortHelper(data, low, pivot_index)
			self.sortHelper(data, pivot_index + 1, high)

	def hoare_partition(self, data, low, high):
		pivot = data[low]
		i = low - 1
		j = high + 1
		
		while True:
			# Find element greater than or equal to pivot from the left
			i += 1
			while data[i] < pivot:
				i += 1
			
			# Find element less than or equal to pivot from the right
			j -= 1
			while data[j] > pivot:
				j -= 1
			
			if i >= j:
				return j
			
			# Swap elements
			data[i], data[j] = data[j], data[i]



	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
