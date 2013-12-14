#------filename pick up-------
# -*- coding: utf-8 -*-

import os			#导入os模块
filenames = os.listdir ( os.getcwd() )		#获取当前目录下的文件（夹）名，并创建列表
for name in filenames:
    print  (name)
    filenames [ filenames.index (name) ] = name[:-4]	#删去文件名的最后四个字符
out = open ('names.txt' , 'w')		#以写方式打开文件
for name in filenames:
    out.write (name+'\n')		#写入文件
out.write ( 'by Luctie' )		#添加个人签名
out.close ()
