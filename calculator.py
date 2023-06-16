import customtkinter as ctk


class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()
        # window
        self.geometry('400x400')
        self.title('Calculator')
        ctk.set_appearance_mode('System')

        # text box for calculations
        self.txt_calculations = ctk.CTkTextbox(self, height=120, width=380)
        self.txt_calculations.grid(column=0, row=0, padx=10, pady=10)
        