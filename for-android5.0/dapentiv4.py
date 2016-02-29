#-*-coding:utf8;-*-
#qpy:3
#qpy:console

cmd=__import__("os")
stat=cmd.system("ping -c 2 www.dapenti.com > /dev/null 2>&1")
#这里用到bash的返回特性，用来判断一条命令是否正确执行完毕

if (stat == 512):  
        print("\n\t***请查看网络是否连接***\n")
        exit()

def down(url=""):
    import httplib2
    return httplib2.Http().request(url)[1]

www="http://www.dapenti.com/blog/"
index=www+"index.asp"

html=down(index)
html=str(html)

from datetime import date
now=date.today()
now=now.strftime("%y%m%d")
#将当天日期格式化为字符型
now="20"+now
#在字符前添加字符
#now=int(now)+1
#ow=str(now)

i=html.count(now)
#目标网页有关键字即当前日期
key='ref=(.*) title'
def tuguaurl(s,n,k1,k2):
    temp=str(s)
    adds=[]
    print(n)
    for i in range(n):
         #if (n == 1):
         pos=temp.find(k1)+len(k1)
         path=temp[pos-100:pos+108]
         print (path)
         pos=pos+len(path)
         temp=temp[pos:]
         import re
         adds.append(re.findall(k2,path))
    return adds
             
listurl=tuguaurl(html,i,now,key)
if (len(listurl) < 1 ): 
           import apimsg
           apimsg.msg("今天还没出新闻")
           exit()
print(www+','.join(listurl[0]))          
html=down(www+",".join(listurl[0]))
print (type(html))
print ("#######################")
#open("/sdcard/dapenti/"+now+".html","wb").write(html)
#html=str(html)

#print(len(html))

i=html.count(b'<img')
listurl=tuguaurl(html,i,'<img','src="(.*)" alt=""')
print(i)
print(len(listurl))
print("*******************************\n")
i=0
ptimglist=[]
for it in listurl:
     it=','.join(it)
     if (it.find("jpg") > 0 ):
              print (it)
              ptimglist.append(it)
              i=str(i)
              
              import os
              if (os.path.isdir("/sdcard/dapenti/"+now+"/")):
                     pass
              else:
                     os.mkdir("/sdcard/dapenti/"+now+"/")  
              path="/sdcard/dapenti/"+now+"/"+i+".jpg"           
              open(path,"wb").write(down(it))
              
              html=html.replace(it.encode('utf8'),path.encode("utf8"))
              
     i=int(i)+1 
     open("/sdcard/dapenti/"+now+".html","wb").write(html)
'''
print (len(ptimglist))
print (type(html))

html=eval(html)
print (type(html))
open("/sdcard/dapenti/ti.html","w").write(str(html))
'''
