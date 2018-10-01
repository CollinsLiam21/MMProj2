
import math

def cost(speed,size,maxLoad):

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

cost(5,10000000,10000000)
    
        
    
