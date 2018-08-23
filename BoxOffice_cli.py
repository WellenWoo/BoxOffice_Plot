#-*- coding: utf-8 -*-

"""
本程序可获取国内当天票房数据，
并将其可视化。
Usage:
Today boxoffice:
  python BoxOffice_cli.py
  
Sum boxoffice:
  python BoxOffice_cli.py -sum
  
Month boxoffice:
  python BoxOffice_cli.py -m month("xxxx-xx")
  
Taipei weekend boxoffice:
  python BoxOffice_cli.py -tw
  
US weekend boxoffice:
  python Boxoffice_cli.py -us
"""

import sys
from plot_figure import plt_fig,plt_fig_month

from tw_boxoffice import tw_fig
from us_boxoffice import us_fig

__author__ = 'wellenwoo'
__mail__ = 'wellenwoo@163.com'

class Main(object):
    def __init__(self):
        """预定义参数"""
        self.fig = plt_fig()
        self.fig_month = plt_fig_month()
        
        self.tw_fig = tw_fig()
        self.us_fig = us_fig()
        
    def day_boxoffice(self):
        self.fig.day_boxoffice(title = u'本日票房',ylabel = u'票房\万元')

    def sum_boxoffice(self):
        self.fig.sum_boxoffice(title =u'本日影片累计票房',ylabel = u'累计票房\万元')

    def month_boxoffice(self,month):
        self.fig_month.day_boxoffice(u'月份票房',u'票房\万元',month)       

    def tw_boxoffice(self):
        self.tw_fig.weekend()

    def us_boxoffice(self):
        self.us_fig.weekend()
        
if __name__ == '__main__':
    print(__doc__)
    main = Main()
    if len(sys.argv)==1:
        main.day_boxoffice()
        
    elif len(sys.argv)==2:
        action = sys.argv[1]
        if action =="-sum":
            main.sum_boxoffice()
        elif action =="-tw":
            main.tw_boxoffice()
        elif action =="-us":
            main.us_boxoffice()

    elif len(sys.argv)==3:
        month = sys.argv[2]
        main.month_boxoffice(month)
        
    else:
        print(__doc__)
