import easygui as g
import sys
while 1:
    g.msgbox('准备好选择国家了吗!!!')
    msg='请选择出生国家'
    title='选择国家'
    choices=['魏国','蜀国','吴国']
    choice=g.choicebox(msg,title,choices)
    g.msgbox('您的选择是:'+str(choice),'ok')
    if g.ccbox(msg='你需要重新选择吗',title='请选择'):
	    pass
    else:
	    sys.exit(0)
