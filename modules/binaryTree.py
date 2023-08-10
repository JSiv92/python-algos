import main

def binaryTree():
    print("Binary Tree")
    
    choice = input("Do you want to return to the main menu? (y/n): ")
    if choice.lower() == 'y':
        main.main()  # Call the main() function from the main module to return to the main menu