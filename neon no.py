a=int(input("enter no "))
rem=s1=s2=0
while(a>0):
        rem=a%10
        if(rem%2==0):s1+=rem
        else:s2+=rem
          
          a=a//10

if(s1==s2):print("a")
else: print("b")    
