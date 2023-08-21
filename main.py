# main.py 

# using Colorama to get ANSI escapes to work on Windows
from colorama import just_fix_windows_console

# import textStyles module from frontend folder -
# to access funcs for changing text style/colors
import frontend.textStyles as textStyle

# sys to enable exit func, time to enable sleep func
import sys, time


# MAIN STARTS
def main():

    #fix ansi colors for windows terminals
    just_fix_windows_console()    

    #title
    textStyle.print_title()


#USER INPUT MENU

    textStyle.print_green_italic("Choose a DS: ")

    print("0. Exit")
    print("1. Binary Tree")
    print("2. Selection Sort")
    choice = input("Enter your choice (number): ")

    if choice == "0":
        textStyle.print_red("Exiting...")
        time.sleep(1)
        sys.exit()

    elif choice == "1":
        import modules.binaryTree as module
        module.binary_tree()

    elif choice == "2":
        import modules.selectionSort as module
        module.selection_sort()

    else:
        textStyle.print_red("Invalid choice")
        time.sleep(1)
        textStyle.print_red("Returning to main menu...")
        time.sleep(1.5)
        main()


#MAIN
if __name__ == "__main__":
    main()
