moving_average = []
hits = []
import pandas as pd

def standerd_moving_average(sym,days):
    global moving_average
    if len(moving_average)>0:
        moving_average.clear()
    temp = pd.read_csv("Stocks/" + sym + ".csv")
    i = -1
    last_days = []
    while (i<-days):
        last_days.append(temp['close'][i])
        i=i-1
        print(len(last_days))
    i = len(temp)-days
    while (i>=0):
        last_days.append(temp['close'][i])
        if (len(last_days)==days):
            moving_average.append((sum(last_days))/days)
            last_days.pop(0)
    
        i=i-1
    i=len(moving_average)-1
     
    counter=0
    while i>=0:
        if (moving_average[-i]<temp['high'][i])&(moving_average[-i]>temp['low'][i]):
            counter=counter+1   
                
        i=i-1
    hits.append(counter)
