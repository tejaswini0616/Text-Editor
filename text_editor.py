import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, Menu

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create Menu Bar
        self.menu_bar = Menu(root)
        
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Close", command=self.close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        self.root.config(menu=self.menu_bar)

        # Create Text Area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
    
    def close_file(self):
        self.text_area.delete(1.0, tk.END)
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()