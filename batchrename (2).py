#------batchrename----------
#-*- coding: utf-8 -*-

import os

def batchdo ( path ):		#批量处理
    os.chdir( path )		#改变当前目录
    files = os.listdir( path )
    nfiles = os.listdir( path )
    num = 0
    out = open( 'record_of_work.txt' , 'w' )
    out.write( 'all names of files before renaming:\n\n' )
    for item in nfiles:
        if item == ( 'p.py' or 'record_of_work.txt' ):	#在列表中删去本程序文件名及生成文件名
            num -= 1
            del nfiles[ num ] , files[ num ]
        else:
            out.write( item + '\n' )
    select = raw_input( '\nplease choose a way of renaming:\n1 for adding from the left\n2 for adding from the right without the extension included\n' )
    if int( select ) == 1:		#选择重命名方式
        rel( files , nfiles )
    elif int( select ) == 2:
        rer( files , nfiles )
    else:		#操作错误，程序停止运行
        print ( '\n\nINPUT ERROR!ACTION ABORTED!' )
        out.close()
        out = open( 'record_of_work.txt' , 'w' )
        out.write( 'INPUT ERROR!PROGRAM FAILED TO RENAME FILES IN BULK!' )
    out.write( '\n\nall names of files after trying renaming:\n\n' )
    files = os.listdir( path )
    for item in files:
        if item!=( 'p.py' or 'record_of_work.txt' ):
            out.write( item + '\n' )
    out.write( '\nby Luctie' )
    out.close()

def rer( files , nfiles ):
    way1 = raw_input( '\nplease choose a filling way:\n1 for sequence number filling\n2 for character string filling\n' )
    while way1:
        if int( way1 ) == 1:
            num = 1
            width = raw_input( '\nplease input the filling width:\n' )
            '''while not isinstance( width , int ):
#判断数据类型
                width = raw_input( '\nINVALID VALUE!please input again!\n' )'''
            connec = raw_input( '\nplease input the connection:\ninput \"None\" or nothing to skip\n' )
            for item in nfiles:
                pos = item.rfind( '.' )		#寻找小数点的位置
                nfiles[ nfiles.index( item ) ] = item[ :pos ] + str( num ).zfill( int( width ) ) + str( connec ) + item[ pos: ] 	#用0填充
        elif int( way1 ) == 2:
            sign = raw_input( '\nplease input the string to add:\n' )
            connec = raw_input( '\nplease input the connection:\ninput \"None\" or nothing to skip\n' )
            for item in nfiles:
                pos = item.rfind( '.' )
                nfiles[ nfiles.index( item ) ] = item[:pos ] + str( connec ) + str( sign ) + item[ pos: ]
        else:
            continue
        break
    gorename( files , nfiles )

def rel( files , nfiles ):
    way1 = raw_input( '\nplease choose a filling way:\n1 for sequence number filling\n2 for character string filling\n' )
    while way1:
        if int( way1 ) == 1:
            num = 1
            width = raw_input( '\nplease input the filling width:\n' )
            '''while not isinstance( width , int ):
                width = raw_input( '\nINVALID VALUE!please input again!\n' )'''
            connec = raw_input( '\nplease input the connection:\ninput \"None\" or nothing to skip\n' )
            for item in nfiles:
                nfiles[ nfiles.index( item ) ] = str( num ).zfill( int( width ) ) + str( connec ) + item
        elif int( way1 ) == 2:
            sign = raw_input( '\nplease input the string to add:\n' )
            connec = raw_input( '\nplease input the connection:\ninput \"None\" or nothing to skip\n' )
            for item in nfiles:
                nfiles[ nfiles.index( item ) ] = str( sign ) + str( connec ) + item
        else:
            continue
        break
    gorename( files , nfiles )

def gorename( a , b ):		#负责重命名操作的核心函数
    confirm = raw_input( 'confirm to rename all the files in the folder??\ny|n\n' )
    if confirm == 'y':
        for item in a:
            os.rename( item , b[ a.index( item ) ] )
        print ( '\naction completed!\n' )
    else:
        print ( '\naction aborted!\n' )

def main():
    path = raw_input( 'input the path of the folder you\'d like to rename files in bulk:\n' )
    while path:
        if os.path.exists( path ):		#判断路径是否有效
            batchdo( path )
            break
        else:
            order = raw_input( '\nWARNING:\nthe path you input is not valid, program will function in default path!\nagree or not??\n' )
            if order == 'y':
                batchdo( os.getcwd() )	#使用当前地址
                break
            else:
                print ("\nthen check the path and input again!")
                path = raw_input( 'input the path of the folder you\'d like to rename files in bulk:\n' )
if __name__ == '__main__':
    main()
