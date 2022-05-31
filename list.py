from xmlrpc.server import list_public_methods


list=[]
s=0
for num in list:
    num=int(num)
    if (num<0):
     s=s+num
     print(s)