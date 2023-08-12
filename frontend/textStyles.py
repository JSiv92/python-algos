
# Red bold text
def print_red(text):
    print(f"\033[91m{text}\033[0m")

# Green italic text
def print_green_italic(text):
    print(f"\033[3;32m{text}\033[0m")

# Title/Logo/Homepage 
def print_title():
    border = "+" + "-" * 11 + "+"
    spaced_text = "    " + "\033[1;35mALGOS\033[0m    "  # Bold and magenta text

    print(" ")
    print(border)
    print(spaced_text)
    print(border)


