# main.py 

# using Colorama to get ANSI escapes to work on Windows
from colorama import just_fix_windows_console
# logo/program title
from frontend.printTitle import print_title
#print func with green italics
from frontend.greenItalic import print_green_italic
#print func with red text
from frontend.redText import print_red

import sys, time


# MAIN STARTS
def main():

    #fix ansi colors for windows terminals
    just_fix_windows_console()    

    #title
    print_title()


#USER INPUT MENU

    print_green_italic("Choose a DS: ")

    print("0. Exit")
    print("1. Binary Tree")
    print("2. Linked List")
    choice = input("Enter your choice (number): ")

    if choice == "0":
        print_red("Exiting...")
        time.sleep(1)
        sys.exit()

    elif choice == "1":
        import modules.binaryTree as module
        module.binary_tree()

    elif choice == "2":
        import modules.linkedList as module
        module.linked_list()

    else:
        print_red("Invalid choice")
        time.sleep(1)
        print_red("Returning to main menu...")
        time.sleep(1.5)
        main()


#MAIN
if __name__ == "__main__":
    main()
