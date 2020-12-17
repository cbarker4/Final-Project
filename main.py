import requests
import pandas as pd
import time
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import utility

its=[]
days = 50
moving_average =[]




transactions = pd.read_csv("2020transactions.csv")

tickers=[]
for symbol in transactions['SYMBOL'] :
    if  (symbol not in tickers): 
        symbol = str(symbol)
        if len(symbol)<5:
            if 0==(symbol == "nan"):

               
                tickers.append(str(symbol))
tickers.sort()
#print(tickers)

import utility
its=[]
days = 50
moving_average =[]

days = [50,100,200]
for day in days:
    hits =[]
   
    for sym in tickers:
        utility.standerd_moving_average(sym,day)
    plt.bar(tickers,hits)
    plt.xticks(tickers,rotation=90)
    plt.ylabel("Times Coliding with "+ str(day) +  " day moving average")
    plt.xlabel("Stock Ticker")
    plt.title("How Often Stock Hit Their "+ str(day) + " Day Moving Average")
    plt.show()
    plt.show()


# for ticker in tickers:

#     # key 1 7297G5GSN8QCRGZH
#     apkey = "7297G5GSN8QCRGZH"
#     period = "60min"
#     url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ticker&outputsize=full&apikey=apkey&datatype=csv"
#    # url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=AAPL&interval=1min&slice=year1month1&apikey=apkey"
#     url=url.replace("ticker",ticker)
#     url=url.replace("apkey",apkey)
#    # url=url.replace("period",period)
#     #print(url)
#     #url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo"
#     data = requests.request("GET", url)
#     outfile = open(r"Stocks/" +ticker+".csv", "w")
#     outfile.write(data.text)
#     outfile.close()
#     time.sleep(15)
    

transactions['DATE'] = pd.to_datetime(transactions['DATE'],infer_datetime_format = True,dayfirst = False,)
#print(transactions)
i=0
buys=[]
while i<len(transactions):
    if "Bought" in transactions.loc[i]["DESCRIPTION"]:
        if len(transactions.loc[i]["DESCRIPTION"])<38:
            buys.append(transactions.loc[i]["DESCRIPTION"] + " " + str(i))
    if "Sold" in transactions.loc[i]["DESCRIPTION"]:
        if len(transactions.loc[i]["DESCRIPTION"])<36:
            buys.append(transactions.loc[i]["DESCRIPTION"] + " " + str(i)) 
    i=i+1


i=0
while i<len(buys):
   # buys[i]=buys[i].replace("Bought ","")
    buys[i]=buys[i].replace("@ ","")
    buys[i]=buys[i].replace(" ",",")
    buys[i]=buys[i].replace("@","")
    
    i=i+1
#print (buys)
temp=[]
money =6000
Stock_buys = pd.DataFrame([sub.split(",")for sub in buys])
Stock_buys.columns = ['Buy/Sell','Shares','Ticker','Price','Date']

i=0
for days in Stock_buys['Date']:
    days=int(days)
    Stock_buys.loc[i]['Date']=(transactions["DATE"][days])
    i=i+1

i=0
k=0
price = []
shares = []
ticker = []
bought_Price = []
date = []
for buys in Stock_buys['Buy/Sell']:
    j=0
    first = 1
    while(j<len(ticker)):
        if ticker[j]==Stock_buys['Ticker'][i]:
            first = 0 
            #print(first)
        j=j+1

    if (buys=="Bought") & first :
        date.append(Stock_buys.loc[i]['Date'])
        price.append(float(Stock_buys.loc[i]['Price']))
        shares.append(int(Stock_buys.loc[i]['Shares']))
        ticker.append(Stock_buys.loc[i]['Ticker'])
        bought_Price.append((shares[k])*(price[k]))
        k=k+1
    i=i+1
    current_Price=[]

for sym in ticker:
    temp = pd.read_csv("Stocks/" + sym + ".csv")
    current_Price.append(temp['close'][0])


i=0
profit_loss = []
while(i<len(tickers)):
    
    if (ticker[i]=="TSLA"):
        profit_loss.append((current_Price[i]*shares[i]*5)-(bought_Price[i]))
    elif (ticker[i]=="AAPL"):
        profit_loss.append((current_Price[i]*shares[i]*4)-(bought_Price[i]))
    else:
        profit_loss.append((current_Price[i]*shares[i])-bought_Price[i])
    i=i+1

#print (len(profit_loss))
#print (len(ticker))
#print(profit_loss)
plt.bar(ticker,profit_loss)
plt.xticks(ticker,rotation=90)
plt.show()

hits=[]
days = 50
moving_average =[]
for sym in ticker:
    moving_average =[]
    temp = pd.read_csv("Stocks/" + sym + ".csv")
    i = -1
    last_days = []
    while (i<-50):
        last_days.append(temp['close'][i])
        i=i-1
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
        if (moving_average[i]<temp['open'][i])&(moving_average[i]>temp['close'][i]):
            counter=counter+1   
                
        i=i-1
    hits.append(counter)
print(hits)




plt.bar(ticker,hits)
plt.xticks(ticker,rotation=90)
plt.show()






#AAPL = pd.read_csv("Stocks/AAL.csv")

# i=0
# sells=[]
# while i<len(transactions):
#     if "Sold" in transactions.loc[i]["DESCRIPTION"]:
#         if len(transactions.loc[i]["DESCRIPTION"])<35:
#             sells.append(transactions.loc[i]["DESCRIPTION"] + " " + str(i))
#     i=i+1


# i=0
# while i<len(sells):
#     sells[i]=sells[i].replace("Sold ","")
#     sells[i]=sells[i].replace("@ ","")
#     sells[i]=sells[i].replace(" ",",")
#     sells[i]=sells[i].replace("@","")
    
#     i=i+1

# temp=[]
# money = 6000
# Stock_sold = pd.DataFrame([sub.split(",")for sub in sells])
# Stock_sold.columns = ['Shares','Ticker','Price','Date index']
# print (Stock_sold)





AAPL = pd.read_csv("Stocks/AAL.csv")
data=[go.Candlestick(x=AAPL['timestamp'],open=AAPL['open'],high=AAPL['high'],low=AAPL['low'],close=AAPL['close'])]
figSignal = go.Figure(data=data)
figSignal.show()

for tic in tickers:    
    temp = pd.read_csv("Stocks/" + tic + ".csv")
    open_ = temp["open"].tolist()
    close = temp["close"].tolist()

    alpha = 0.005

        # ttest_ind performs a two-tailed test
    t_computed, p_value = stats.ttest_rel(open_,close)
    print("t-computed:", t_computed, "p-value:", p_value)
    if p_value < alpha: 
        print("H0 is false, p-value:", p_value)
    else:
        print("H0 was not able to prove wrong, p-value:", p_value)