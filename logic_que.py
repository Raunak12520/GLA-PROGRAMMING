from wsgiref import headers


head=(int(input('enter the no: of head: ')))
leg=(int(input('enter the no: of leg: ')))
x=(leg/2)-head
y=head-x
print(f'the no of rabbit is {x} and the no: of hens is : {y}')
