# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("sort-analyzer-python-starter-main/data-files/random-values.txt")
reversedData = loadDataArray("sort-analyzer-python-starter-main/data-files/reversed-values.txt")
nearlySortedData = loadDataArray("sort-analyzer-python-starter-main/data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("sort-analyzer-python-starter-main/data-files/few-unique-values.txt")

# Bubblesort function

def bubbleSort(anArray):
    for i in range(len(anArray) - 1):
        for n in range(len(anArray) - i - 1):
            if anArray[n] > anArray[n+1]:
                value = anArray[n]
                anArray[n] = anArray[n+1]
                anArray[n+1] = value
                
# SelectionSort function 

def selectionSort(anArray):
    for i in range(len(anArray)):
        minPoistion = i
        for n in range(i+1, len(anArray)):
            if anArray[n] < anArray[minPoistion]:
                minPoistion = n
        anArray[i], anArray[minPoistion] = anArray[minPoistion], anArray[i]

# InsertionSort function 

def insertionSort(anArray):
    for i in range(len(anArray)):
        insertVal = anArray[i]
        n = i - 1
        while n >= 0 and insertVal < anArray[n]:
            anArray[n + 1] = anArray[n]
            n = n - 1
        anArray[n + 1] = insertVal


# Bubble Sort - Average Time to Sort Array 

startTime = time.time()
bubbleSort(randomData)
endTime = time.time()
print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(reversedData)
endTime = time.time()
print(f"Bubble Sort reversed Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(nearlySortedData)
endTime = time.time()
print(f"Bubble Sort nearly Sorted Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(fewUniqueData)
endTime = time.time()
print(f"Bubble Sort few unique Data: {endTime - startTime} seconds")

# Selection Sort - Average Time to Sort Array

startTime = time.time()
selectionSort(randomData)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(reversedData)
endTime = time.time()
print(f"Selection Sort reversed Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(nearlySortedData)
endTime = time.time()
print(f"Selection Sort nearly sorted Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(fewUniqueData)
endTime = time.time()
print(f"Selection Sort few unique Data: {endTime - startTime} seconds")

#  Insertion Sort - Average Time to Sort Array

startTime = time.time()
insertionSort(randomData)
endTime = time.time()
print(f"Insertion Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(reversedData)
endTime = time.time()
print(f"Insertion Sort reversed Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(nearlySortedData)
endTime = time.time()
print(f"Insertion Sort nearly sorted Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
print(f"Insertion Sort few unique Data: {endTime - startTime} seconds")
