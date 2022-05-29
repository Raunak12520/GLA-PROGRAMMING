dict={}
n=int(input())
for i in range(n):
    k=int(input())
    v=int(input())
    dict.update({k:v})
    print(dict.values())
    print(sum(dict.values()))