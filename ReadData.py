import pandas as pd

top3 = pd.read_csv("TOP3.csv")
top3 = top3.set_index("date")


def read_hist_values(data):
    '''Accepts pandas DataFrame of top pickes for eachday and returns DataFrame with trading values'''
    df = data

    trading_days = df.index.tolist()

    my_trading_list =[]

    for day in trading_days[1:483]: #[1:] ... first (0 element) is NaN, last element is also not used
        for col1 in range(0,len(df.columns)): #warning ... based on number of columns len(df.columns)
            tick = df[df.columns[col1]].loc[day]
            #Open file with data
            hisdf = pd.read_csv("CSV-DATA/{}.csv".format(tick), "r", delimiter=',' ) # load data from file
            hisdf = hisdf.set_index('date') # ste index to date to make it searchable
            aclose = hisdf['adj_close'].loc[day] #adjusted close value from day of evaluation
            open = hisdf['open'].iloc[hisdf.index.get_loc(day) + 1] # one trading day later
            close =hisdf['close'].iloc[hisdf.index.get_loc(day) + 1] #again one trading day later
            wlist =[day, tick, aclose, open, close] # create small with Ticker and data
            my_trading_list.append(wlist) #add list to the list of lists


    trading_df = pd.DataFrame(columns=['date', 'Ticker','aclose','Nopen','Nclose'], data=my_trading_list)
    trading_df = trading_df.set_index('date')
    print(trading_df)






if __name__ == '__main__':
    read_hist_values(top3)
