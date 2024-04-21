class RadixSort:
    def __init__(self):
        '''
        Initialize the RadixSort class.
        '''
        self.time = 0
        # Create 10 buckets (0-9)
        self.table = [[] for _ in range(10)]
        self.max = 0

    def insert(self, elem, digit_place):
        '''
        Insert an element into the correct bucket based on the current digit place.
        
        @param int elem: element to be inserted
        @param int digit_place: the current digit place (1s, 10s, 100s, etc.)
        '''
        # Calculate the bucket index using the current digit place
        bucket_index = (elem // digit_place) % 10
        # Insert the element into the appropriate bucket
        self.table[bucket_index].append(elem)

    def sort(self, data):
        '''
        Sort the list data using RadixSort.
        @param list data: list to be sorted
        '''
        # Find the maximum value to know the maximum number of digits
        self.max = max(data)
        
        # Start with the least significant digit place (1s place)
        digit_place = 1
        
        # Loop through each digit place while there is a digit place to process
        while self.max // digit_place > 0:
            # Clear the buckets
            self.table = [[] for _ in range(10)]
            
            # Distribute elements into buckets based on the current digit place
            for elem in data:
                self.insert(elem, digit_place)
            
            # Gather the elements from the buckets back into the data list
            index = 0
            for bucket in self.table:
                for elem in bucket:
                    data[index] = elem
                    index += 1
            
            # Move to the next significant digit place (10s place, 100s place, etc.)
            digit_place *= 10

# Example usage
arr = [329, 457, 657, 839, 436, 720, 355]
rsort = RadixSort()
rsort.sort(arr)
print(arr)  # Output will be a sorted array: [329, 355, 436, 457, 657, 720, 839]
