import pyautogui
import subprocess
from shutil import which

# Making sure vim is installed.
if which("vim") == None:
    print("You will need Vim if you want this program
    to work. Please install it.")
    exit()

def hard_start_vim(path_to_file):
    '''
    Starts vim with subprocess.

    path_to_file: The path towards the file you want to edit.
    returns: 'Vim is running!'
    '''
    subprocess.Popen([
        "vim",
        path_to_file
        ])
    return 'Vim is running!'

def start_vim(path_to_file):
    '''
    Slowly starts vim by typing 'vim' with pyautogui.

    path_to_file: The path towards the file you want to edit.
    returns: 'Vim is running!'
    '''
    

# Some vim utilities
def go_to_line(line_number):
    '''
    Moves the cursor to the line corresponding to line_number.
    
    line_number: An integer. Should represent a line number.
    returns: The line where the cursor should be after the 
    function.
    '''
    pyautogui.press("esc")
    pyautogui.press([line_number, "G"])

    return line_number
