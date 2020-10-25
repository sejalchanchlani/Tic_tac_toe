from tkinter import *
from itertools import permutations
from tkinter.messagebox import *
root=Tk()
root.geometry('600x600')
y='x'
x=2
play_1=[]
play_2=[]
def fun(number):
    global x,y
    global play_1,play_2
    if number==1:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b1.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b1.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b1.config(text=y)
    if number==2:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b2.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b2.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b2.config(text=y)
    if number==3:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b3.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b3.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b3.config(text=y)
    if number==4:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b4.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b4.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b4.config(text=y)
    if number==5:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b5.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b5.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b5.config(text=y)
    if number==6:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b6.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b6.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b6.config(text=y)
    if number==7:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b7.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b7.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b7.config(text=y)
    if number==8:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b8.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b8.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b8.config(text=y)
    if number==9:#if user clicks button 1
        if x%2==0:#if is player 1
            y='X'
            print("player 1")
            b3.config(bg='lightgreen')
            play_1.append(number)
        else:
            y='0'
            print("player 2")
            b9.config(bg='cyan')
            play_2.append(number)
        x=x+1
        b9.config(text=y)
    set1 = permutations([1,2,3])
    set2 = permutations([4,5,6])
    set3 = permutations([7,8,9])
    set4 = permutations([1,4,7])
    set5 = permutations([2,5,8])
    set6 = permutations([3,6,9])
    set7 = permutations([1,5,9])
    set8 = permutations([3,5,7])
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            player_1=all(elem in play_1 for elem in j)
            player_2 =all(elem in play_2 for elem in j)
            if player_1:
                showinfo("Results", "HURRAY, Player 1 won")
                break
            elif player_2:
                showinfo("Results", "HURRAY, Player 2 won")
                break
            else:
                pass
l=Label(root,bg='peachpuff',fg='green',text='TIC TAC TOE',font=('calibri',36,'bold'),width=20,height=1)
l.place(x=50,y=10)
l1=Label(root,text="Player 1- 'X'",font=(('italic'),20,'bold'),width=20,height=1)
l1.place(x=3,y=100)
l2=Label(root,text="Player 2- '0'",font=(('italic'),20,'bold'),width=15,height=1)
l2.place(x=250,y=100)
b1=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(1))
b1.place(x=50,y=150)
b2=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(2))
b2.place(x=200,y=150)
b3=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(3))
b3.place(x=351,y=150)
b4=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(4))
b4.place(x=50,y=266)
b5=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(5))
b5.place(x=200,y=266)
b6=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(6))
b6.place(x=351,y=266)
b7=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(7))
b7.place(x=50,y=382)
b8=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(8))
b8.place(x=200,y=382)
b9=Button(root,bg='lightgray',font=(('calibri'),10,'bold'),width=20,height=7,command=lambda :fun(9))
b9.place(x=351,y=382)
root.mainloop()
