
import math

def costDesalinating(speed,size,dailyRental,numOfDays,disday1,disday2,disday3,disday4,disday5,disday6,disday7,disday8,disday9):

    OneRate = [0.06,0.12,0.18,0.24]
    ThreeRate = [0.08,0.16,0.24,0.32]
    FiveRate = [0.1,0.2,0.3,0.4]
    
    if speed == 1:
        rate = 0
        if disday1 > 0:
            rate += OneRate[(disday1/1000)-1]
        if disday2 > 0:
            rate += OneRate[(disday2/1000)-1]
        if disday3 > 0:
            rate += OneRate[(disday3/1000)-1]
        if disday4 > 0:
            rate += OneRate[(disday4/1000)-1]
        if disday5 > 0:
            rate += OneRate[(disday5/1000)-1]
        if disday6 > 0:
            rate += OneRate[(disday6/1000)-1]
        if disday7 > 0:
            rate += OneRate[(disday7/1000)-1]
        if disday8 > 0:
            rate += OneRate[(disday8/1000)-1]
        if disday9 > 0:
            rate += OneRate[(disday9/1000)-1]
        print('rate =',rate)
    
    if speed == 3:
        rate = 0
        if disday1 > 0:
            rate += ThreeRate[(disday1/1000)-1]
        if disday2 > 0:
            rate += ThreeRate[(disday2/1000)-1]
        if disday3 > 0:
            rate += ThreeRate[(disday3/1000)-1]
        if disday4 > 0:
            rate += ThreeRate[(disday4/1000)-1]
        if disday5 > 0:
            rate += ThreeRate[(disday5/1000)-1]
        if disday6 > 0:
            rate += ThreeRate[(disday6/1000)-1]
        if disday7 > 0:
            rate += ThreeRate[(disday7/1000)-1]
        if disday8 > 0:
            rate += ThreeRate[(disday8/1000)-1]
        if disday9 > 0:
            rate += ThreeRate[(disday9/1000)-1]
        print('rate =',rate)
        
    if speed == 5:
        rate = 0
        if disday1 > 0:
            rate += FiveRate[(disday1/1000)-1]
        if disday2 > 0:
            rate += FiveRate[(disday2/1000)-1]
        if disday3 > 0:
            rate += FiveRate[(disday3/1000)-1]
        if disday4 > 0:
            rate += FiveRate[(disday4/1000)-1]
        if disday5 > 0:
            rate += FiveRate[(disday5/1000)-1]
        if disday6 > 0:
            rate += FiveRate[(disday6/1000)-1]
        if disday7 > 0:
            rate += FiveRate[(disday7/1000)-1]
        if disday8 > 0:
            rate += FiveRate[(disday8/1000)-1]
        if disday9 > 0:
            rate += FiveRate[(disday9/1000)-1]
        print('rate =',rate)
    
    print('Cost of desalinating: $',(size-rate)*0.85*0.13)
    
    OneFuel = [10.9,13.7,16.4]
    ThreeFuel = [14,17.6,21]
    FiveFuel = [17.2,21.5,25.7]
    
    if speed == 1:
        if dailyRental == 520:
            print('Cost of Towing = $',OneFuel[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',OneFuel[math.log10(size)-5]*9600+dailyRental*numOfDays)
    
    if speed == 3:
        if dailyRental == 520:
            print('Cost of Towing = $',ThreeFuel[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',ThreeFuel[math.log10(size)-5]*9600+dailyRental*numOfDays)
    
    if speed == 5:
        if dailyRental == 520:
            print('Cost of Towing = $',FiveFuel[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',FiveFuel[math.log10(size)-5]*9600+dailyRental*numOfDays)
        
costDesalinating(1,100000,520,2,3000,3000,2000,2000,0,0,0,0,0)

'''def costTowing(speed,size,dailyRental,numOfDays):

    One = [10.9,13.7,16.4]
    Three = [14,17.6,21]
    Five = [17.2,21.5,25.7]
    
    if speed == 1:
        if dailyRental == 520:
            print('Cost of Towing = $',One[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',One[math.log10(size)-5]*9600+dailyRental*numOfDays)
    
    if speed == 3:
        if dailyRental == 520:
            print('Cost of Towing = $',Three[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',Three[math.log10(size)-5]*9600+dailyRental*numOfDays)
    
    if speed == 5:
        if dailyRental == 520:
            print('Cost of Towing = $',Five[math.log10(size)-5]*5*9600+dailyRental*numOfDays)
        else:
            print('Cost of Towing = $',Five[math.log10(size)-5]*9600+dailyRental*numOfDays)

costTowing(1,10000000,1400,2)'''
    
        
    
