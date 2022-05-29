''' when ever a exception occur the progarm stops the execution and thus tha further code not 
going to execute therefore an excetion is a run time error that are anable to handle by the python
the common exception are 
1- ZeroDivisionEreror- occus when a num. is divided by zero
2- NameError- occurs when the name is not defined
3- IoError - when input and output not defined 
4- EOFError- Eccors when the end of file is reached and still operation is preform'''
'''1 - the try and except - the try block is use to throw exception and expect block catches that 
    exception in another word we must place the whole whick make throw exception in try block 
    if exception occus it is to be catch by except block'''




try:
    a = int(input())
    if (a<0):
        raise ValueError
    else:
        print(a)    
    except ValueError:
        print("X")    