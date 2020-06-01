#!usr/bin/python3
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
def open_file():
    filepath = askopenfilename( filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"V-Note Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes = [("Text Files", "*.txt"), ("Java Files", "*.java"), ("Python Files", "*.py"),
    ("C Files", "*.c"), ("C++ Files", "*.cpp"), ("C# Files", "*.cs"), ("PHP Files", "*.php"), ("HTML Files", "*.html"),
    ("CSS Files", "*.css"), ("Javascript Files", "*.js"), ("Windows Batch Files", "*.bat"), ("Perl Files", "*.pl"),
    ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"V-Note Text Editor - {filepath}")

def help():
    messagebox.showinfo("V-Note Text Editor - Help", " Creator: Vinayak\n Date: 01 June, 2020\n Version: 1.0\n Contact: kunwarvinayak123@outlook.com\n Language: English\n License: \n Publisher: Vinayak")

def new_file():
    messagebox.showinfo( "New File", "Don't forget to save current\nfile before opening new file.")
    txt_edit = tk.Text(window, bg="#333", fg="white")
    txt_edit.grid(row=0, column=1, sticky="nsew")
    window.title("V-Note Text Editor - Untitled")

def white():
    theme1 = messagebox.askquestion( "Light Theme", " Don't forget to save current\n file before changing theme because\n application will take restart.\n Do you want to proceed?")
    if theme1 == 'yes':
        txt_edit = tk.Text(window, bg="white", fg="black")
        txt_edit.grid(row=0, column=1, sticky="nsew")
    else:
        messagebox.showinfo("No", "Ok")    

def black():
    theme2 = messagebox.askquestion( "Dark Theme", " Don't forget to save current\n file before changing theme because\n application will take restart.\n Do you wnat to proceed?")
    if theme2 == 'yes':
        txt_edit = tk.Text(window, bg="#333", fg="white")
        txt_edit.grid(row=0, column=1, sticky="nsew")
    else:
        messagebox.showinfo("No", "Ok")    

def choco():
    theme3 = messagebox.askquestion( "Choco Theme", " Don't forget to save current\n file before changing theme because\n application will take restart.\n Do you want to proceed?")
    if theme3 == 'yes':
        txt_edit = tk.Text(window, bg="chocolate", fg="lawngreen")
        txt_edit.grid(row=0, column=1, sticky="nsew")
    else:
        messagebox.showinfo("No", "Ok")    

def exit():
    result = messagebox.askquestion("V-Note Text Editor", "Do you want to Exit?", icon='warning')
    if result == 'yes':
        window.destroy()
    else:
        messagebox.showinfo("No", "Ok")    

                     

window = tk.Tk()
window.title("V-Note Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, bg="snow", fg="#333")
fr_buttons = tk.Frame(window, relief= tk.RAISED, bd=2, bg="black")
btn_open = tk.Button(fr_buttons, text="Open", command=open_file, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_save = tk.Button(fr_buttons, text="Save As..", command=save_file, bg="#333", fg="white", activebackground="white", activeforeground="#333" )   
btn_help = tk.Button(fr_buttons, text="Help", command=help, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_new = tk.Button(fr_buttons, text="New", command=new_file, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_light = tk.Button(fr_buttons, text="Light Theme", command=white, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_dark = tk.Button(fr_buttons, text="Dark Theme", command=black, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_choco = tk.Button(fr_buttons, text="Choco Theme", command=choco, bg="#333", fg="white", activebackground="white", activeforeground="#333")
btn_exit = tk.Button(fr_buttons, text="Exit", command=exit, bg="#333", fg="white", activebackground="white", activeforeground="#333")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_new.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_help.grid(row=3, column=0, sticky="ew", padx=5)
btn_light.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_dark.grid(row=5, column=0, sticky="ew", padx=5)
btn_choco.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=7, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()