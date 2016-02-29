# -*- coding:utf-8 -*-
  

import time,sys,socket,easygui,os,threading





mkf = time.strftime('%Y-%m-%d'+'.txt')
ctim = time.strftime('%H:%M:%S')
xstim = time.strftime ('%H')
fztim = time.strftime ('%M')
datafile= open('\\\\theone\\70gx\\'+mkf,'a+') 

'''
def taskkill():
  
    #隐藏pythonGUI windows窗口终端
    import win32api, win32gui
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)
  
    
    #time.sleep(10)
    #i=os.system('taskkill /f /im cmd.exe')#关掉终端
    #if i !=1:
     #   taskkill()
    #print i
'''

     

	
def dc():

    if ( int(xstim) == 10  and  int(fztim)>45 ):
        easygui.msgbox("请调整成为北京时间，时区为UTC+08:00","上午10:45以后不点餐")        
        sys.exit()          
    

    elif ( int(xstim) < 11 ):
                
        allname = ["餐厅名和菜名:","你的名字:","你的联系电话:"]
        enn = easygui.multenterbox('请输入信息(其中任意两项必填)',ctim,allname)
       # os.popen(".\\flashscreem01.exe").read()
    

        if  enn == None :
            easygui.msgbox("点餐取消",ctim)
            pass
        elif  enn[0] == enn[2] == '':
            easygui.msgbox("点餐取消",ctim)
            pass
        elif  enn[1] == enn[2] == '':
            easygui.msgbox("点餐取消",ctim)
            pass
        elif enn[0] == enn[1]  == '':
            easygui.msgbox("点餐取消",ctim)
            pass
        else:
              import sys
              reload(sys)
              sys.setdefaultencoding('GBK')
              datafile.write("\n"+enn[0]+'\n'+enn[1]+'\n'+enn[2]+'\n'+ctim+"\n\n")
              datafile.close()
              time.sleep(3)
              easygui.msgbox('点餐成功',title=enn[1])

    else:
         easygui.msgbox("请调整成为北京时间，时区为UTC+08:00","上午10:45以后不点餐")
         import sys
         sys.exit()


def seemenu():
      time.sleep(5)
      copy='echo d | xcopy \\\\theone\\gx\\tu c:\\menu /D /S /Y /E /Q' #复制共享的图片菜单
      view='rundll32.exe c:\\windows\\System32\\shimgvw.dll,ImageView_Fullscreen c:\\menu\\img9.jpg'
      n=os.system(copy)
      if n !=0:
          sys.exit()
      #os.system(view)
      os.popen(view).read() #这样调用dos命令就不会出现终端黑框

def sp():
     cmd = ".\\flashscreem.exe "+ ctim
     #print cmd
     os.popen(cmd).read()  


#cmd = ".\\flashscreem01.exe "+ ctim;
#print cmd;
  
       
if socket.gethostbyname('theone') == '192.168.67.234' :
      T = []
      t1 = threading.Thread(target=dc)
      T.append(t1)
      t2 = threading.Thread(target=sp)
      T.append(t2)
      t3 = threading.Thread(target=seemenu)
      T.append(t3)
      for t in T:
          t.setDaemon(True)
          t.start()
      t.join()

elif not socket.gethostbyname('theone') == '192.168.67.234' :
    easygui.msgbox("网络不存在,请联系管理员","请检查网络")
    sys.exit()



