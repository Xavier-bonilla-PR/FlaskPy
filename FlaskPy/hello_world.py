import builtins
import sys
original_input = builtins.input

def new_input(prompt=''):
    print(prompt, end='\n', flush=True)  # Add newline and flush
    return original_input('')

builtins.input = new_input


x = input("Your name? ")
print(x)



