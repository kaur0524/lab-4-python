#calculating area of circle

def area(r):
    import math
    a=r**2 * math.pi
    return a
r=float(input('Enter radius of circle:'))
print(f'Area of circle is:{area(r)}')
