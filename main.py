
from tkinter import *
from tkinter import ttk
from stack_operations import stack_operations
from arithmetic_operations import arithmetic_operations
from input_handler import input_handler
from stack_label_updater import stack_label_updater
from mock_label import mock_label

class main_calk:
    def __init__(self):
        self.rt = Tk()
        self.rt.title("RPN Calc 1.1 by Shino")
        self.rt.resizable(0, 0)

        self.mf = ttk.Frame(self.rt)
        self.argument, self.stacklist = StringVar(), StringVar()
        self.mf.grid(column=0, row=0, sticky=(N, W, E, S))

        self.label0 = Label(self.mf, textvariable=self.stacklist)
        self.label0.grid(row=0, columnspan=3)
        self.label1 = Label(self.mf, textvariable=self.argument, background="white")
        self.label1.grid(row=0, column=3)

        self.stack_operations = stack_operations()
        stack_label_updater(self.stacklist, self.stack_operations)
        self.arithmetic_operations = arithmetic_operations(self.stack_operations)
        self.input_handler = input_handler(self.argument)

        self.create_buttons()
        self.rt.mainloop()

    def create_buttons(self):
        buttons = [
            ("7", self.input_handler.construct7), ("8", self.input_handler.construct8), ("9", self.input_handler.construct9), ("+", self.arithmetic_operations.performa),
            ("4", self.input_handler.construct4), ("5", self.input_handler.construct5), ("6", self.input_handler.construct6), ("-", self.arithmetic_operations.performs),
            ("1", self.input_handler.construct1), ("2", self.input_handler.construct2), ("3", self.input_handler.construct3), ("*", self.arithmetic_operations.performm),
            ("0", self.input_handler.construct0), (".", self.input_handler.constructd), ("!", self.arithmetic_operations.performf), ("/", self.arithmetic_operations.performd),
            ("Push!", lambda: self.input_handler.num == self.stack_operations.push(self.input_handler.num, self.argument)),
            ("neg", self.input_handler.constructm), ("<-", self.input_handler.goback), ("<- (st)", self.stack_operations.delfromstack)
        ]

        for i, (text, command) in enumerate(buttons):
            row, col = divmod(i, 4)
            Button(self.mf, text=text, command=command, width=5, height=2).grid(row=row + 2, column=col)

if __name__ == "__main__":
    main_calk()