# -*- coding: utf-8 -*-

from tkinter import *  
from tkinter.messagebox import *  
from tkinter import filedialog
import tkinter as tk
  
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
        r = filedialog.askopenfilename(title='打开文件', filetypes=[('*.txt', '*.xlsx'), ('All Files', '*')])
        self.deductPrice.set(r)
        #print(self.r)
        #print(self.var_path)
        
        
    def opendnafile(self):
        #fq = filedialog.askopenfilenames(title = '打开fastq文件',filetypes=[('*.fa', '*.fq', '*.fasta','*.fastq'), ('All Files', '*')], )
        #fq = filedialog.askopenfilenames(title = '打开fastq文件',filetypes=[('All Files', '*')], )
        fq = filedialog.askdirectory()
        self.sellPrice.set(fq)
        #print(self.r)
        
    def find_table_data(self):
        r_path = self.deductPrice.get()
        print(r_path)
        
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)  
        Button(self, text='File Open', command=self.openfile).grid(row=1,column=1,stick = W,pady=10)
        Entry(self, textvariable=self.deductPrice,width=80).grid(row=2, column=1, stick=E,columnspan=3)
        Button(self, text='File Open table', command=self.opendnafile).grid(row=3,column=1,stick = W,pady=10)
        Entry(self,textvariable= self.sellPrice,width=80).grid(row=4,column=1,stick=E,columnspan=3)
        #Label(self, text = '患者名字: ').grid(row=1, stick=W, pady=10)  
        #Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)  
        #Label(self, text = '样本ID: ').grid(row=2, stick=W, pady=10)  
        #Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)  
        #Label(self, text = '录入时间: ').grid(row=3, stick=W, pady=10)  
        #Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)  
        #Label(self, text = '治疗时间: ').grid(row=4, stick=W, pady=10)  
        #Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)  
        #Button(self, text='录入').grid(row=6, column=1, stick=E, pady=10)  
         
        #Label(self, textvariable = self.var_path).grid(row=4, stick=W, pady=10)  
        #print(self.deductPrice)
        
  
  
class QueryFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.itemName = StringVar()  
        self.createPage()
        self.var_path = StringVar()
  
    def createPage(self):  
        Label(self, text='查询界面').pack()  
        #print(self.var_path.get)
  
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