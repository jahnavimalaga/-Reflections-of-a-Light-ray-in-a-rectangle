# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:14:31 2016

@author: Jahnavi Malagavalli
"""
#Programme: Time taken by the incident ray to come out of the rectangle 
#Hole is located on the line x=a
import pylab as p
a=20 #a : length of the rectangle
b=10 #b : breadth of the rectangle
w=5
d=input('coordinate of the midpoint with commas on x=a:')
m=1
h=float(d[0])
k=float(d[1])
 #h : x_coordinate of the midpoint
#m =float(input('enter the slope :'))#m : slope of the incident ray with x-axis
x=0
y=0
x1=h #x1 : x-coordinate of the point where the light ray touches the rectangle
y1=k #y1 : y-coordinate of the point where the light ray touches the rectangle
l1=[h] #l1 : list of all x1's
l2=[k] #l2 : list of all y1's
def fun(x,y):
       l1.append(x) 
       l2.append(y)
       x1=x
       y1=y
       global x1 
       global y1 
       print x1,y1  
    
    
while x!=a or (y>(w/2.0)+k or y<k-(w/2.0)):       
   if x1==a:
      if m>y1/x1:
        y=0
        x=((y-y1)/m)+x1
        if x>0 and x<a:
           fun(x,y)
           m=-m
           continue
      if m<y1/x1 or m>(y1-b)/x1: 
        x=0
        y=m*(x-x1)+y1
        if y>0 and y<b:
           fun(x,y)
           m=-m
           continue
      if m<(y1-b)/x1:   
        y=b
        x=((y-y1)/m)+x1
        if x>0 and x<a:
           fun(x,y)
           m=-m
           continue
   if y1==0:
      if (m)>(y1-b)/x1:
        x=0
        y=m*(x-x1)+y1
        if y>0 and y<b:
           fun(x,y)
           m=-m
           continue
      if m>(y1-b)/(x1-a) or m<(y1-b)/x1 :
        y=b
        x=((y-y1)/m)+x1
        if x>0 and x<a:
            fun(x,y)
            m=-m
            continue 
      if m<(y1-b)/(x1-a):
        x=a
        y=m*(x-x1)+y1
        if y>0 and y<b:
            fun(x,y)
            m=-m
            continue     
   if x1==0:
      if m>(y1-b)/(x1-a):
        y=b
        x=((y-y1)/m)+x1
        if x>0 and x<b:
            fun(x,y)
            m=-m
            continue
      if m<(y1-b)/(x1-a) or m>y1/(x1-a):
        x=a
        y=m*(x-x1)+y1
        if y>0 and y<b:
            fun(x,y)
            m=-1*m
            continue  
      if m<y1/(x1-a):
        y=0
        x=((y-y1)/m)+x1
        if x>0 and x<a:
            fun(x,y)
            m=-1*m
            continue
   if y1==b:
      if m>y1/(x1-a):
        x=a
        y=m*(x-x1)+y1
        if y>0 and y<b:
           fun(x,y)
           m=-1*m
           continue
      if m<y1/(x1-a) or m>y1/x1 :
         y=0
         x=((y-y1)/m)+x1
         if x>0 and x<a:
           fun(x,y)
           m=-1*m
           continue 
      if m<y1/x1 :
         x=0
         y=m*(x-x1)+y1
         if y>0 and y<b:
           fun(x,y)
           m=-1*m
           continue
             
else:
    print 'no of reflections:',(len(l1)-2)
    d=0
    for i in range(len(l1)-1):
        d=d+p.sqrt(((l1[i]-l1[i+1])**2)+((l2[i]-l2[i+1])**2) )
        print d
    print 'the distance traveled by the light ray is : ',d
    time=d/(3.0*(10**8))
    print 'The time taken for the light ray to come out is : ',time
    



a
