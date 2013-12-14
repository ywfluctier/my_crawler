#------batchrename----------
#-*- coding: utf-8 -*-
import os

def batchdo ( path ):
    os.chdir( path )
    files = os.listdir( path )
    nfiles = os.listdir( path )
    num = 0
    for item in nfiles:
        num += 1
        if item == 'p.py':
            num -= 1
            continue
        if item == 'record_of_work.txt' :
            num -= 1
            continue
        nfiles[ nfiles.index( item ) ] = str( num ).zfill( 3 ) + item
        print ( item  )
    confirm = input( 'confirm to rename all the files in the folder??\ny|n\n' )
    if confirm == 'y':
        out = open( 'record_of_work.txt' , 'w')
        out.write( 'all names of files before renaming:\n\n' )
        for item in files:
            if item == 'record_of_work.txt' :
                continue
            print ( item )
            os.rename( item , nfiles[ files.index( item ) ] )
            out.write( item + '\n' )
        out.write( '\n\n& all names of the files after renaming:\n\n' )
        for item in nfiles:
            out.write( item + '\n' )
        out.close()

def main():
    path = input( 'input the path of the folder you\'d like to rename 

files in bulk:\n' )
    while path:
        if os.path.exists( path ):
            batchdo( path )
            break
        else:
            order = input( '\nWARNING:the path you input is not valid , program will function in default path!\nagree or not??\n' )
            if order == 'y':
                batchdo( os.getcwd() )
                break
            else:
                print ("\nthen check the path and input again!")
                path = input( 'input the path of the folder you\'d like to 

rename files in bulk:\n' )
if __name__ == '__main__':
    main()
