#-*- coding: utf-8 -*-

import wx
import  wx.lib.dialogs
from collections import namedtuple

from plot_figure import plt_fig,plt_fig_month

from tw_boxoffice import tw_fig
from us_boxoffice import us_fig

__author__ = 'WellenWoo'
__mail__ = 'wellenwoo@163.com'

"""
本程序可获取国内当天票房和近期历史电影票房数据，
并将其可视化。
"""

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(600,-1))
        static_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        
        Size = namedtuple("Size",['x','y'])
        s = Size(100,50)

        """预定义参数"""
        self.fig = plt_fig()
        self.fig_month = plt_fig_month()
        
        self.tw_fig = tw_fig()
        self.us_fig = us_fig()
        
        b_labels = [
                    u'今日票房榜',
                      u'今日票房占比',
                      u'总票房榜',
                      u'总票房占比',
                      u'月票房榜',
                      u'月票房占比',
                    u'台北周末票房',
                    u'美国周末票房'
                        ]

        TipString = [ u'今日票房榜',
                      u'今日票房占比',
                      u'总票房榜',
                      u'总票房占比',
                      u'月票房榜',
                      u'月票房占比',
                      u'台北周末票房',
                      u'美国周末票房'
            ]
        funcs = [self.day_boxoffice,self.day_boxoffice_pre,
                 self.sum_boxoffice,self.sum_boxoffice_pre,
                 self.month_boxoffice,self.month_boxoffice_pre,
                 self.tw_boxoffice,self.us_boxoffice]
        
        """创建菜单栏"""
        filemenu = wx.Menu()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit\tCtrl+Q","Tenminate the program 退出")

        menuBar = wx.MenuBar ()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        
        '''创建按钮'''
#        self.sizer0 = wx.FlexGridSizer(rows=5, hgap=4, vgap=2) #wx2.8
        self.sizer0 = wx.FlexGridSizer(cols=2, hgap=4, vgap=2) #wx4.0
        buttons = []
        for i,label in enumerate(b_labels):
            b = wx.Button(self, id = i,label = label,size = (1.5*s.x,s.y))
            buttons.append(b)
            self.sizer0.Add(b)      

        '''菜单绑定函数'''
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)

        '''设置各控件的颜色、字体属性,绑定控件函数'''  
        for i,button in enumerate(buttons):
            button.SetForegroundColour('red')
            button.SetFont(static_font)
#            button.SetToolTipString(TipString[i]) #wx2.8
            button.SetToolTip(TipString[i])       #wx4.0
            button.Bind(wx.EVT_BUTTON,funcs[i])

        '''设置页面布局'''
        self.SetSizer(self.sizer0)
        self.SetAutoLayout(1)
        self.sizer0.Fit(self)
        
        self.CreateStatusBar()
        self.Show(True)
    
    def day_boxoffice(self,evt):
        self.fig.day_boxoffice(title = u'本日票房',ylabel = u'票房\万元')

    def sum_boxoffice(self,evt):
        self.fig.sum_boxoffice(title =u'本日影片累计票房',ylabel = u'累计票房\万元')

    def day_boxoffice_pre(self,evt):
        self.fig.day_boxoffice_pre(title = u'本日票房占比')

    def sum_boxoffice_pre(self,evt):
        self.fig.sum_boxoffice_pre(title = u'累计票房占比')

    def month_boxoffice(self,evt):
        month = self.get_month()
        title = u'{m}票房'.format(m = month)
        self.fig_month.day_boxoffice(title,u'票房\万元',month)

    def month_boxoffice_pre(self,evt):
        month = self.get_month()
        title = u'{m}票房占比'.format(m = month)
        self.fig_month.day_boxoffice_pre(title,month)
        
    def get_month(self):
        month = None
        dlg = wx.TextEntryDialog(
                self, u'please input the month输入月份',
                'month_boxoffice', 'oooo-oo')
        dlg.SetValue("2018-11")
        if dlg.ShowModal() == wx.ID_OK:
            month = dlg.GetValue()
        dlg.Destroy()
        if month is None:
            month = "2018-11"
        return month

    def tw_boxoffice(self,evt):
        self.tw_fig.weekend()

    def us_boxoffice(self,evt):
        self.us_fig.weekend()
    
    def OnExit(self,event):
        """退出函数"""
        self.Close()

    def raise_msg(self,msg):
        '''添加警告信息'''
        info = wx.AboutDialogInfo()
        info.Name = "Warning Message"
        info.Copyright = msg
        wx.AboutBox(info)
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None,'BoxOffice_Plot')
    app.MainLoop()
