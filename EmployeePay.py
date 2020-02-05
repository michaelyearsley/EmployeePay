complete = []
while True:
    a = input('do you want to enter a employee (y or n):')
    if a == 'y' or a == 'Y' :
        complete.append(input("Enter Employees Name: "))
        x = input("Enter hours:" )
        while True:
            try:
                x = float(x)
                break
            except:
                x= input('Error, please enter numeric:')
        y = input("Enter rate:" )
        while True:
            try:
                y = float(y)
                break
            except:
                y= input('Error, please enter numeric:')
        complete.append(round((max(x-40,0)*(y*.5)+x*y),2))
        complete.append(round(((max(x-40,0)*(y*.5)+x*y) * 52.1428571),2))
        
    else:
        break
count = 0
for i in complete[::3]:
    count+= 1
    TXT = "Name: {0}, weekly pay is: {1} and yearly is: {2}."
    print(TXT.format(i , complete[count], complete[count+1]))
    count += 2
