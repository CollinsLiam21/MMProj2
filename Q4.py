
import math

def cost(speed,size,maxLoad):

    radius1 = 76
    radius3 = 60
    radius5 = 25.58

    if speed == 1:
        totalVolumeLoss = (4/3)*3.14*76**3
        print('volume loss =',totalVolumeLoss)
    
    elif speed == 3:
        totalVolumeLoss = (4/3)*3.14*60**3
        print('volume loss =',totalVolumeLoss)
        
    elif speed == 5:
        totalVolumeLoss = (4/3)*3.14*25.28**3
        print('volume loss =',totalVolumeLoss)
    
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

cost(1,10000000,10000000)

'''def cost(speed,size,maxLoad): 
    
    dailyRental = [520,780,1400]
    dailyRental1 = dailyRental[(math.log10(maxLoad)//1)-5]
    
    if maxLoad/size >= 1:
        numOfLoads = maxLoad/size
    else:
        print('Not feasible')
    
    numOfDays = (9600/speed)/24
    
    if speed == 1:
        radius = 0
        volume = maxLoad
        costOfFuel_Before4000 = 0
        for x2 in range(0,168):
            r = '0.00144*x-0.0000014'
            #prints function and interval
            radius += eval(r.replace('x',str(x2)))
            volume -= (4/3)*3.1415*(radius)**3
            f = '2.75*math.log10(volume)-2.83'
            fuel = eval(f.replace('x',str(volume)))
            costOfFuel_Before4000 += fuel*24

        costOfFuel_After4000 = fuel*(numOfDays-x2)
        costOfFuel = costOfFuel_Before4000 + costOfFuel_After4000
        totVolumeLoss = maxLoad - volume
        print('total volume loss:',totVolumeLoss)
        print('final volume:',volume)
        print('cost of desalinating:',volume*0.85*0.13)
        print('final fuel:',fuel)
        print('cost of fuel: ',costOfFuel)
        
        costOfTowing = costOfFuel + dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',volume*0.85*0.13 - costOfTowing)
    
    elif speed == 3:
        costOfTowing = ThreeFuel[math.log10(size)-5]*numOfLoads*9600+dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',(size-totalVolumeLoss)*0.85*0.13 - costOfTowing)
    
    elif speed == 5:
        costOfTowing = FiveFuel[math.log10(size)-5]*numOfLoads*9600+dailyRental1*numOfDays
        print('Cost of Towing = $',costOfTowing)
        print('Profit =',(size-totalVolumeLoss)*0.85*0.13 - costOfTowing)

cost(1,10000000,10000000)'''
print('')
speed = 1

dailyRental = [520,780,1400]
dailyRental1 = dailyRental[(math.log10(10000000)//1)-5]

numOfDays = (9600/speed)/24


radius1 = 133.65046
volume = 10000000
#costOfFuel_Before4000 = 0
fuel = 0
for x2 in range(1,168):
    r = '0.00144*x-0.0000014'
    #prints function and interval
    radius = eval(r.replace('x',str(x2)))
    radius1 -= radius
    volume = (4/3)*3.1415*(radius1)**3
    f = '2.75*math.log10(x)-2.83'
    fuel += 24*eval(f.replace('x',str(volume)))
    #costOfFuel_Before4000 += fuel*24


#costOfFuel_After4000 = 0
for i in range(168,400):
    r = '0.00144*x-0.0000014'
    #prints function and interval
    radius = 0.24
    radius1 -= radius
    volume = (4/3)*3.1415*(radius1)**3
    f = '2.75*math.log10(x)-2.83'
    fuel += 24*eval(f.replace('x',str(volume)))
    #costOfFuel_After4000 += fuel*24

#volumeLoss_After4000 = (4/3)*3.1415*(eval(r.replace('x',str(x2)))*(400-x2))**3
#costOfFuel = costOfFuel_Before4000 + costOfFuel_After4000
totVolumeLoss = 10000000 - volume

print(eval(r.replace('x',str(x2)))*(400-x2))
print('total volume loss:',totVolumeLoss)
print('final volume:',volume)
print('cost of desalinating:',(volume)*0.85*0.13)
print('final fuel:',fuel)
print('cost of fuel: ',fuel)

costOfTowing = fuel + dailyRental1*400
print('Cost of Towing = $',costOfTowing)
print('Profit =',(volume)*0.85*0.13 - costOfTowing)

'''volume = 1000
for i in range(0,2):
    f = 'math.log10(x)'
    print(eval(f.replace('x',str(volume))))'''




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

    
        
    
