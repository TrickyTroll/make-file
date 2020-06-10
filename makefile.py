import pyautogui
import subprocess
from shutil import which

# Making sure vim is installed.
if which("vim") == None:
    print("You will need Vim if you want this program
    to work. Please install it.")
    exit()

# File creation
# The file should probably be precreated by the user.

# File loading:
def load_file(path_to_file):
    '''
    Loads a file by lines to help with movement while editing.

    path_to_file: The path towards the file you want to load.
    This should be the file you will edit later on.
    returns: A dictionnary with strings associated with each 
    line of the text file.
    '''
    with opent(path_to_file, "r") as stream:
        lines = stream.readlines()
    sort = {}
    line_number = 1
    for line in lines:
        sort[line_number] = line
        line_number += 1
    return sort

# Options to start vim
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
    pyautogui.write("vim", interval = .25)
    pyautogui.write(path_to_file, interval = .25)
    pyautogui.press("enter")

# Some vim utilities. These functions assume that load_file has run 
# and that vim is running.

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

def write_file():
    '''
    This command should rewrite the whole file using pyautogui.
    Since I'm not sure about the use cases yet, the function has not
    been implemented.
    '''
    return None

def change_word(word, new_word, line_number, file_lines):
    '''
    This function changes all occurences of a word in the 
    provided line number.
    
    word: A string that will be replaced.
    new_word: What to replace word for.
    line_number: The number of the line where the string is located.
    file_lines: Returned by the load_file function.
    returns: 'Done!'
    '''
    pyautogui.press([str(line_number), 'G'])
    current_line = file_lines[line_number]
    words_in_line = current_line.split()
    word_position = words_in_line.index(word)+1
    # The (+1) comes from the fact that index starts at 0.
    pyautogui.press([str(word_position), 'w')
    pyautogui.press(['c', 'w'])
    pyautogui.write(new_word, interval = .25)
    return 'Done!'

def change_from_until(begins_after, ends_before, new_expression, line_number, file_lines):
    '''
    Changes an expression on a line from begins_after until ends_before.

    begins_after: A string delimiter.
    ends_before: Another string delimiter.
    new_expression: A string. What the expression will be replaced for.
    file_lines: Returned by the load_file function.
    returns: 'Done!'
    '''
    pyautogui.press([str(line_number), 'G'])
    current_line = file_lines[line_number]
    words_in_line = current_line.split()
    begin_index = words_in_line.index(begins_after)
    end_index = words_in_line.index(ends_before)

    move_to = begin_index+1
    replace_until = (end_index+1) - move_to
    pyautogui.press([str(move_to), 'w'])
    pyautogui.press(['c', str(replace_until), 'w'])
    pyautogui.write(new_expression, interval = .25)
    
    return 'Done!'
