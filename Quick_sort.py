import random
import time

#data_array = []  an empty array for loading data of given main file if we need to maintain fixed number of elements.

# fixed length arrays as required 
array_30 = [None] * 30
array_1000 = [None] * 1000
array_3000 = [None] * 3000

# Here we read all the data from the given file and store in an array if we need to maintain fixed number of elements.
'''with open('4_letter_words_rand.txt', 'r') as file:
    for line in file:
        data_array += line.split()'''


# Algorithm 
# Quick Sort
# Taken as a function to make the coding efficient as we need to sort 3 datas or arrays
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    for word in arr[:-1]:
        if isinstance(word, str) and isinstance(pivot, str):
            if word < pivot:
                left.append(word)
            else:
                right.append(word)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# A function that takes the array as input returns the array by removing duplicates.
# Same word with capital and other in lower are treated as different word, else you can treat as one by adding .lower() in if condition
def duplicate(arr):
    unique_words = [arr[0]]
    for word in arr[1:]:
            if word != unique_words[-1]:
                unique_words.append(word)
    return unique_words

# This loop runs for a range of three as we require to traverse through 3 arrays or datas

for i in range(3):
    if i == 0:
        # Here we read all the data from the file and store in an array
        with open('array_30.txt', 'r') as file:
            for line in file:
                array_30 += line.split()
        start_30 = time.time()
        arrQS_O_30 = quick_sort(array_30) # sorting
        end_30 = time.time()
        exc_30 = end_30 - start_30 # time taken for execution
        arrQS_O_30 = duplicate(arrQS_O_30) # removing duplicates
        
        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrQS_O_30) < 30:
            add_30 = random.sample(data_array, 30 - len(arrQS_O_30))
            arrQS_O_30.extend(add_30)
            quick_sort(arrQS_O_30)
            arrQS_O_30 = duplicate(arrQS_O_30)'''
        
        # Stores the sorted unique array and execution time into a text file.
        with open('arrQS_O_30.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_30) + '\n')
            for item in arrQS_O_30:
                file.write(str(item) + '\n')
        
    elif i == 1:
        # Here we read all the data from the file and store in an array
        with open('array_1000.txt', 'r') as file:
            for line in file:
                array_1000 += line.split()
        start_1000 = time.time()
        arrQS_O_1000 = quick_sort(array_1000) # sorting
        end_1000 = time.time()
        exc_1000 = end_1000 - start_1000 # time taken for execution
        arrQS_O_1000 = duplicate(arrQS_O_1000) # removing duplicates
        
        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrQS_O_1000) < 1000:
            add_1000 = random.sample(data_array, 1000 - len(arrQS_O_1000))
            arrQS_O_1000.extend(add_1000)
            quick_sort(arrQS_O_1000)
            arrQS_O_1000 = duplicate(arrQS_O_1000)'''
        
        # Stores the sorted unique array and execution time into a text file.
        with open('arrQS_O_1000.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_1000) + '\n')
            for item in arrQS_O_1000:
                file.write(str(item) + '\n')
        
    else:
        # Here we read all the data from the file and store in an array
        with open('array_3000.txt', 'r') as file:
            for line in file:
                array_3000 += line.split()
        start_3000 = time.time()
        arrQS_O_3000 = quick_sort(array_3000) # sorting
        end_3000 = time.time()
        exc_3000 = end_3000 - start_3000 # time taken for execution
        arrQS_O_3000 = duplicate(arrQS_O_3000) # removing duplicates
        
        # The below commented code is used if we are expected that if both input file and output file must contain same count of words but the output must not have duplicates.
        '''while len(arrQS_O_3000) < 3000:
            add_3000 = random.sample(data_array, 3000 - len(arrQS_O_3000))
            arrQS_O_3000.extend(add_3000)
            quick_sort(arrQS_O_3000)
            arrQS_O_3000 = duplicate(arrQS_O_3000)'''
        
        # Stores the sorted unique array and execution time into a text file.
        with open('arrQS_O_3000.txt', 'w') as file:
            file.write('Time taken :- ' + str(exc_3000) + '\n')
            for item in arrQS_O_3000:
                file.write(str(item) + '\n')


