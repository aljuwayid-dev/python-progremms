#name: Abdulkarim Aljuwayid
#id: 441102673
#Program 1:
print('============================')
pi = 3.14159265359
print('Enter the circle radius:')
r= input()
area1=pi*float(r)**2
print(f'The area of the circle with radius {r}',f'is:{area1}')
print('============================')
#Program 2:
number1 = 1234567.456
number2 = 1234567.456
print(format(number1, ',.3f'))
print(format(number2, ',.0f'))
print('============================')
#Program 3:
print('Enter the amount of purchase:')
p3 = input()
tax = float(p3)*0.05
total= tax + float(p3)
print(f'Total purchase = {p3} SR')
print(f'Sales tax = {tax} SR')
print(f'Total = {total} SR')
print('============================')
#Program 4:
def lbs_to_kgs(ibs):
    kgs = float(ibs)/2.205
    return kgs
print('Enter the weight in pounds:')
lbs= input()
kg = lbs_to_kgs(lbs)
ww=format(kg, ',.2f')
print(f'The weight in kilograms=  {ww} kgs')
print('============================')
#Program 5:
print('Enter the value of x:')
x=input()
print('Enter the value of y:')
(y)=input()
r1=float(y)*float(x)*float(y)+float(x)*float(y)+float(x)*float(y)*float(x)
print ('The computed value is:' , r1)
print('============================')