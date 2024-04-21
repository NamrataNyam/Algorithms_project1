import sorting as ref_sorting 
import random
import time
import matplotlib.pyplot as plt
import math
'''
The first part of this code will verify functional correctness of all sorting algorithms.
Then, the code will time 
'''

random.seed(260)

names = ["MergeSort", "QuickSort", "InsertionSort", "ShellSort1", "ShellSort2", "BucketSort", "RadixSort"]

sorter = [None]*7
sorter[0] = ref_sorting.MergeSort()
sorter[1] = ref_sorting.QuickSort()
sorter[2] = ref_sorting.InsertionSort()
sorter[3] = ref_sorting.ShellSort([7,3,1])
sorter[4] = ref_sorting.ShellSort([1000,100,10,1])
sorter[5] = ref_sorting.BucketSort(1000)
sorter[6] = ref_sorting.RadixSort()

merge_sort_times = []
quick_sort_times = []
insertion_sort_times = []
shell_sort1_times = []
shell_sort2_times = []
bucket_sort_times = []
radix_sort_times = []

DATA_SIZE = 500
NUM_EXP = 5
data = []
almost_sorted = []
for i in range(DATA_SIZE):
    data.append(random.randint(0,1000))
    
data_save = data.copy()
test_data = sorted(data)

def verify(data, test_data, index):
    for i in range(DATA_SIZE):
        if test_data[i] != data[i]:
            print(names[index], "Incorrect Sorting!")
            exit
    print(names[index], "Successfully Sorted!")

for i in range(len(sorter)):
    data = data_save.copy()
    sorter[i].sort(data)
    verify(data,test_data,i)


for j in range(NUM_EXP):
    print()
    DATA_SIZE = DATA_SIZE * 2
    print("DATA_SIZE:", DATA_SIZE)
    data = []
    almost_sorted = []
    for i in range(DATA_SIZE):
        data.append(random.randint(0,1000))
    
    # Uniformly distributed data
    for i in range(DATA_SIZE):
        almost_sorted.append(i)

    
    # Almost sorted data
    pairs = 2*int(math.log(DATA_SIZE,2))
    for i in range(pairs):
        idx1 = random.randint(0,DATA_SIZE)
        idx2 = random.randint(0,DATA_SIZE)
        temp = almost_sorted[idx1]
        almost_sorted[idx1] = almost_sorted[idx2]
        almost_sorted[idx2] = temp
    data_save = data.copy()
    test_data = sorted(data)
    for i in range(len(sorter)):

        data = data_save.copy()
        start_time = time.perf_counter()
        sorter[i].sort(data)
        end_time = time.perf_counter()
        sorter[i].time = end_time - start_time
        if i == 0:
            merge_sort_times.append(sorter[i].time)
        elif i == 1:
            quick_sort_times.append(sorter[i].time)
        elif i == 2:
            insertion_sort_times.append(sorter[i].time)
        elif i == 3:
            shell_sort1_times.append(sorter[i].time)
        elif i == 4:
            shell_sort2_times.append(sorter[i].time)
        elif i == 5:
            bucket_sort_times.append(sorter[i].time)
        elif i == 6:
            radix_sort_times.append(sorter[i].time)
    
    for i in range(len(sorter)):
        print(names[i], sorter[i].time)
    
    # Almost sorted data
    for i in range(len(sorter)):

        data = almost_sorted.copy()
        start_time = time.perf_counter()
        if i != 5:
            sorter[i].sort(data)
        else:
            sorter[i].range = DATA_SIZE
            sorter[i].sort(data)
        end_time = time.perf_counter()
        sorter[i].time = end_time - start_time
    
    print()
    print("Almost Sorted Data: ")
    for i in range(len(sorter)):
        print(names[i], sorter[i].time)

print(DATA_SIZE)
DATA_SIZE=500
data_sizes = [DATA_SIZE * (2 ** n) for n in range(NUM_EXP)]
plt.plot(data_sizes, merge_sort_times, label='MergeSort')
plt.plot(data_sizes, quick_sort_times, label='QuickSort')
plt.plot(data_sizes, insertion_sort_times, label='InsertionSort')
plt.plot(data_sizes, shell_sort1_times, label='ShellSort1')
plt.plot(data_sizes, shell_sort2_times, label='ShellSort2')
plt.plot(data_sizes, bucket_sort_times, label='BucketSort')
plt.plot(data_sizes, radix_sort_times, label='RadixSort')

# Add labels and title
plt.xlabel('Data Size')
plt.ylabel('Time (s)')
plt.title('Sorting Time Comparison')
plt.legend()
plt.show()
# Please read all of the following before starting your implementation:
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit the requirements.py and the sorting.py files, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - We have provided a project1_tests.py file that contains some simple test cases to give an idea of how we will be running your
#   code. Please use that file when testing your implementation.
#
# Finish the implementations of the following sorting algorithms:
# 
# - MergeSort
# - QuickSort
# - InsertionSort
# - ShellSort
# - BucketSort
# - RadixSort
#
# - Each algorithm is implemented as a class. The testing code can be seen above. 
