from pickle import FALSE
import tkinter as tk
from tkinter import HORIZONTAL, ttk
from datetime import date

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("400x400")
        self.title('Julius')
        # set up variable
        self.month_info = {
            1:0,
            2:31,
            3:59,
            4:90,
            5:120,
            6:151,
            7:181,
            8:212,
            9:243,
            10:273,
            11:304,
            12:334,
        }

        self.month_info_leap = {
            1:0,
            2:31,
            3:60,
            4:91,
            5:121,
            6:152,
            7:182,
            8:213,
            9:244,
            10:274,
            11:305,
            12:335,
        }

        # set up variable
        # create widget
        self.create_wigets()
        self.getJulius(self)

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # Today Label
        today_date_label = ttk.Label(self,  text='Today normal:')
        today_date_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # Today Value
        today_date_value = ttk.Label(self, text= date.today().strftime("%B %d, %Y") )
        today_date_value.grid(column=1, row=0, sticky=tk.W, **paddings)

        # Today Julius
        self.today_julius_label = ttk.Label(self,  text='Today In Julius:')
        self.today_julius_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        # Today Julius Value
        self.today_julius_value = ttk.Label(self)
        self.today_julius_value.grid(column=1, row=1, sticky=tk.W, **paddings)


    def getJulius(self, *args):
        today = date.today()
        day = today.day
        month = today.month
        year = today.year
        if(year%4==0):
            selectedMonthValue = self.month_info_leap
        else:
            selectedMonthValue = self.month_info
        base = selectedMonthValue[month]
        fin = base + day
        self.today_julius_value['text'] = f'{fin}'



if __name__ == "__main__":
    app = App()
    app.mainloop()