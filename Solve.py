import os

# read data from input
def readingFile(input):
    f = open(input, 'r')
    reading = f.read()
    arr = reading.split('\n')

    result = []
    for i in arr:
        temp = i.split(" ")
        result.append(temp[0])
        result.append(temp[1])

    return result

# create total of number
def createNumbers(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)

    return result


def reverse(arr, n):
    while(n > 0):
        arr.reverse()
        n = n - 1
    
    return arr

def writingFile(output, arr):
    if(os.path.exists(output)):
        os.remove(output)

    f = open(output, 'a')

    for i in arr:
        f.write(str(i)+" ")
    print("Successfully!")    
    f.close()

data = readingFile("input.txt")
arr = createNumbers(int(data[0]))

# swap 2 element in a list
arr[int(data[2]) - 1], arr[int(data[3]) - 1] = arr[int(data[3]) - 1], arr[int(data[2]) - 1]
arr[int(data[4]) - 1], arr[int(data[5]) - 1] = arr[int(data[5]) - 1], arr[int(data[4]) - 1]

resultArr = reverse(arr, int(data[1]))

writingFile("output.txt", resultArr)



