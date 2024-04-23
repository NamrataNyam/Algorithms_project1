import sorting as ref_sorting 
import random
import time
import math
import matplotlib.pyplot as plt

'''
The first part of this code will verify functional correctness of all sorting algorithms.
Then, the code will time 
'''

random.seed(260)

names = ["MergeSort", "QuickSort", "InsertionSort", "ShellSort1", "ShellSort2", "BucketSort", "RadixSort", "CustomSort"]

sorter = [None]*8
sorter[0] = ref_sorting.MergeSort()
sorter[1] = ref_sorting.QuickSort()
sorter[2] = ref_sorting.InsertionSort()
sorter[3] = ref_sorting.ShellSort([7,3,1])
sorter[4] = ref_sorting.ShellSort([1000,100,10,1])
sorter[5] = ref_sorting.BucketSort(16000)
sorter[6] = ref_sorting.RadixSort()
sorter[7] = ref_sorting.CustomSort2()

DATA_SIZE = 500
NUM_EXP = 5
data = []
almost_sorted = []

uniformDistributedTimes = [[] for _ in range(8)]
almostSortedTimes = [[] for _ in range(8)]

theoriticalTimeTable = [[] for _ in range(8)]
lastTime = [1 for _ in range(8)]

theoriticalTimeTable2 = [[] for _ in range(8)]
lastTime2 = [1 for _ in range(8)]

theoriticalTimeTable3 = [[] for _ in range(8)]
lastTime3 = [1 for _ in range(8)]

def generate_data(size, duplicates_ratio):
    unique_count = int(size * (1 - duplicates_ratio))
    unique_elements = list(range(unique_count))
    duplicated_elements = random.choices(unique_elements, k=size - unique_count)
    data = unique_elements + duplicated_elements
    random.shuffle(data)
    return data

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
        data.append(random.randint(0,DATA_SIZE))
        # data.append(random.randint(0,1000))

    # Uniformly distributed data
    for i in range(DATA_SIZE):
        almost_sorted.append(i)

    # Almost sorted data
    pairs = 2*int(math.log(DATA_SIZE,2))
    # print("num pairs:", pairs)
    for i in range(pairs):
        idx1 = random.randint(0,DATA_SIZE-1)
        idx2 = random.randint(0,DATA_SIZE-1)
        temp = almost_sorted[idx1]
        almost_sorted[idx1] = almost_sorted[idx2]
        almost_sorted[idx2] = temp
       
    data_save = data.copy()
    test_data = sorted(data)

    # Uniformly distributed data
    for i in range(len(sorter)):

        data = data_save.copy()
        start_time = time.perf_counter()
        sorter[i].sort(data)
        end_time = time.perf_counter()
        sorter[i].time = end_time - start_time
    print()
    print("Uniformly Distributed Random Data: ")
    for i in range(len(sorter)):
        theoriticalTimeTable[i].append([DATA_SIZE, sorter[i].time, sorter[i].time / lastTime[i]])
        lastTime[i] = sorter[i].time
        uniformDistributedTimes[i].append(sorter[i].time)
        print(names[i], sorter[i].time)
    
    # print("----------TIME TABLE-------------")
    # print(theoriticalTimeTable)

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
        theoriticalTimeTable2[i].append([DATA_SIZE, sorter[i].time, sorter[i].time / lastTime2[i]])
        lastTime2[i] = sorter[i].time
        almostSortedTimes[i].append(sorter[i].time)
        print(names[i], sorter[i].time)

    # print("----------TIME TABLE 2-------------")
    # print(theoriticalTimeTable2)


DATA_SIZE=500
data_sizes = [DATA_SIZE * (2 ** n) for n in range(NUM_EXP)]
plt.loglog(data_sizes, uniformDistributedTimes[0], label='MergeSort')
plt.loglog(data_sizes, uniformDistributedTimes[1], label='QuickSort')
plt.loglog(data_sizes, uniformDistributedTimes[2], label='InsertionSort')
plt.loglog(data_sizes, uniformDistributedTimes[3], label='ShellSort1')
plt.loglog(data_sizes, uniformDistributedTimes[4], label='ShellSort2')
plt.loglog(data_sizes, uniformDistributedTimes[5], label='BucketSort')
plt.loglog(data_sizes, uniformDistributedTimes[6], label='RadixSort')
plt.loglog(data_sizes, uniformDistributedTimes[7], label='CustomSort2')

# Add labels and title
plt.xlabel('Data Size (n)')
plt.ylabel('Time (s)')
plt.title('Sorting Time Comparison')
plt.legend()
plt.show()

DATA_SIZE=500
data_sizes = [DATA_SIZE * (2 ** n) for n in range(NUM_EXP)]
plt.loglog(data_sizes, almostSortedTimes[0], label='MergeSort')
plt.loglog(data_sizes, almostSortedTimes[1], label='QuickSort')
plt.loglog(data_sizes, almostSortedTimes[2], label='InsertionSort')
plt.loglog(data_sizes, almostSortedTimes[3], label='ShellSort1')
plt.loglog(data_sizes, almostSortedTimes[4], label='ShellSort2')
plt.loglog(data_sizes, almostSortedTimes[5], label='BucketSort')
plt.loglog(data_sizes, almostSortedTimes[6], label='RadixSort')
plt.loglog(data_sizes, almostSortedTimes[7], label='CustomSort2')

# Add labels and title
plt.xlabel('Data Size (n)')
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
