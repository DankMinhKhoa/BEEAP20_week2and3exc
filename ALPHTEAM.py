import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("ALPHATEAM")# title changed ,Mohsen Fadaee and Jack hocock
        # setting window size# size changed from W 700, h 500 to W900 ,h 700
        width = 900
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__LoudFile = tk.Button(root)
        self.__LoudFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__LoudFile["font"] = ft
        self.__LoudFile["fg"] = "#000000"
        self.__LoudFile["justify"] = "center"
        self.__LoudFile["text"] = "Loud file"# changed Button
        self.__LoudFile.place(x=70, y=50, width=70, height=25)
        self.__LoudFile["command"] = self.__GButton_450_command
        
        self.__Combobox = ttk.Combobox(root)
        self.__Combobox.place(x=550, y=50, width=80, height=25)
        self.__Combobox.bind("<<ComboboxSelected>>", self.__comboBoxCb)
        

        self.__FileName = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__FileName["font"] = ft
        self.__FileName["fg"] = "#333333"
        self.__FileName["justify"] = "center"
        self.__FileName["text"] = "file name"#Changed Label 
        self.__FileName.place(x=150, y=50, width=70, height=25)

        self.__SelectTown = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__SelectTown["font"] = ft
        self.__SelectTown["fg"] = "#333333"
        self.__SelectTown["justify"] = "center"
        self.__SelectTown["text"] = "Select town"#Changed Label 
        self.__SelectTown.place(x=450, y=50, width=70, height=25)
        
        
        # these canvases are broken, fix them
     

        
        self.__GLineEdit_517 = tk.Canvas(root)
        self.__GLineEdit_517.place(x=50, y=130, width=234, height=140)
        
       

        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=239, height=139)

        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=290, width=233, height=157)

        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

    def __GButton_450_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__GListBox_563['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            root = tk.Tk()
            root.title("NOPEFILE")
            root.geometry("250x50")
            
            myFun =tk.Frame(root)
            myFun.pack()
            
            button = tk.Button(myFun)
            button["text"]= "NOPE"
             
            root.mainloop()
         
          
            #print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__GListBox_563.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
