import tkinter as tk
import calendar
from datetime import datetime

def show_calendar():
    now = datetime.now()
    year = now.year
    month = now.month

    cal_text = calendar.month(year, month)

    # Clear previous content
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, cal_text)

# Create main window
root = tk.Tk()
root.title("Calendar - Current Month")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Create a text widget to display the calendar
text_widget = tk.Text(root, height=8, width=20, font=("Courier", 14), bg="white", fg="black", borderwidth=0)
text_widget.pack(padx=10, pady=10)

# Show calendar
show_calendar()

# Keep window always on top
root.attributes('-topmost', True)

# Start the application
root.mainloop()
