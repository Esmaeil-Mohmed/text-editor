import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*,*")])

    if not file_path:
        return
    
    text_edit.delete(1.0, tk.END)

    with open(file_path, "r") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)

    window.title(f"Text Editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*,*")])

    if not file_path:
        return
    
    with open(file_path, "w") as output_file:
        text = text_edit.get(1.0, tk.END)
        output_file.write(text)

    window.title(f"Text Editor - {file_path}")


window = tk.Tk()
window.title("Text editor")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)

frame_buttons = tk.Frame(window, relief="raised")
frame_buttons.grid(column=0, row=0, sticky="nw")

button_open = tk.Button(frame_buttons, text="Open File", width=8, command=open_file)
button_save = tk.Button(frame_buttons, text="Save AS", width=8, command=save_file)
button_open.grid(padx=5, pady=5)
button_save.grid(padx=5, pady=5)

text_edit = tk.Text(window)
text_edit.grid(column=1, row=0, sticky="nsew")

window.mainloop()