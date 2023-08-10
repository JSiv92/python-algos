# go to home function
import modules.goToHome as  home
#print func with green italics
from frontend.greenItalic import print_green_italic

def binary_tree():
    print_green_italic("Binary Tree")

    # 1. a sorted array
    sorted_array = [1,5,8,5,34,54,76,88,787,3453,23466]
    import frontend.redText as red
    red.print_red("Sorted array: " + str(sorted_array))

    # 1.2 get user search item and convert to int
    string_item = input("Get index of : ")
    item = int(string_item)

    # 2. low and high keeps track of which part of the list we are checking
    low = 0
    high = len(sorted_array) - 1

    # 3. while element is not found...
    while low <= high:
        mid = (low + high) // 2 #4. check the middle element
        guess = sorted_array[mid]
        result = "number not in the array" #default

        if guess == item: #5. item is found
            result = f"{item} is located at [{mid}]"
            break
        if guess > item:  #6. guess too high
            high = mid - 1
        else:             #7. guess too low  
            low = mid + 1

    print_green_italic(result)  
    # ask if user wants to go to home page
    home.go_to_home()  



