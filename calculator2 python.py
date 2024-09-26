from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')  # Corrected the geometry string
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Button layout with appropriate commands and labels
        buttons = [
            ('7', 0, 50), ('8', 90, 50), ('9', 180, 50), ('/', 270, 50),
            ('4', 0, 125), ('5', 90, 125), ('6', 180, 125), ('*', 270, 125),
            ('1', 0, 200), ('2', 90, 200), ('3', 180, 200), ('-', 270, 200),
            ('C', 0, 275), ('0', 90, 275), ('=', 180, 275), ('+', 270, 275)
        ]

        for (text, x, y) in buttons:
            Button(master, width=11, height=4, text=text, relief='flat', bg='white',
                   command=lambda value=text: self.show(value) if value != '=' and value != 'C' else self.solve() if value == '=' else self.clear()).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = str(eval(self.entry_value))  # Using eval to evaluate the expression
            self.equation.set(result)
            self.entry_value = result  # Store the result for further calculations
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()

