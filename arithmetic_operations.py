import tkinter.messagebox
class arithmetic_operations:
    def __init__(self, stack_operations):
        self.stack_operations = stack_operations

    def perform_operation(self, operation):
        stack = self.stack_operations.stack
        if len(stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            stack[-2] = operation(stack[-2], stack[-1])
            stack.pop()
            if stack[-1] % 1 == 0.0:
                stack[-1] = int(stack[-1])
            self.stack_operations.update_stacklist()

    def performa(self):
        self.perform_operation(lambda x, y: x + y)

    def performs(self):
        self.perform_operation(lambda x, y: x - y)

    def performm(self):
        self.perform_operation(lambda x, y: x * y)

    def performd(self):
        stack = self.stack_operations.stack
        if len(stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            if stack[-1] == 0:
                tkinter.messagebox.showinfo("The error", "The divisor is 0, can't perform the division.")
            else:
                self.perform_operation(lambda x, y: x / y)

    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)

    def performf(self):
        stack = self.stack_operations.stack
        if len(stack) < 1:
            tkinter.messagebox.showinfo("The error", "At least 1 element in the stack is required.")
        elif not isinstance(stack[-1], int):
            tkinter.messagebox.showinfo("The error", "The type of the argument is not an integer.")
        elif stack[-1] < 0:
            tkinter.messagebox.showinfo("The error", "Unable to factor a negative number.")
        elif stack[-1] > 25:
            tkinter.messagebox.showinfo("The error", "The number is too large.")
        else:
            stack[-1] = self.factorial(stack[-1])
            self.stack_operations.update_stacklist()