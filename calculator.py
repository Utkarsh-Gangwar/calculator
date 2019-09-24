from tkinter import *
a=" "
b=0
c=0
d=0
i=0
def clr():
   global a,b,c,d,i
   a=" "
   b=0
   c=0
   d=0
   i=0
   l['text']=a
def text_update():
   if i==0:
      a=str(b)
   if i==1:
      a=str(b)+'+'+str(c)
   if i==2:
      a=str(b)+'-'+str(c)
   if i==3:
      a=str(b)+'*'+str(c)
   if i==4:
      a=str(b)+'/'+str(c)
   l['text']=a
def i_up(n):
   global i,b
   i=n
   if c==0:
      if i==1:
         a=str(b)+'+'
      if i==2:
         a=str(b)+'-'
      if i==3:
         a=str(b)+'*'
      if i==4:
         a=str(b)+'/'
   else :
      if i==0:
         a=str(b)
      if i==1:
         a=str(b)+'+'+str(c)
      if i==2:
         a=str(b)+'-'+str(c)
      if i==3:
         a=str(b)+'*'+str(c)
      if i==4:
         a=str(b)+'/'+str(c)
   l['text']=a
def num(n):
   global a,b,c,i
   if i==0:
      b=b*10+n
   else :
      c=c*10+n
   text_update()
def eq():
   global i,a,b,c,d
   if i==1:
      d=b+c
      a=str(b)+'+'+str(c)+'='+str(d)
      l['text']=a
   if i==2:
      d=b-c
      a=str(b)+'-'+str(c)+'='+str(d)
      l['text']=a
   if i==3:
      d=b*c
      a=str(b)+'*'+str(c)+'='+str(d)
      l['text']=a
   if i==4:
      d=b/c
      a=str(b)+'/'+str(c)+'='+str(d)
      l['text']=a
root=Tk()
root.configure()
l = Label(root,text=a,height=2,width=10)
l.grid(row=1,column=1)
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
eql=Button(root,text="=", command=eq,height=2,width=10)
eql.grid(row=5,column=2)
add=Button(root,text="+", command=lambda: i_up(1),height=2,width=10)
add.grid(row=2,column=3)
sub=Button(root,text="-", command=lambda: i_up(2),height=2,width=10)
sub.grid(row=3,column=3)
mul=Button(root,text="*", command=lambda: i_up(3),height=2,width=10)
mul.grid(row=4,column=3)
div=Button(root,text="/", command=lambda: i_up(4),height=2,width=10)
div.grid(row=5,column=3)
cl=Button(root,text="Clear",command=clr,height=2,width=10)
cl.grid(row=5,column=0)
root.mainloop()
