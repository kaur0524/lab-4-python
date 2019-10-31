#distance between two points

def distance(x1,y1,x2,y2):
    import math
    
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist
x1=int(input('enter value of x1:')) 
y1=int(input('enter value of y1:'))  
x2=int(input('enter value of x2:'))  
y2=int(input('enter value of y2:'))   
print(f'The distance between {(x1,y1),(x2,y2)} is {distance(x1,y1,x2,y2)}.')


