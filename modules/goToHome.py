import main, sys, time
#print func with red text
from frontend.redText import print_red

def go_to_home():
    # ask if return to main menu or shutdown
    choice = input("Do you want to return to the main menu? (y/n): ")  

    if choice.lower() == 'y':
        main.main()  # Call the main() function from the main module to return to the main menu
    else:
        print_red("Exiting...")
        time.sleep(1)
        sys.exit()  