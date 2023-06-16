import customtkinter as ctk
from tkinter import messagebox


class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()
        # window
        self.geometry('400x450')
        self.title('Calculator')
        ctk.set_appearance_mode('System')

        # configure grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=25)
        self.columnconfigure(0, weight=1)

        # text box for calculations
        self.txt_calculations = ctk.CTkTextbox(self, height=170, font=("Helvetica", 24))
        self.txt_calculations.grid(column=0, row=0, padx=10, pady=10, sticky='new')
        
        # frame for all buttons
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')

        self.btn_frame.rowconfigure((0, 1, 2, 3), weight=1)
        self.btn_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

        # buttons
        # number buttons 
        self.btn_1 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='1', command=lambda: self.input_numbers_operators('1'))
        self.btn_2 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='2', command=lambda: self.input_numbers_operators('2'))
        self.btn_3 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='3', command=lambda: self.input_numbers_operators('3'))
        self.btn_4 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='4', command=lambda: self.input_numbers_operators('4'))
        self.btn_5 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='5', command=lambda: self.input_numbers_operators('5'))
        self.btn_6 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='6', command=lambda: self.input_numbers_operators('6'))
        self.btn_7 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='7', command=lambda: self.input_numbers_operators('7'))
        self.btn_8 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='8', command=lambda: self.input_numbers_operators('8'))
        self.btn_9 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='9', command=lambda: self.input_numbers_operators('9'))
        self.btn_0 = ctk.CTkButton(self.btn_frame, height=30, width=30, text='0', command=lambda: self.input_numbers_operators('0'))
        self.btn_open = ctk.CTkButton(self.btn_frame, height=30, width=30, text='(', command=lambda: self.input_numbers_operators('('))
        self.btn_close = ctk.CTkButton(self.btn_frame, height=30, width=30, text=')', command=lambda: self.input_numbers_operators(')'))

        self.btn_1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.btn_2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.btn_3.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        self.btn_4.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.btn_5.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        self.btn_6.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        self.btn_7.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.btn_8.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
        self.btn_9.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
        self.btn_0.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
        self.btn_close.grid(row=3, column=2, padx=5, pady=5, sticky='nsew')
        self.btn_open.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')


        # operator buttons
        self.btn_add = ctk.CTkButton(self.btn_frame, height=30, width=30, text='+', command=lambda: self.input_numbers_operators('+'))
        self.btn_subtract = ctk.CTkButton(self.btn_frame, height=30, width=30, text='-', command=lambda: self.input_numbers_operators('-'))
        self.btn_divide = ctk.CTkButton(self.btn_frame, height=30, width=30, text='/', command=lambda: self.input_numbers_operators('/'))
        self.btn_multiply = ctk.CTkButton(self.btn_frame, height=30, width=30, text='*', command=lambda: self.input_numbers_operators('*'))
        self.btn_period = ctk.CTkButton(self.btn_frame, height=30, width=30, text='.', command=lambda: self.input_numbers_operators('.'))

        self.btn_add.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')
        self.btn_subtract.grid(row=0, column=4, padx=5, pady=5, sticky='nsew')
        self.btn_divide.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
        self.btn_multiply.grid(row=1, column=4, padx=5, pady=5, sticky='nsew')
        self.btn_period.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')

        # calculate and clear button
        self.btn_calc = ctk.CTkButton(self.btn_frame, height=30, width=30, text='=', command=self.display_result)
        self.btn_clear = ctk.CTkButton(self.btn_frame, height=30, width=30, text='C', command=self.clear_textbox)
        self.btn_delete = ctk.CTkButton(self.btn_frame, height=30, width=30, text='Del', command=self.delete_one_character)

        self.btn_calc.grid(row=2, column=4, padx=5, pady=5, sticky='nsew')
        self.btn_clear.grid(row=3, column=3, padx=5, pady=5, sticky='nsew')
        self.btn_delete.grid(row=3, column=4, padx=5, pady=5, sticky='nsew')

    def input_numbers_operators(self, text):
        self.txt_calculations.insert('end', text)

    def display_result(self):
        result = self.calculate_result()
        self.txt_calculations.delete('0.0', 'end')
        self.txt_calculations.insert('0.0', str(result))

    def calculate_result(self):
        calculations = self.validate_calculations()
        try:
            result = eval(calculations)
        except ZeroDivisionError:
            result = 'You cannot divide by 0'
        return result

    def validate_calculations(self):
        # checks if input consists of numbers and acceptable operators
        calculations = self.txt_calculations.get('0.0', 'end').strip()
        calc_copy = calculations[:]
        for operator in '+-/*().':
            calc_copy = calc_copy.replace(operator, '')
        
        if not calc_copy.isnumeric():
            messagebox.showerror('Wrong input', 'Something went wrong!')
        else:
            return calculations

    def clear_textbox(self):
        self.txt_calculations.delete('0.0', 'end')

    def delete_one_character(self):
        self.txt_calculations.delete('end-2c', 'end')


if __name__ == '__main__':
    pass
