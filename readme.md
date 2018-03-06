# **BoxOffice_Plot**

0. 本程序可获取国内当天票房和近期历史电影票房数据，并将其可视化。

1. day_boxoffice按钮：获取当天票房数据并以excel表格形式保存在data文件夹下，
   并据此绘制当日票房榜及当天上映电影的累计票房柱状图；
   
   day_boxoffice_pre按钮:获取当天票房数据，并据此绘制当天票房百分占比饼图及当天上映电影累计票房的百分占比饼图；
   
   month_boxoffice按钮：获取指定月份的票房数据，并绘制该月票房榜（以“xxxx-xx"形式输入指定月份）；
   
   month_boxoffice_pre按钮：获取指定月份的票房数据，并绘制该月上映电影票房的百分之百饼图。
   
2. 票房数据均采集自第三方网站，本程序不负责其真实性或精确性。

## Note 注意事项:
需安装以下第三方库，本脚本才能正常运行：
wx,tushare,matplotlib,pandas,numpy,seaborn。

## Feedback:
有任何疑问或建议欢迎[反馈](https://github.com/WellenWoo/BoxOffice_Plot.git)。

## Todo:
1. 增加北美地区票房数据的可视化功能.



