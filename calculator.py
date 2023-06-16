import customtkinter as ctk


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
        self.txt_calculations = ctk.CTkTextbox(self, height=170)
        self.txt_calculations.grid(column=0, row=0, padx=10, pady=10, sticky='new')
        self.txt_calculations.configure(state='disabled')
        
        # frame for all buttons
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')

        self.btn_frame.rowconfigure((0, 1, 2, 3), weight=1)
        self.btn_frame.columnconfigure((0, 1, 2), weight=1)
        self.btn_frame.columnconfigure((3, 4), weight=2)

        # buttons
        # number buttons 
        self.create_number_buttons()

        # operator buttons
        self.btn_add = ctk.CTkButton(self.btn_frame, height=30, width=30, text='+')
        self.btn_subtract = ctk.CTkButton(self.btn_frame, height=30, width=30, text='-')
        self.btn_divide = ctk.CTkButton(self.btn_frame, height=30, width=30, text='/')
        self.btn_multiply = ctk.CTkButton(self.btn_frame, height=30, width=30, text='*')

        self.btn_add.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')
        self.btn_subtract.grid(row=0, column=4, padx=5, pady=5, sticky='nsew')
        self.btn_divide.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
        self.btn_multiply.grid(row=1, column=4, padx=5, pady=5, sticky='nsew')

        # calculate and clear button
        self.btn_calc = ctk.CTkButton(self.btn_frame, height=30, text='=')
        self.btn_clear = ctk.CTkButton(self.btn_frame, height=30, text='C')

        self.btn_calc.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky='nsew')
        self.btn_clear.grid(row=3, column=3, columnspan=2, padx=5, pady=5, sticky='nsew')

    def create_number_buttons(self):
        button_num = 1
        for row in range(4):
            for col in range(3):
                if row != 3:
                    new_btn = ctk.CTkButton(self.btn_frame, height=30, width=30, text=str(button_num))
                    button_num += 1
                else:
                    if col == 0:
                        new_btn = ctk.CTkButton(self.btn_frame, height=30, width=30, text='(')
                    if col == 1:
                        new_btn = ctk.CTkButton(self.btn_frame, height=30, width=30, text='0')
                    if col == 2:
                        new_btn = ctk.CTkButton(self.btn_frame, height=30, width=30, text=')')
                new_btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
