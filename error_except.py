import easygui as g
while 1:
    try:
        a=int(input('请输入被除数'))
        r=10/a
        print('result:',r)
    except ValueError  as e:
        print('输入类型错误:',e)
        continue
    except ZeroDivisionError as e:
        g.msgbox('除数不能为0')
        continue
    else:
        print('no error!')
        break
    finally:
        print('干得漂亮')
    
    
