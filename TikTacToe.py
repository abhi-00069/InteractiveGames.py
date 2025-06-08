#  Tic Tac Toe

import os
import random


def checkx(lstx) :
    for i in range(1,150):
        nlist=random.sample(lstx,3)
        mlst=[6,120,504,28,80,162,105,45]
        plst=[6,12,15,18,24]
        if nlist[0]*nlist[1]*nlist[2] in mlst :
            if nlist[0]+nlist[1]+nlist[2] in plst :
                print("X WON!!!")
                exit()

def checko(lsto) :
    for i in range(1,150):
        nlist=random.sample(lsto,3)
        mlst=[6,120,504,28,80,162,105,45]
        plst=[6,12,15,18,24]
        if nlist[0]*nlist[1]*nlist[2] in mlst :
            if nlist[0]+nlist[1]+nlist[2] in plst :
                print("O WON!!!")
                exit()

def prnt(lst):
    print("      |       |")
    print(" ",lst[0],"  |  ",lst[1],"  |  ",lst[2])
    print("      |       |")
    print("--------------------")
    print("      |       |")
    print(" ",lst[3],"  |  ",lst[4],"  |  ",lst[5])
    print("      |       |")
    print("--------------------")
    print("      |       |")
    print(" ",lst[6],"  |  ",lst[7],"  |  ",lst[8])
    print("      |       |")


lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
prnt(lst)

lstx=[]
lsto=[]

for j in range(1,6) :
    x=int(input("X's Turn : "))
    if x in lstx :
        print("INVALID MOVE!!")
        print("O WON!!!")
        exit()
    if x in lsto :
        print("INVALID MOVE!!")
        print("O WON!!!")
        exit()
    lstx.append(x)
    x-=1
    lst[x]="X"
    os.system('cls')
    prnt(lst)
    if len(lstx)>=3 :
        checkx(lstx)
        if j==5 :
            break
    o=int(input("O's Turn : "))
    if o in lstx :
        print("INVALID MOVE!!")
        print("X WON!!!")
        exit()
    if o in lsto :
        print("INVALID MOVE!!")
        print("X WON!!!")
        exit()
    lsto.append(o)
    o-=1
    
    lst[o]="O"
    os.system('cls')
    prnt(lst)
    if len(lsto)>=3 :
        checko(lsto)
print("Its a Draw")
