import time
import sys
import os
from pynput.keyboard import Controller, Key

def start_program():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_to_type = f.read().replace('\t', '    ')
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        return

    trigger = input("Enter 'Y' to start: ").strip().upper()
    
    if trigger == 'Y':
        keyboard = Controller()
        wait_time = 5
        
        for i in range(wait_time + 1):
            percent = int((i / wait_time) * 100)
            filled = int(20 * i / wait_time)
            bar = '█' * filled + '-' * (20 - filled)
            sys.stdout.write(f"\rWaiting: [\033[32m{bar}\033[0m] {percent}%")
            sys.stdout.flush()
            if i < wait_time:
                time.sleep(1)
        
        print("\nTyping...")
        
        shift_chars = '!@#$%^&*()_+{}|:"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        total = len(text_to_type)
        
        for index, char in enumerate(text_to_type, 1):
            if char == '\r':
                continue
            
            if char == '\n':
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(0.1)
            elif char in shift_chars:
                with keyboard.pressed(Key.shift):
                    keyboard.type(char)
            else:
                keyboard.type(char)
            
            time.sleep(0.02)
            
            percent = int((index / total) * 100)
            filled = int(20 * index / total)
            bar = '█' * filled + '-' * (20 - filled)
            sys.stdout.write(f"\rProgress: [\033[32m{bar}\033[0m] {percent}%")
            sys.stdout.flush()

if __name__ == "__main__":
    start_program()
