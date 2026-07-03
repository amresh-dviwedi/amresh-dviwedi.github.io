import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("350x500")
window.configure(bg="black")
def click_button(value):
    current = display.get()

    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            answer = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, answer)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif value == "+/-":
        if current.startswith("-"):
            display.delete(0, tk.END)
            display.insert(tk.END, current[1:])
        else:
            display.delete(0, tk.END)
            display.insert(tk.END, "-" + current)

    elif value == "%":
        try:
            answer = float(current) / 100
            display.delete(0, tk.END)
            display.insert(tk.END, answer)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    else:
        display.insert(tk.END, value)
display = tk.Entry(window, font=("Arial", 28), bg="black", fg="white", justify="right")
display.pack(fill="both", padx=10, pady=20, ipady=15)
button_frame = tk.Frame(window, bg="black")
button_frame.pack(expand=True, fill="both")
buttons = [
    ["C", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]
for row_index, row in enumerate(buttons):
    for col_index, text in enumerate(row):
        if text in ["/", "*", "-", "+", "="]:
            color = "orange"
        else:
            color = "#222222"

        button = tk.Button(
    button_frame,
    text=text,
    font=("Arial", 20),
    bg=color,
    fg="white",
    width=5,
    height=2,
    command=lambda x=text: click_button(x)
)
        button.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
window.mainloop()