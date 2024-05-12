import tkinter as tk
from tkinter import messagebox

def brute_force(s: str) -> (str, str):
    max_length = 0
    start = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                if max_length < j - i + 1:
                    max_length = j - i + 1
                    start = i
    return s[start:start + max_length], "O(n³)"

def dynamic_programming(s: str) -> (str, str):
    n = len(s)
    table = [[False for x in range(n)] for y in range(n)]
    max_length = 1
    start = 0
    for i in range(n):
        table[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if table[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k
    return s[start:start + max_length], "O(n²)"

def display_results(result_str):
    result_window = tk.Toplevel(root)
    result_window.title("Results")
    lines = result_str.count('\n') + 1
    window_height = min(400, max(150, 18 * lines))
    result_window.geometry(f"500x{window_height}")  
    tk.Label(result_window, text=result_str, justify=tk.LEFT, wraplength=480).pack(pady=10, padx=10)

def find_palindrome():
    user_input = entry.get()
    if any(char.isdigit() for char in user_input):
        messagebox.showerror("Input Error", "Input wrong, try again. Only alphabetic strings are allowed.")
        return

    result_str = ""
    result_str += f"Brute Force - Longest Palindrome: ({brute_force(user_input)[0]})\n Time Complexity: {brute_force(user_input)[1]}\n\n"
    result_str += f"Dynamic Programming - Longest Palindrome: ({dynamic_programming(user_input)[0]})\n Time Complexity: {dynamic_programming(user_input)[1]}\n\n"
    display_results(result_str)

# Create main window
root = tk.Tk()
root.title("Palindrome Finder")
root.geometry("300x100")

# Create input textbox
entry_label = tk.Label(root, text="Enter a string:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=40) 
entry.pack(pady=5)

# Create button to find palindrome
find_button = tk.Button(root, text="Find Palindrome", command=find_palindrome)
find_button.pack(pady=5)

root.mainloop()

