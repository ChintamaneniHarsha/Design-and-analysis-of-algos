import random
import time

data_array = [] # an empty array for loading data of given main file.

# fixed length arrays as required 
array_30 = [None] * 30 
array_1000 = [None] * 1000
array_3000 = [None] * 3000

# Here we read all the data from the given file and store in an array
with open('4_letter_words_rand.txt', 'r') as file:
    for line in file:
        data_array += line.split()

# loading data into three specified arrays randomly.
for i in range(30):
    array_30[i] = random.choice(data_array)

for i in range(1000):
    array_1000[i] = random.choice(data_array)
    
for i in range(3000):
    array_3000[i] = random.choice(data_array)

# Algorithm 
# Insertion Sort
# Taken as a function to make the coding efficient as we need to sort 3 datas or arrays
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # takes the array and returns the array by removing duplicates.
    # Same word with capital and other in lower are treated as different word, else you can treat as one by adding .lower() in if condition
    unique_words = []
    for i in range(len(arr)):
            if arr[i] not in unique_words:
                unique_words.append(arr[i])
    return unique_words



# This loop runs for a range of three as we require to traverse through 3 arrays or datas
for i in range(3):
    if i == 0:
        # Stores the array into a text file.
        with open('array_30.txt', 'w') as file:
            for item in array_30:
                file.write(str(item) + '\n')
        start_30 = time.time()
        arrIS_O_30 = insertion_sort(array_30) # sorting
        end_30 = time.time()
        exc_30 = end_30 - start_30 # Time taken for execution

        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrIS_O_30) < 30:
            add_30 = random.sample(data_array, 30 - len(arrIS_O_30))
            arrIS_O_30.extend(add_30)
            insertion_sort(arrIS_O_30)
            arrIS_O_30 = duplicate(arrIS_O_30)'''

        # Stores the sorted unique array and execution time into a text file.
        with open('arrIS_O_30.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_30) + '\n')
            for item in arrIS_O_30:
                file.write(str(item) + '\n')

        
    elif i == 1:
        # Stores the array into a text file.
        with open('array_1000.txt', 'w') as file:
            for item in array_1000:
                file.write(str(item) + '\n')
        start_1000 = time.time()
        arrIS_O_1000 = insertion_sort(array_1000) # sorting
        end_1000 = time.time()
        exc_1000 = end_1000 - start_1000 # time taken for execution

        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrIS_O_1000) < 1000:
            add_1000 = random.sample(data_array, 1000 - len(arrIS_O_1000))
            arrIS_O_1000.extend(add_1000)
            insertion_sort(arrIS_O_1000)
            arrIS_O_1000 = duplicate(arrIS_O_1000)'''

        # Stores the sorted unique array and execution time into a text file.
        with open('arrIS_O_1000.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_1000) + '\n')
            for item in arrIS_O_1000:
                file.write(str(item) + '\n')
            
           
    elif i == 2:
        # Stores the array into a text file.
        with open('array_3000.txt', 'w') as file:
            for item in array_3000:
                file.write(str(item) + '\n')
        start_3000 = time.time()
        arrIS_O_3000 = insertion_sort(array_3000) # sorting
        end_3000 = time.time()
        exc_3000 = end_3000 - start_3000 # Time taken for execution
        
        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrIS_O_3000) < 3000:
            add_3000 = random.sample(data_array, 3000 - len(arrIS_O_3000))
            arrIS_O_3000.extend(add_3000)
            insertion_sort(arrIS_O_3000)
            arrIS_O_3000 = duplicate(arrIS_O_3000)'''

        # Stores the sorted unique array and execution time into a text file.
        with open('arrIS_O_3000.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_3000) + '\n')
            for item in arrIS_O_3000:
                file.write(str(item) + '\n')


