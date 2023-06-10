from tkinter import *

root = Tk()
root.geometry('250x310')
root.resizable(False, False)
root.title('Calculator')
root.iconphoto(False, PhotoImage(file='F:\\Загрузки Google\\Windows_Calculator_icon.png'))

background_frame = Frame(width=250,
                         height=310,
                         bg='#212122')
background_frame.place(relx=0.5,
                       rely=0.5,
                       anchor=CENTER)

result_bottom = Entry(root,
                      font='Montserrat 18',
                      background='#212122',
                      borderwidth=0,
                      foreground='white',
                      justify=RIGHT,
                      state='readonly')
result_bottom.configure(readonlybackground='#212122')
result_bottom.place(width=230,
                    height=50,
                    relx=0.5,
                    rely=0.195,
                    anchor=CENTER)

result_top = Entry(root,
                   font='Montserrat 14',
                   borderwidth=0,
                   foreground='white',
                   justify=RIGHT,
                   state='readonly')
result_top.configure(readonlybackground='#212122')
result_top.place(width=230,
                 height=30,
                 relx=0.5,
                 rely=0.07,
                 anchor=CENTER)


class CreateButtons:
    def __init__(self, text, bg, command, height=2, width=7, font='Montserrat 9',
                 foreground='white', borderwidth=0):
        self.text = text
        self.height = height
        self.width = width
        self.font = font
        self.bg = bg
        self.foreground = foreground
        self.borderwidth = borderwidth
        self.command = command


class PlaceButtons(CreateButtons):
    def __init__(self, text, bg, command, relx, rely, anchor=CENTER):
        super().__init__(text, bg, command)
        self.relx = relx
        self.rely = rely
        self.anchor = anchor

        button = Button(root,
                        text=self.text,
                        height=self.height,
                        width=self.width,
                        font=self.font,
                        bg=self.bg,
                        foreground=self.foreground,
                        borderwidth=self.borderwidth,
                        command=self.command)

        button.place(relx=self.relx,
                     rely=self.rely,
                     anchor=self.anchor)


class Buttons:
    @staticmethod
    def insert(sign):
        result_bottom.config(state='normal')
        if result_bottom.get() == 'ZeroDivisionError!':
            result_bottom.delete(0, END)
            result_bottom.insert(END, f'{sign}')
        else:
            entered_bottom = result_bottom.get()
            if sign not in '.-+÷×' and entered_bottom == '0':
                result_bottom.delete(0, END)
            result_bottom.insert(END, f'{sign}')
        result_bottom.config(state='readonly')

    @staticmethod
    def verify():
        result_bottom.config(state='normal')
        result_top.config(state='normal')
        if len(result_bottom.get()) == 1:
            result_bottom.delete(0)
        else:
            result_top.insert(END, result_bottom.get())
            result_bottom.delete(0, END)
        result_bottom.config(state='readonly')
        result_top.config(state='readonly')


def press_but_0():
    button = Buttons()
    button.insert('0')


but_0 = PlaceButtons('0', 'black', press_but_0, 0.38, 0.92)


def press_but_1():
    button = Buttons()
    button.insert('1')


but_1 = PlaceButtons('1', 'black', press_but_1, 0.14, 0.78)


def press_but_2():
    button = Buttons()
    button.insert('2')


but_2 = PlaceButtons('2', 'black', press_but_2, 0.38, 0.78)


def press_but_3():
    button = Buttons()
    button.insert('3')


but_3 = PlaceButtons('3', 'black', press_but_3, 0.62, 0.78)


def press_but_4():
    button = Buttons()
    button.insert('4')


but_4 = PlaceButtons('4', 'black', press_but_4, 0.14, 0.64)


def press_but_5():
    button = Buttons()
    button.insert('5')


but_5 = PlaceButtons('5', 'black', press_but_5, 0.38, 0.64)


def press_but_6():
    button = Buttons()
    button.insert('6')


but_6 = PlaceButtons('6', 'black', press_but_6, 0.62, 0.64)


def press_but_7():
    button = Buttons()
    button.insert('7')


but_7 = PlaceButtons('7', 'black', press_but_7, 0.14, 0.5)


def press_but_8():
    button = Buttons()
    button.insert('8')


but_8 = PlaceButtons('8', 'black', press_but_8, 0.38, 0.5)


def press_but_9():
    button = Buttons()
    button.insert('9')


but_9 = PlaceButtons('9', 'black', press_but_9, 0.62, 0.5)


def press_but_plus():
    button = Buttons()
    button.insert('+')
    button.verify()


but_plus = PlaceButtons('+', '#131212', press_but_plus, 0.86, 0.78)


def press_but_minus():
    button = Buttons()
    button.insert('-')
    button.verify()


but_minus = PlaceButtons('-', '#131212', press_but_minus, 0.86, 0.64)


def press_but_plus_minus():
    result_bottom.configure(state='normal')
    result_top.configure(state='normal')
    entered_bottom = result_bottom.get()
    if entered_bottom[0] != '-':
        result_bottom.insert(0, '-')
    else:
        result_bottom.delete(0, 1)
    result_bottom.configure(state='readonly')
    result_top.configure(state='readonly')


but_plus_minus = PlaceButtons('±', '#131212', press_but_plus_minus, 0.14, 0.92)


def press_but_multiply():
    button = Buttons()
    button.insert('×')
    button.verify()


but_multiply = PlaceButtons('×', '#131212', press_but_multiply, 0.86, 0.5)


def press_but_divide():
    button = Buttons()
    button.insert('÷')
    button.verify()


but_divide = PlaceButtons('÷', '#131212', press_but_divide, 0.86, 0.36)


def press_but_point():
    button = Buttons()
    result_bottom.configure(state='normal')
    if result_bottom.get() == 'ZeroDivisionError!':
        result_bottom.delete(0, END)
    else:
        if len(result_bottom.get()) != 0:
            if '.' not in (result_bottom.get()):
                button.insert('.')
    result_bottom.configure(state='readonly')


but_point = PlaceButtons('.', '#131212', press_but_point, 0.62, 0.92)


def press_but_equal():
    result_bottom.configure(state='normal')
    result_top.configure(state='normal')
    if result_bottom.get() != 'ZeroDivisionError!':
        try:
            solution = result_top.get() + result_bottom.get()
            result_bottom.delete(0, END)
            result_top.delete(0, END)
            solution = solution.replace('×', '*')
            solution = solution.replace('÷', '/')
            solution = eval(solution)
            result_bottom.insert(END, f'{solution}')
        except ZeroDivisionError:
            result_bottom.delete(0, END)
            result_top.delete(0, END)
            result_bottom.insert(END, 'ZeroDivisionError!')
    else:
        result_bottom.delete(0, END)
    result_bottom.configure(state='readonly')
    result_top.configure(state='readonly')


but_equal = PlaceButtons('=', '#131212', press_but_equal, 0.86, 0.92)


def press_but_delete_all():
    result_bottom.config(state='normal')
    result_top.config(state='normal')
    result_bottom.delete(0, END)
    result_top.delete(0, END)
    result_bottom.config(state='readonly')
    result_top.config(state='readonly')


but_delete_all = PlaceButtons('C', '#131212', press_but_delete_all, 0.38, 0.36)


def press_but_delete_one_symbol():
    result_bottom.config(state='normal')
    result_bottom.delete(len(result_bottom.get()) - 1)
    result_bottom.config(state='readonly')


but_delete_one_symbol = PlaceButtons('←', '#131212', press_but_delete_one_symbol, 0.62, 0.36)


def press_but_delete_last_entry():
    result_bottom.config(state='normal')
    result_bottom.delete(0, END)
    result_bottom.config(state='readonly')


but_delete_last_entry = PlaceButtons('CE', '#131212', press_but_delete_last_entry, 0.14, 0.36)

mainloop()
