# selection sort O(n2) or O(nxn) 
# is slower than quick sort which is O(n log n)
# this is because selection sort check each element in the list

# this function is to find the smallest value to start sorting with
def find_smallest(arr):
    smallest = arr[0] #store the smallest value at index 0
    smallest_index = 0 #store the index of the smallest value

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


#using the function above inside the selection sort algo
def selection_sort(arr):    
    print("selection sort")

    newArr = [] #new array to hold sorted list
    for i in range(len(arr)):
        smallest = find_smallest(arr) #find smallest element in the array
        newArr.append(arr.pop(smallest)) #add element to new array and remove from arr
    return newArr

def print_selection_sort():
    sorted_array =  selection_sort([45,3,564,2,23,52])
    print(sorted_array)