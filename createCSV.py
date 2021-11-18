import yahoo_fin.stock_info as si
import pandas as pd

with open("companies.txt") as file:
    lines = file.readlines()
    companyList = [line.rstrip() for line in lines]

stockData = {}

sum_df=pd.DataFrame()

for ticker in companyList:
    try:
        print(si.get_data(ticker, start_date="01/01/2010", end_date="01/03/2020", interval="1mo"))
        stockData[ticker] = si.get_data(ticker, start_date="01/01/2010", end_date="01/03/2020", interval="1mo")
        
        sum_df = sum_df.append(stockData[ticker])
    except:
        continue

sum_df.index=sum_df.index.rename("data")
sum_df.to_excel("output.xlsx") 