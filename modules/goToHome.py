import main, sys, time
#print func with red text
import frontend.textStyles as textStyle

def go_to_home():
    # ask if return to main menu or shutdown
    choice = input("Do you want to return to the main menu? (y/n): ")  

    if choice.lower() == 'y':
        main.main()  # Call the main() function from the main module to return to the main menu
    else:
        textStyle.print_red("Exiting...")
        time.sleep(0.5)
        sys.exit()  