from pyautogui import *
import tkinter as tk
from random import uniform
from keyboard import is_pressed

def find_longest_word_with_sequence(filename, sequence):
    longest_word = ""
    
    with open(filename, 'r') as file:
        text = file.read().split()  # Read the file and split it into words
        
        for word in text:
            if sequence in word:  # Check if the sequence exists in the word
                if len(word) > len(longest_word):
                    longest_word = word

    return longest_word

def submit_text(event=None):
    entered_text = text_entry.get()
    letters = entered_text  # Print the entered text in the console
    text_entry.delete(0, tk.END)  # Clear the text entry field
    window.destroy()  # Close the window
    filename = "english.txt"  # Change this to the path of your text file
    sequence_to_find = letters  # Change this to the sequence you want to search for
    result = find_longest_word_with_sequence(filename, sequence_to_find)
    sleep(0.001)
    typewrite(result, uniform(0.001, 0.01))
    sleep(0.01)
    press('enter')

def main():
    global text_entry
    global window
    # Create a new window
    window = tk.Tk()
    window.title("WTF")

    # Create a label
    label = tk.Label(window, text="Letters:")
    label.pack()

    # Create a text entry field
    text_entry = tk.Entry(window)
    text_entry.pack()
    text_entry.focus_set()
    text_entry.focus_force()  # Automatically focus on the text entry field

    # Bind the Enter key to the submit function
    text_entry.bind('<Return>', submit_text)

    # Start the GUI main loop
    window.mainloop()

while True:
    if is_pressed('ctrl'):
        main()