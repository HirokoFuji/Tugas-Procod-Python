import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

root = tk.Tk()
root.title("Kalkulator Pelo")

entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, font=('Arial', 14), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Hasil", width=20, font=('Arial', 14), command=calculate).grid(row=row, column=0, columnspan=4, padx=5, pady=5)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.grid(row=row+1, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
