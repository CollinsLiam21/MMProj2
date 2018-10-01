
import math

'''def cost(speed,size,maxLoad):

    radius1 = 76
    radius3 = 60
    radius5 = 25.58
        
    x2 = 0
    f = '0.00144*x-0.0000014'
    eval(f.replace('x',str(x2)))
    #prints function and interval
    print('Interval = [',0,',',x2,']')
    
    #Finding derivative
    print("f'(x) = ",a*b,'x^',b-1,' + ',c*d,'x^',d-1)
    
    #number of boxes, after 1000 boxes the program runs very slowly
    n = 100
    
    #a loop multiplying every other y value by 4 and the other y values by 2 (Simpson's Rule)
    num = 1
    total = 0
    for i in range(1,n):
        if num%2 == 0:
            total += 4*eval(f.replace('x',str(((x2-0)/n)*i)))
            num += 1
        else:
            total += 2*eval(f.replace('x',str(((x2-0)/n)*i)))
            num += 1
    
    #first value yo and last value yn
    firstYValue = sqrt(1+(a*b*(x1)**(b-1)+c*d*(x1)**(d-1))**2)
    lastYValue = sqrt(1+(a*b*(x2)**(b-1)+c*d*(x2)**(d-1))**2)
    
    #prints arc length
    print('Arc Length:',(total+firstYValue+lastYValue)*(x2-x1)/n*(1/3))

#user input values for the function
#function(a,b,c,d,e,x1,x2)


    if speed == 1:
        totalVolumeLoss = (4/3)*3.14*76**3
        print('rate (volume/day) =',totalVolumeLoss)
    
    elif speed == 3:
        totalVolumeLoss = (4/3)*3.14*60**3
        print('rate (volume/day) =',totalVolumeLoss)
        
    elif speed == 5:
        totalVolumeLoss = (4/3)*3.14*25.28**3
        print('rate (volume/day) =',totalVolumeLoss)
    
    print('Original Volume =',size)
    print('Final Volume =',size-totalVolumeLoss)
    print('Cost of desalinating: $',(size-totalVolumeLoss)*0.85*0.13)
    
    OneFuel = [10.9,13.7,16.4]
    ThreeFuel = [14,17.6,21]
    FiveFuel = [17.2,21.5,25.7]
    
    dailyRental = [520,780,1400]
    dailyRental1 = dailyRental[(math.log10(maxLoad)//1)-5]
    
    if maxLoad/size >= 1:
        numOfLoads = maxLoad/size
    else:
        print('Not feasible')
    
    numOfDays = (9600/speed)/24
    
    from math import sqrt

    #defined function
    def arcLength(x1,x2):
        
        f = 2.75*math.log10(totalVolume)
        #prints function and interval
        print('Interval = [',x1,',',x2,']')
        
        #Finding derivative
        print("f'(x) = ",a*b,'x^',b-1,' + ',c*d,'x^',d-1)
        
        #number of boxes, after 1000 boxes the program runs very slowly
        n = 100
        
        #a loop multiplying every other y value by 4 and the other y values by 2 (Simpson's Rule)
        num = 1
        total = 0
        for i in range(1,n):
            if num%2 == 0:
                total += 4*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
                num += 1
            else:
                total += 2*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
                num += 1
        
        #first value yo and last value yn
        firstYValue = sqrt(1+(a*b*(x1)**(b-1)+c*d*(x1)**(d-1))**2)
        lastYValue = sqrt(1+(a*b*(x2)**(b-1)+c*d*(x2)**(d-1))**2)
        
        #prints arc length
        print('Arc Length:',(total+firstYValue+lastYValue)*(x2-x1)/n*(1/3))
    
    #user input values for the function
    #function(a,b,c,d,e,x1,x2)
    arcLength(1/3,3,1/4,-1,0,1,3)
    
    if speed == 1:
        costOfTowing = OneFuel[math.log10(size)-5]*numOfLoads*9600+dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',(size-totalVolumeLoss)*0.85*0.13 - costOfTowing)
    
    elif speed == 3:
        costOfTowing = ThreeFuel[math.log10(size)-5]*numOfLoads*9600+dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',(size-totalVolumeLoss)*0.85*0.13 - costOfTowing)
    
    elif speed == 5:
        costOfTowing = FiveFuel[math.log10(size)-5]*numOfLoads*9600+dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',(size-totalVolumeLoss)*0.85*0.13 - costOfTowing)

cost(5,10000000,10000000)'''

a = 0
for x2 in range(0,167):
    f = '0.00144*x-0.0000014'
    #prints function and interval
    a += eval(f.replace('x',str(x2)))
    
print(a)



'''#number of boxes, after 1000 boxes the program runs very slowly
n = 100

#a loop multiplying every other y value by 4 and the other y values by 2 (Simpson's Rule)
num = 1
total = 0
for i in range(1,n):
    if num%2 == 0:
        total += 4*eval(f.replace('x',str(((x2)/n)*i)))
        num += 1
    else:
        total += 2*eval(f.replace('x',str(((x2)/n)*i)))
        num += 1

#first value yo and last value yn
firstYValue = eval(f.replace('x',str(0)))
lastYValue = eval(f.replace('x',str(x2)))
integral = (total+firstYValue+lastYValue)*(x2)/n*(1/3)
box = (400-x2)*eval(f.replace('x',str(x2)))

#prints arc length
print('Interval = [',0,',',x2,']')
print('Integral:',integral)'''

    
        
    
