# selection sort O(n2) or O(nxn) 
# is slower than quick sort which is O(n log n)
# this is because selection sort checks each element in the list

# function to return to main.py
import modules.goToHome as  home
# import frontend module
import frontend.textStyles as textStyle

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
def selection_sort():    
    textStyle.print_green_italic("Selection Sort")

    input_string = input("Please enter numbers seperated by a space: ")
    unsorted_list = [int(x) for x in input_string.split()]  # Convert input to integers

    newArr = [] #new array to hold sorted list

    for i in range(len(unsorted_list)):
        smallest = find_smallest(unsorted_list) #find smallest element in the array
        newArr.append(unsorted_list.pop(smallest)) #add element to new array and remove from arr
   
    # print sorted array
    textStyle.print_green_italic(newArr)

    # function to return to home
    home.go_to_home()

# call the selection_sort function if this script is run directly
if __name__ == "__main__":
    selection_sort()