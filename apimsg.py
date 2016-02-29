#-*-coding:utf8;-*-
#qpy:3
#qpy:console


import android
h=android.Android()

def msg(m=None):
    if m:
       p=m
    else:
       p="This is console module"
    h.makeToast(p)
 
 
msg("hgfy")

#h.vibrate(300*0.5)
#使手机震动，以毫秒为单位，默认300毫秒

h.setClipboard("我是复制内容")

a=h.wifiGetConnectionInfo()
print(type(a))
#h.toggleAirplaneMode(True)

#h.toggleWifiState()
#如果无线被打开则关闭，如果是关掉则打开


import time
time.sleep(12)

print(a)
h.wakeLockAcquireFull()



