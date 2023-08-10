# main.py

# using Colorama to get ANSI escapes to work on Windows
from colorama import just_fix_windows_console
just_fix_windows_console()

import sys

def main():

#TITLE    
    border = "+" + "-" * 11 + "+"
    spaced_text = "    " + "\033[1;35mALGOS\033[0m    "  # Bold and magenta text

    print(border)
    print(spaced_text)
    print(border)


#USER INPUT MENU
    print("\033[3;32mChoose a DS:\033[0m")

    print("0. Exit")
    print("1. Binary Tree")
    print("2. Linked List")
    choice = input("Enter your choice (number): ")

    if choice == "0":
        print("Exiting...")
        sys.exit()
    elif choice == "1":
        import modules.binaryTree as module
        module.binaryTree()
    elif choice == "2":
        import modules.linkedList as module
        module.linkedList()
    else:
        print("Invalid choice")


#MAIN
if __name__ == "__main__":
    main()
