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


but_0 = Button(root,
               text='0',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_0)
but_0.place(relx=0.38,
            rely=0.92,
            anchor=CENTER)


def press_but_1():
    button = Buttons()
    button.insert('1')


but_1 = Button(root,
               text='1',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_1)
but_1.place(relx=0.14,
            rely=0.78,
            anchor=CENTER)


def press_but_2():
    button = Buttons()
    button.insert('2')


but_2 = Button(root,
               text='2',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_2)
but_2.place(relx=0.38,
            rely=0.78,
            anchor=CENTER)


def press_but_3():
    button = Buttons()
    button.insert('3')


but_3 = Button(root,
               text='3',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_3)
but_3.place(relx=0.62,
            rely=0.78,
            anchor=CENTER)


def press_but_4():
    button = Buttons()
    button.insert('4')


but_4 = Button(root,
               text='4',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_4)
but_4.place(relx=0.14,
            rely=0.64,
            anchor=CENTER)


def press_but_5():
    button = Buttons()
    button.insert('5')


but_5 = Button(root,
               text='5',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_5)
but_5.place(relx=0.38,
            rely=0.64,
            anchor=CENTER)


def press_but_6():
    button = Buttons()
    button.insert('6')


but_6 = Button(root,
               text='6',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_6)
but_6.place(relx=0.62,
            rely=0.64,
            anchor=CENTER)


def press_but_7():
    button = Buttons()
    button.insert('7')


but_7 = Button(root,
               text='7',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_7)
but_7.place(relx=0.14,
            rely=0.5,
            anchor=CENTER)


def press_but_8():
    button = Buttons()
    button.insert('8')


but_8 = Button(root,
               text='8',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_8)
but_8.place(relx=0.38,
            rely=0.5,
            anchor=CENTER)


def press_but_9():
    button = Buttons()
    button.insert('9')


but_9 = Button(root,
               text='9',
               height=2,
               width=7,
               font='Montserrat 9',
               bg='black',
               foreground='white',
               borderwidth=0,
               command=press_but_9)
but_9.place(relx=0.62,
            rely=0.5,
            anchor=CENTER)


def press_but_plus():
    button = Buttons()
    button.insert('+')
    button.verify()


but_plus = Button(root,
                  text='+',
                  height=2,
                  width=7,
                  font='Montserrat 9',
                  bg='#131212',
                  foreground='white',
                  borderwidth=0,
                  command=press_but_plus)
but_plus.place(relx=0.86,
               rely=0.78,
               anchor=CENTER)


def press_but_minus():
    button = Buttons()
    button.insert('-')
    button.verify()


but_minus = Button(root,
                   text='-',
                   height=2,
                   width=7,
                   font='Montserrat 9',
                   bg='#131212',
                   foreground='white',
                   borderwidth=0,
                   command=press_but_minus)
but_minus.place(relx=0.86,
                rely=0.64,
                anchor=CENTER)


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


but_plus_minus = Button(root,
                        text='±',
                        height=2,
                        width=7,
                        font='Montserrat 9',
                        bg='#131212',
                        foreground='white',
                        borderwidth=0,
                        command=press_but_plus_minus)
but_plus_minus.place(relx=0.14,
                     rely=0.92,
                     anchor=CENTER)


def press_but_multiply():
    button = Buttons()
    button.insert('×')
    button.verify()


but_multiply = Button(root,
                      text='×',
                      height=2,
                      width=7,
                      font='Montserrat 9',
                      bg='#131212',
                      foreground='white',
                      borderwidth=0,
                      command=press_but_multiply)
but_multiply.place(relx=0.86,
                   rely=0.5,
                   anchor=CENTER)


def press_but_divide():
    button = Buttons()
    button.insert('÷')
    button.verify()


but_divide = Button(root,
                    text='÷',
                    height=2,
                    width=7,
                    font='Montserrat 9',
                    bg='#131212',
                    foreground='white',
                    borderwidth=0,
                    command=press_but_divide)
but_divide.place(relx=0.86,
                 rely=0.36,
                 anchor=CENTER)


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


but_point = Button(root,
                   text='.',
                   height=2,
                   width=7,
                   font='Montserrat 9',
                   bg='#131212',
                   foreground='white',
                   borderwidth=0,
                   command=press_but_point)
but_point.place(relx=0.62,
                rely=0.92,
                anchor=CENTER)


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


but_equal = Button(root,
                   text='=',
                   height=2,
                   width=7,
                   font='Montserrat 9',
                   bg='#131212',
                   foreground='white',
                   borderwidth=0,
                   command=press_but_equal)
but_equal.place(relx=0.86,
                rely=0.92,
                anchor=CENTER)


def press_but_delete_all():
    result_bottom.config(state='normal')
    result_top.config(state='normal')
    result_bottom.delete(0, END)
    result_top.delete(0, END)
    result_bottom.config(state='readonly')
    result_top.config(state='readonly')


but_delete_all = Button(root,
                        text='C',
                        height=2,
                        width=7,
                        font='Montserrat 9',
                        bg='#131212',
                        foreground='white',
                        borderwidth=0,
                        command=press_but_delete_all)
but_delete_all.place(relx=0.38,
                     rely=0.36,
                     anchor=CENTER)


def press_but_delete_one_symbol():
    result_bottom.config(state='normal')
    result_bottom.delete(len(result_bottom.get()) - 1)
    result_bottom.config(state='readonly')


but_delete_one_symbol = Button(root,
                               text='←',
                               height=2,
                               width=7,
                               font='Montserrat 9',
                               bg='#131212',
                               foreground='white',
                               borderwidth=0,
                               command=press_but_delete_one_symbol)
but_delete_one_symbol.place(relx=0.62,
                            rely=0.36,
                            anchor=CENTER)


def press_but_delete_last_entry():
    result_bottom.config(state='normal')
    result_bottom.delete(0, END)
    result_bottom.config(state='readonly')


but_delete_last_entry = Button(root,
                               text='CE',
                               height=2,
                               width=7,
                               font='Montserrat 9',
                               bg='#131212',
                               foreground='white',
                               borderwidth=0,
                               command=press_but_delete_last_entry)
but_delete_last_entry.place(relx=0.14,
                            rely=0.36,
                            anchor=CENTER)

mainloop()
