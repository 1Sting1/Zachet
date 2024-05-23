import tkinter.messagebox

class input_handler:
    def __init__(self, argument):
        self.num = ''
        self.argument = argument

    def construct_number(self, number):
        if number == '0' and self.num == '0':
            tkinter.messagebox.showinfo("The error", "Can't begin with a zero.")
        else:
            self.num += number
            self.argument.set(self.num)

    def construct0(self):
        self.construct_number('0')

    def construct1(self):
        self.construct_number('1')

    def construct2(self):
        self.construct_number('2')

    def construct3(self):
        self.construct_number('3')

    def construct4(self):
        self.construct_number('4')

    def construct5(self):
        self.construct_number('5')

    def construct6(self):
        self.construct_number('6')

    def construct7(self):
        self.construct_number('7')

    def construct8(self):
        self.construct_number('8')

    def construct9(self):
        self.construct_number('9')

    def constructd(self):
        if '.' in self.num:
            tkinter.messagebox.showinfo("The error", "A dot is used already.")
        elif self.num == '':
            self.num += "0."
            self.argument.set(self.num)
        else:
            self.num += '.'
            self.argument.set(self.num)

    def constructm(self):
        if self.num == '':
            self.num += '-'
            self.argument.set(self.num)
        else:
            tkinter.messagebox.showinfo("The error", "A minus can be put only in the beginning.")

    def goback(self):
        if self.num == '':
            tkinter.messagebox.showinfo("The error", "It's empty already.")
        else:
            self.num = self.num[:-1]
            self.argument.set(self.num)
