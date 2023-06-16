import customtkinter as ctk


class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()
        # window
        self.geometry('400x400')
        self.title('Calculator')
        ctk.set_appearance_mode('System')
