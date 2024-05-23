from tkinter import StringVar
from observable import observable
import tkinter.messagebox
class stack_operations(observable):
    def __init__(self):
        super().__init__()
        self.stack = []

    def update_stacklist(self):
        self.notify_observers()

    def push(self, num, argument):
        try:
            if float(num) % 1 == 0.0:
                self.stack.append(int(num))
            else:
                self.stack.append(float(num))
            self.update_stacklist()
            argument.set('')
            return ''
        except ValueError:
            tkinter.messagebox.showinfo("The error", "Invalid number.")
            return num

    def delfromstack(self):
        if len(self.stack) == 0:
            tkinter.messagebox.showinfo("The error", "There is nothing on the stack.")
        else:
            self.stack.pop()
            self.update_stacklist()
