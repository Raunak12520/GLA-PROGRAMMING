from hashlib import shake_128


a=int(input("enter no "))
rem=s=q=0
i=10
while(a>0 and i>=1)
 rem=a%10
 if(i%2==0):
      s+=rem
 else:
     q+=rem
if(s==q):
    print("a")
else:
    print("b")    
           