#impot the important packaging module
import pandas_datareader.data as pdr
import fix_yahoo_finance
import pandas as pd
import matplotlib.pyplot as plt



#define each and everything to perform the operation
def PPSR(data):  
    PP = pd.Series((data['High'] + data['Low'] + data['Close']) / 3)  
    R1 = pd.Series(2 * PP - data['Low'])  
    S1 = pd.Series(2 * PP - data['High'])  
    R2 = pd.Series(PP + data['High'] - data['Low'])  
    S2 = pd.Series(PP - data['High'] + data['Low'])  
    R3 = pd.Series(data['High'] + 2 * (PP - data['Low']))  
    S3 = pd.Series(data['Low'] - 2 * (data['High'] - PP))  
    psr = {'PP':PP, 'R1':R1, 'S1':S1, 'R2':R2, 'S2':S2, 'R3':R3, 'S3':S3}  
    PSR = pd.DataFrame(psr)  
    data= data.join(PSR)  
    return data
#extract the stock data
data = pdr.get_data_yahoo("^NSEI", start="2017-01-01", end="2017-07-31")
#compute and print the data
PD=PPSR(data)
print(PD)
# plot the data
pd.concat([data['Close'],PD.PP,PD.R1,PD.S1,PD.R2,PD.S2,PD.R3,PD.S3],axis=1).plot(figsize=(12,9),grid=True)
plt.show()
