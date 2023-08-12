# BINARY SEARCH FUNCTION
# Initialised a sorted array for testing
# User inputs an element to search for
# Prints the element and index or a not found message

# function to return to main.py
import modules.goToHome as  home
#import frontend module
import frontend.textStyles as textStyle

# binary search logic
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]

        if guess == item:
            return f"{item} is located at [{mid}]"
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return "Number not in the array"    

# main binary tree function which calls the search func
def binary_tree():
    textStyle.print_green_italic("Binary Tree")

    sorted_array = [1, 5, 8, 5, 34, 54, 76, 88, 787, 3453, 23466]
    textStyle.print_red(f"Sorted array: {sorted_array}")

    string_item = input("Get index of: ")
    item = int(string_item)

    result = binary_search(sorted_array, item)
    textStyle.print_green_italic(result)

    #ask user to return to home
    home.go_to_home()

# Call the binary_tree function if this script is run directly
if __name__ == "__main__":
    binary_tree()

