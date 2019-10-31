#convert Fahrenheit To Celsius
# conversion formula: (F − 32) × 5/9 

def fTemp(f):
    cTemp=(f-32) * (5/9)
    return cTemp
f=float(input('Enter Fharenheit value: '))

print(f'You entered {f}F and in celsius it is:{fTemp(f)}')


