import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import threading

def visualize_palindromes(s: str):
    if any(char.isdigit() for char in s):
        messagebox.showerror("Input Error", "Input wrong, try again. Only alphabetic strings are allowed.")
        return
    
    def setup_plot():
        global fig, ax1, ax2, canvas, text_bf, text_dp
        result_window = tk.Toplevel(root)
        result_window.title("Palindrome Finder - Visualization")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        setup_axes([ax1, ax2], s, n=len(s))

        text_bf = ax1.text(0.5, -0.1, '', ha='center', va='top', transform=ax1.transAxes)
        text_dp = ax2.text(0.5, -0.1, '', ha='center', va='top', transform=ax2.transAxes)

        run_visualizations()

    def setup_axes(axes, s, n):
        for ax in axes:
            ax.set_xlim(-1, n)
            ax.set_ylim(0, n + 1)
            ax.set_xticks(np.arange(n))
            ax.set_xticklabels(list(s))
            ax.set_yticks(np.arange(n + 1))
            ax.grid(True)

    def run_visualizations():
        threading.Thread(target=lambda: run_brute_force(s)).start()

    def run_brute_force(s):
        n = len(s)
        max_length = 0
        start = 0
        ax1.set_title("Brute Force")
        for i in range(n):
            for j in range(i, n):
                current_sub = s[i:j + 1]
                is_palindrome = current_sub == current_sub[::-1]
                color = 'lightgreen' if is_palindrome else 'lightcoral'
                rect = plt.Rectangle((i, n - j - 1), j - i + 1, 1, color=color)
                ax1.add_patch(rect)
                canvas.draw_idle()
                root.after(50)

                if is_palindrome and max_length < j - i + 1:
                    max_length = j - i + 1
                    start = i
                    longest_palindrome = s[start:start + max_length]

        rect = plt.Rectangle((start, n - start - max_length), max_length, max_length, edgecolor='blue', facecolor='none', linewidth=2)
        ax1.add_patch(rect)
        text_bf.set_text(f"Longest Palindrome: {longest_palindrome}, Time Complexity: O(n³)")
        canvas.draw_idle()
        root.after(1000, run_dynamic_programming, s)

    def run_dynamic_programming(s):
        n = len(s)
        table = [[False] * n for _ in range(n)]
        max_length = 1
        start = 0
        ax2.set_title("Dynamic Programming")
        for i in range(n):
            table[i][i] = True
            rect = plt.Rectangle((i, n - i - 1), 1, 1, color='lightgreen')
            ax2.add_patch(rect)
            canvas.draw_idle()
            root.after(50)

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2
                rect = plt.Rectangle((i, n - i - 2), 2, 1, color='lightgreen')
                ax2.add_patch(rect)
                canvas.draw_idle()
                root.after(50)

        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                    rect = plt.Rectangle((i, n - j - 1), j - i + 1, 1, color='lightgreen')
                    ax2.add_patch(rect)
                    canvas.draw_idle()
                    root.after(50)

        rect = plt.Rectangle((start, n - start - max_length), max_length, max_length, edgecolor='blue', facecolor='none', linewidth=2)
        ax2.add_patch(rect)
        text_dp.set_text(f"Longest Palindrome: {s[start:start + max_length]}, Time Complexity: O(n²)")
        canvas.draw_idle()
        plt.close(fig)

    root.after(0, setup_plot)

# Main window
root = tk.Tk()
root.title("Palindrome Finder")
root.geometry("300x100")

entry_label = tk.Label(root, text="Enter a string:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

visualize_button = tk.Button(root, text="Find Palindrome", command=lambda: visualize_palindromes(entry.get()))
visualize_button.pack(pady=5)

root.mainloop()
