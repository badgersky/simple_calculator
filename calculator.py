import customtkinter as ctk


class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()
        # window
        self.geometry('400x400')
        self.title('Calculator')
        ctk.set_appearance_mode('System')

        # configure grid
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # text box for calculations
        self.txt_calculations = ctk.CTkTextbox(self, height=120)
        self.txt_calculations.grid(column=0, row=0, padx=10, pady=10, sticky='new')
        
        # frame for all buttons
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.grid(column=0, row=1, padx=10, pady=10, sticky='nsew')