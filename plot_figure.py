# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tushare as ts
import time
import os

plt.rcParams['font.family'] = 'SimHei'
__author__ = 'WellenWoo'

class plt_fig():
    def __init__(self):
        tt = time.gmtime()
        self.today = str(tt[0]) + str(tt[1]) + str(tt[2])

    def cd_dir(self):
        path_now = os.getcwd()
        if path_now.endswith('data'):
            return None
        elif os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        os.chdir(r'data')
        
    def get_data(self,*args):
        self.cd_dir()
        f0 = self.today+'.xlsx'
        try:
            d1 = pd.read_excel(f0)
        except IOError:
            d0 = ts.realtime_boxoffice()
            d0.to_excel(f0)
            d1 = pd.read_excel(f0)
        d2 = d1.Irank
        d3 = d1.BoxOffice
        d4 = d1.MovieName
        d5 = d1.sumBoxOffice
        return d2,d3,d4,d5
    
    def day_boxoffice(self,title = u'本日票房',ylabel = u'票房\万元',*args):
        if len(args)>0:
            irank,box,name,sumbox = self.get_data(args[0])
        else:
            irank,box,name,sumbox = self.get_data()        
        self.plt_bar(irank,box,name,title,ylabel)
        
    def sum_boxoffice(self,title =u'本日影片累计票房',ylabel = u'累计票房\万元'):
        irank,box,name,sumbox = self.get_data()
        self.plt_bar(irank,sumbox,name,title,ylabel)

    def day_boxoffice_pre(self,title = u'本日票房占比',*args):
        if len(args)>0:
            irank,box,name,sumbox = self.get_data(args[0])
        else:
            irank,box,name,sumbox = self.get_data()        
        self.plt_pie(box,name,title)

    def sum_boxoffice_pre(self,title = u'累计票房占比'):
        irank,box,name,sumbox = self.get_data()
        self.plt_pie(sumbox,name,title)
        
    def plt_bar(self,xdata,ydata,xticks,title,ylabel):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        bar_width = 0.65

        ax.bar(xdata,ydata,bar_width,color = 'r')
        plt.xticks(xdata+bar_width/2,xticks)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        plt.grid()
        fig.autofmt_xdate()
        plt.tight_layout()
        plt.show()

    def plt_pie(self,xdata,ydata,title):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax = fig.add_subplot(111)
        ax.pie(xdata,labels = ydata,autopct = '%1.1f%%',shadow = True)
        ax.set_title(title)
        plt.show()
            
class plt_fig_month(plt_fig):
        
    def get_data(self,*args):
        self.cd_dir()
        month = args[0]
        f0 = month+'.xlsx'
        try:
            d1 = pd.read_excel(f0)
        except IOError:
            d0 = ts.month_boxoffice(month)
            d0.to_excel(f0)
            d1 = pd.read_excel(f0)
        d2 = d1.Irank[:-1]
        d3 = d1.boxoffice[:-1]
        d4 = d1.MovieName[:-1]
        d5 = d1.avgboxoffice[:-1] 
        return d2,d3,d4,d5

