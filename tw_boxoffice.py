#-*- coding: utf-8 -*-

import pandas as pd

from plot_figure import plt_fig

url = 'http://app2.atmovies.com.tw/boxoffice/twweekend/'

'''获取台北周末票房'''

class tw_fig(plt_fig):

    def table2excel(self,url):
        tbs = pd.read_html(url,header = 0,index_col = 0,skiprows = 0)
        df = tbs[1]
        df.columns = [u'MovieName',u'weekbox',u'sumbox',u'lastweek',u'weeknum',u'nouse']
        df.index.name = u'irank'

        df1 = df.fillna(method = 'bfill')
        df1 = df1.dropna(axis = 1,how = 'all')
        df1.weekbox = df1.weekbox.str.replace('$','')
        df1.sumbox = df1.sumbox.str.replace('$','')

        df1.sumbox = df1.sumbox.str.replace(',','')
        df1.weekbox = df1.weekbox.str.replace(',','')
    
        df1.sumbox = pd.to_numeric(df1.sumbox)
        df1.weekbox = pd.to_numeric(df1.weekbox)
    
        n = range(1,21)
        df2 = df1[df1.index.isin(n)]
        return df2

    def get_data(self,area,url):
        self.cd_dir()
        f0 = str(area)+'_'+self.today+'.xlsx'
        try:
            df = pd.read_excel(f0)
        except IOError:
            df = self.table2excel(url)
            df.to_excel(f0)
        irank = df.index
        weekbox = df.weekbox
        name = df.MovieName
        title = str(area)+self.today+'boxoffice'
        return irank,weekbox,name,title

    def weekend(self):
        irank,weekbox,name,title = self.get_data('tw',url)
        self.plt_bar(irank,weekbox,name,title,u'票房\万元')
