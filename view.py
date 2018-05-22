# -*- coding: utf-8 -*-

from tkinter import *  
from tkinter.messagebox import *  
from tkinter import filedialog
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
  
class InputFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.itemName = StringVar()  
        self.importPrice = StringVar()  
        self.sellPrice = StringVar()  
        self.deductPrice = StringVar()  
        self.createPage() 
        self.varpath = StringVar()
        
    
        
    def openfile(self):
        r = filedialog.askopenfilename(title='打开文件', filetypes=[('Text file','*.txt'), ('All Files', '*')])
        self.deductPrice.set(r)
        #print(self.r)
        #print(self.var_path)
        
        
    def opendnafile(self):
        fq = filedialog.askdirectory()
        self.sellPrice.set(fq)
        print(sellPrice)
        
    def find_table_data(self):
        r_path = self.deductPrice.get()
        print(r_path)
        
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)  
        Button(self, text='File Open', command=self.openfile).grid(row=1,column=1,stick = W,pady=10)
        Entry(self, textvariable=self.deductPrice,width=80).grid(row=2, column=1, stick=E,columnspan=3)
        Button(self, text='File Open table', command=self.opendnafile).grid(row=3,column=1,stick = W,pady=10)
        Entry(self,textvariable= self.sellPrice,width=80).grid(row=4,column=1,stick=E,columnspan=3)
        Button(self, text='Run', command=self.opendnafile).grid(row=5,column=1,stick = W,pady=10)

     
  
  
class QueryFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.itemName = StringVar()  
        self.createPage()
        self.var_path = StringVar()
        #self.update_table()

    def update_table(self):
        #self.clear()
        tv = ttk.Treeview(self, height =10,columns=('c1','c2','c3'))
        for i in range(1000):
            tv.insert('',i,values=('a'+str(i),'b'+str(i),'c'+str(i)))
        tv.pack()
        #tv.grid(row=1,column=1)

    def createPage(self):  
        Label(self, text='查询界面').pack()
        Button(self, text='File Open table', command=self.update_table).pack()
        
  
class CountFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
  
    def createPage(self):  
        Label(self, text='统计界面').pack()  
  
  
class AboutFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
  
    def createPage(self):  
        Label(self, text='关于界面').pack()  
