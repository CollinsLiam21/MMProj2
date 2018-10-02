import math


'''def cost(speed,size,maxLoad):

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

cost(1,10000000,10000000)'''

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
            f = '2.75*math.log10(x)-2.83'
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

maxLoad = 10000000
speed = 3

dailyRental = [520,780,1400]
dailyRental1 = dailyRental[(math.log10(maxLoad)//1)-5]

numOfDays = round((9600/speed)/24)
print(numOfDays)

if speed == 1:
    radius1 = 133.65046     #starting radius of spherical iceberg (found using volume of starting size)
    volume = maxLoad    #starting volume is the assumption that the starting size of the iceberg is the max load
    costOfFuel_Before4000 = 0
    for x2 in range(1,168):     #for loop that calculates volume at the end of 4000km and total cost of fuel up to 4000km
        r = '0.00144*x-0.0000014'   #linear regression of rate iceberg shrinks up to 4000km - found in desmos
        radius = eval(r.replace('x',str(x2)))   #plugs day into linear regression to find rate of decrease at that specific days
        radius1 -= radius   #updates radius value by subtracting radius on day x2 from previous day
        volume = (4/3)*3.1415*(radius1)**3      #calculates volume of iceberg at day x2
        f = '2.75*math.log10(x)-2.83'    #linear regression of fuel cost (made linear by taking log of size) - found in demos
        fuel = eval(f.replace('x',str(volume)))      #finds cost of fuel at day x2 based on the volume at that day
        costOfFuel_Before4000 += fuel*24    #updates total cost of fuel by adding the fuel for each day and..
                                                #multiplying by 24 because boat travels 24km/day at 1km/hr
    
    
    costOfFuel_After4000 = 0
    for i in range(168,numOfDays):
        radius = 0.24
        radius1 -= radius
        volume = (4/3)*3.1415*(radius1)**3
        f = '2.75*math.log10(x)-2.83'
        fuel = eval(f.replace('x',str(volume)))
        costOfFuel_After4000 += fuel*24
    
    
    totVolumeLoss = maxLoad - volume
    costOfFuel = costOfFuel_Before4000 + costOfFuel_After4000
    costOfTowing = costOfFuel + dailyRental1*numOfDays
    costOfDesalinating = (volume)*0.85*0.13
    
    print('Total volume loss:',totVolumeLoss,'m^3')
    print('Final volume:',volume,'m^3')
    print('Final fuel:',fuel,'$/km')
    print('Cost of fuel: $',costOfFuel)
    print('Cost of Towing = $',costOfTowing)
    print('Cost of desalinating: $',costOfDesalinating)
    print('Profit = $',costOfDesalinating - costOfTowing)

elif speed == 3:
    radius1 = 133.65046     #starting radius of spherical iceberg (found using volume of starting size)
    volume = maxLoad    #starting volume is the assumption that the starting size of the iceberg is the max load
    costOfFuel_Before4000 = 0   
    for x2 in range(1,56):      #for loop that calculates volume at the end of 4000km and total cost of fuel up to 4000km
        r = '0.00576*x+0.0000576'   #linear regression of rate iceberg shrinks up to 4000km - found in desmos
        radius = eval(r.replace('x',str(x2)))   #plugs day into linear regression to find rate of decrease at that specific days
        radius1 -= radius   #updates radius value by subtracting radius on day x2 from previous day
        volume = (4/3)*3.1415*(radius1)**3      #calculates volume of iceberg at day x2
        f = '3.5*math.log10(x)-3.467'   #linear regression of fuel cost (made linear by taking log of size) - found in demos
        fuel = eval(f.replace('x',str(volume)))     #finds cost of fuel at day x2 based on the volume at that day
        costOfFuel_Before4000 += fuel*72    #updates total cost of fuel by adding the fuel for each day and..
                                                #multiplying by 72 because boat travels 72km/day at 3km/hr
    
    
    costOfFuel_After4000 = 0
    for i in range(56,numOfDays):   #for loop that calculates final volume and total cost of fuel after 4000km
        radius = 0.32   #rate of change of radius stays constant after 4000
        radius1 -= radius   #updates radius value by subtracting radius on day x2 from previous day
        volume = (4/3)*3.1415*(radius1)**3      #calculates volume of iceberg at day x2
        f = '3.5*math.log10(x)-3.467'   #same regression for fuel cost b/c fuel cost continues to change
        fuel = eval(f.replace('x',str(volume)))     #finds cost of fuel at day x2 based on the volume at that day
        costOfFuel_After4000 += fuel*72     #updates total cost of fuel by adding the fuel for each day and..
                                                #multiplying by 72 because boat travels 72km/day at 3km/hr
    
    totVolumeLoss = maxLoad - volume
    costOfFuel = costOfFuel_Before4000 + costOfFuel_After4000
    costOfTowing = costOfFuel + dailyRental1*numOfDays      #daily rental found in list at the top of program based on max load
    costOfDesalinating = (volume)*0.85*0.13     #only %85 of ice turns to water
    
    print('Total volume loss:',totVolumeLoss,'m^3')
    print('Final volume:',volume,'m^3')
    print('Final fuel:',fuel,'$/km')
    print('Cost of fuel: $',costOfFuel)
    print('Cost of Towing = $',costOfTowing)
    print('Cost of desalinating: $',costOfDesalinating)
    print('Profit = $',costOfDesalinating - costOfTowing)
    
elif speed == 5:
    radius1 = 133.65046     #starting radius of spherical iceberg (found using volume of starting size)
    volume = maxLoad    #starting volume is the assumption that the starting size of the iceberg is the max load
    costOfFuel_Before4000 = 0   
    for x2 in range(1,34):      #for loop that calculates volume at the end of 4000km and total cost of fuel up to 4000km
        r = '0.0111*x+0.0000111'   #linear regression of rate iceberg shrinks up to 4000km - found in desmos
        radius = eval(r.replace('x',str(x2)))   #plugs day into linear regression to find rate of decrease at that specific days
        radius1 -= radius   #updates radius value by subtracting radius on day x2 from previous day
        volume = (4/3)*3.1415*(radius1)**3      #calculates volume of iceberg at day x2
        f = '4.25*math.log10(x)-4.033'   #linear regression of fuel cost (made linear by taking log of size) - found in demos
        fuel = eval(f.replace('x',str(volume)))     #finds cost of fuel at day x2 based on the volume at that day
        costOfFuel_Before4000 += fuel*120    #updates total cost of fuel by adding the fuel for each day and..
                                                #multiplying by 120 because boat travels 120km/day at 5km/hr
    
    
    costOfFuel_After4000 = 0
    for i in range(34,numOfDays):   #for loop that calculates final volume and total cost of fuel after 4000km
        radius = 0.40   #rate of change of radius stays constant after 4000
        radius1 -= radius   #updates radius value by subtracting radius on day x2 from previous day
        volume = (4/3)*3.1415*(radius1)**3      #calculates volume of iceberg at day x2
        f = '4.25*math.log10(x)-4.033'   #same regression for fuel cost b/c fuel cost continues to change
        fuel = eval(f.replace('x',str(volume)))     #finds cost of fuel at day x2 based on the volume at that day
        costOfFuel_After4000 += fuel*120    #updates total cost of fuel by adding the fuel for each day and..
                                                #multiplying by 120 because boat travels 120km/day at 5km/hr
    
    totVolumeLoss = maxLoad - volume
    costOfFuel = costOfFuel_Before4000 + costOfFuel_After4000
    costOfTowing = costOfFuel + dailyRental1*numOfDays      #daily rental found in list at the top of program based on max load
    costOfDesalinating = (volume)*0.85*0.13     #only %85 of ice turns to water
    
    print('Total volume loss:',totVolumeLoss,'m^3')
    print('Final volume:',volume,'m^3')
    print('Final fuel:',fuel,'$/km')
    print('Cost of fuel: $',costOfFuel)
    print('Cost of Towing = $',costOfTowing)
    print('Cost of desalinating: $',costOfDesalinating)
    print('Profit = $',costOfDesalinating - costOfTowing)

    
