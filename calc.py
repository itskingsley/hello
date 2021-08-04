from tkinter import *
root = Tk()
root.title('Simple Calculator')

#Background Colour
root.configure(bg='blue')

#icon
photo = PhotoImage(file = "sul wisha2.png")
root.iconphoto(False, photo)

#Functions
def get_numbers (numbers):
    num_numbers = e.get()



#Input box
e = Entry(root, borderwidth=10, width=40)
e.grid(row=0, columnspan=4, column=0)


#Top Level Buttons
btn_clear = Button(root, text='Clear', fg='black', bg='blue')
btn_clear.grid(row=1, column=0)

btn_divide = Button(root, text='Divide', fg='black', bg='blue')
btn_divide.grid(row=1, column=1)

btn_multplication = Button(root, text='Multplication', fg='black', bg='blue')
btn_multplication.grid(row=1, column=2)

btn_delete = Button(root, text='Delete', fg='black', bg='blue')
btn_delete.grid(row=1, column=3)

#NUMBER LEVEL BUTTONS
btn_7 = Button(root, text='7',  fg='black', bg='blue', command=lambda :get_numbers(7))
btn_7.grid(row=2, column=0)

btn_8 = Button(root, text='8', fg='black', bg='blue', command=lambda :get_numbers(8))
btn_8.grid(row=2, column=1)

btn_9 = Button(root, text='9', fg='black', bg='blue', command=lambda :get_numbers(9))
btn_9.grid(row=2, column=2)

btn_4 = Button(root, text='4', fg='black', bg='blue', command=lambda :get_numbers(4))
btn_4.grid(row=3, column=0)

btn_5 = Button(root, text='5', fg='black', bg='blue', command=lambda :get_numbers(5))
btn_5.grid(row=3, column=1)

btn_6 = Button(root, text='6', fg='black', bg='blue', command=lambda :get_numbers(6))
btn_6.grid(row=3, column=2)

btn_1 = Button(root, text='1', fg='black', bg='blue', command=lambda :get_numbers(1))
btn_1.grid(row=4, column=0)

btn_2 = Button(root, text='2', fg='black', bg='blue', command=lambda :get_numbers(2))
btn_2.grid(row=4, column=1)

btn_3 = Button(root, text='3', fg='black', bg='blue', command=lambda :get_numbers(3))
btn_3.grid(row=4, column=2)

btn_Percentage = Button(root, text='%', fg='black', bg='blue')
btn_Percentage.grid(row=5, column=0)

btn_0 = Button(root, text='0', fg='black', bg='blue', command=lambda :get_numbers(0))
btn_0.grid(row=5, column=1)

btn_Decimal = Button(root, text='.', fg='black', bg='blue')
btn_Decimal.grid(row=5, column=2)

#signs
btn_minus = Button(root, text='-', fg='black', bg='blue')
btn_minus.grid(rowspan=3, row=2, columnspan=3, column=3)

btn_plus = Button(root, text='+', fg='black', bg='blue')
btn_plus.grid(rowspan=3, row=3, columnspan=3, column=3)

btn_EQUALS = Button(root, text='=', fg='black', bg='blue')
btn_EQUALS.grid(rowspan=2, row=4, columnspan=7, column=3)

root.mainloop()