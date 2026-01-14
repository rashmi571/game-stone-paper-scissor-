import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create display frame
        display_frame = tk.Frame(self.root, bg="#2e2e2e")
        display_frame.pack(expand=True, fill="both")
        
        # Create display
        display = tk.Entry(display_frame, textvariable=self.input_text, font=('Arial', 24), 
                          justify='right', bd=10, bg="#2e2e2e", fg="white", 
                          insertbackground="white")
        display.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Create buttons frame
        buttons_frame = tk.Frame(self.root, bg="#1a1a1a")
        buttons_frame.pack(expand=True, fill="both")
        
        # Button layout
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '⌫']
        ]
        
        button_font = font.Font(family='Arial', size=18, weight='bold')
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                # Set button colors
                if btn_text in ['C', '⌫']:
                    bg_color = "#ff6b6b"
                    fg_color = "white"
                elif btn_text == '=':
                    bg_color = "#4CAF50"
                    fg_color = "white"
                elif btn_text in ['+', '-', '*', '/', '(', ')']:
                    bg_color = "#666666"
                    fg_color = "white"
                else:
                    bg_color = "#404040"
                    fg_color = "white"
                
                btn = tk.Button(buttons_frame, text=btn_text, font=button_font,
                               bg=bg_color, fg=fg_color, bd=0,
                               command=lambda x=btn_text: self.on_button_click(x))
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()