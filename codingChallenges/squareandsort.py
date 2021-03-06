def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(i+1) 
    return (i+1) 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def square_numbers(nums):

    resultArray = []
    for number in nums:
        squareNumber = number**2
        resultArray.append(squareNumber)
    low = len(resultArray)-1
    finalresult = quickSort(resultArray,0,low)
    return finalresult



print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]