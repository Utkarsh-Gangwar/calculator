from tkinter import *


a = ""
sol = 0
num1 = 0
opr1 = '+'


def clr():
   global a, sol, num1, opr1
   a = ""
   sol = 0
   num1 = 0
   opr1 = '+'
   l['text']=a


def num(i):
   global a
   a=a+str(i)
   l['text']=a


def eq():
   global a, num1, opr1
   b=0
   c=0
   for i in range(len(a)):
      if a[i] != '+' and a[i] != '-' and a[i] != '/' and a[i] != '*':
         num1 = num1 * 10 + int(a[i])
      else:
         if opr1 == '+':
            sum()
         if opr1 == '-':
            sub1()
         if opr1 == '/':
            div1()
         if opr1 == '*':
            mul1()
         opr1=a[i]
   if num1 != 0:
      if opr1 == '+':
         sum()
      if opr1 == '-':
         sub1()
      if opr1 == '/':
         div1()
      if opr1 == '*':
         mul1()
   l['text'] = a + "=" + str(sol)


def sum():
   global sol, num1, opr1
   print(num1,'sum')
   sol=sol+num1
   num1=0


def sub1():
   global sol, num1, opr1
   print(num1,'sub')
   sol=sol-num1
   num1=0


def div1():
   global sol, num1, opr1
   print(num1,'div')
   sol=sol/num1
   num1=0


def mul1():
   global sol, num1, opr1
   print(num1,'mul')
   sol=sol*num1
   num1=0

root=Tk()

root.configure()

l = Label(root, text=a, height=2, width=10)
l.grid(row=1, columnspan=2)

b1=Button(root,text="1", command=lambda: num(1),height=2,width=10)
b1.grid(row=2,column=0)

b2=Button(root,text="2", command=lambda: num(2),height=2,width=10)
b2.grid(row=2,column=1)

b3=Button(root,text="3", command=lambda: num(3),height=2,width=10)
b3.grid(row=2,column=2)

b4=Button(root,text="4", command=lambda: num(4),height=2,width=10)
b4.grid(row=3,column=0)

b5=Button(root,text="5", command=lambda: num(5),height=2,width=10)
b5.grid(row=3,column=1)

b6=Button(root,text="6", command=lambda: num(6),height=2,width=10)
b6.grid(row=3,column=2)

b7=Button(root,text="7", command=lambda: num(7),height=2,width=10)
b7.grid(row=4,column=0)

b8=Button(root,text="8", command=lambda: num(8),height=2,width=10)
b8.grid(row=4,column=1)

b9=Button(root,text="9", command=lambda: num(9),height=2,width=10)
b9.grid(row=4,column=2)

b0=Button(root,text="0", command=lambda: num(0),height=2,width=10)
b0.grid(row=5,column=1)

add=Button(root,text="+", command=lambda: num('+'),height=2,width=10)
add.grid(row=2,column=3)

sub=Button(root,text="-", command=lambda: num('-'),height=2,width=10)
sub.grid(row=3,column=3)

mul=Button(root,text="*", command=lambda: num('*'),height=2,width=10)
mul.grid(row=4,column=3)

div=Button(root,text="/", command=lambda: num('/'),height=2,width=10)
div.grid(row=5,column=3)

cl=Button(root,text="Clear",command=clr,height=2,width=10)
cl.grid(row=5,column=0)

eql=Button(root,text="=", command=eq,height=2,width=10)
eql.grid(row=5,column=2)


root.mainloop()
