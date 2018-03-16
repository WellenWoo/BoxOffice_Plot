#-*- coding: utf-8 -*-

import pandas as pd

from tw_boxoffice import tw_fig

url = 'http://app2.atmovies.com.tw/boxoffice/usweekend/'

'''获取美国周末票房'''

class us_fig(tw_fig):

    def weekend(self):
        irank,weekbox,name,title = self.get_data('us',url)
        self.plt_bar(irank,weekbox,name,title,u'票房\万元')
