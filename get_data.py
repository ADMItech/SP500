# Pokus o nejaky maly program


import quandl
import os
import pandas as pd


quandl.ApiConfig.api_key = "GFC7TB6QRmcKByPXsN9y"  # private key of each owner


def download_data(shares):
    if not os.path.exists("CSV-DATA"):
        os.makedirs("CSV-DATA")

    for ticker in shares:
        if not os.path.exists("CSV-DATA/{}.csv".format(ticker)):
            df = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'adj_close', 'open', 'close'] }, ticker = ticker, date = { 'gte': '2016-01-01', 'lte': '2017-12-31' })
            newdf = df[df.columns[1:]].set_index(['date'])
            newdf.to_csv("CSV-DATA/{}.csv".format(ticker))
        else:
            print("*** I already have {} ***".format(ticker))


def compile_data():

    main_df = pd.DataFrame()

    for count,ticker in enumerate(shares):

        df = pd.read_csv("CSV-DATA/{}.csv".format(ticker), "r", delimiter=',' )
        df.set_index('date', inplace=True)

        df.rename(columns = {"adj_close":ticker}, inplace=True)
        df.drop(["open","close"], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how="outer")

    #print(main_df.head())
    main_df.to_csv('Joined_closes.csv')

def df_pct_change():
    df = pd.read_csv("Joined_closes.csv", "r", delimiter=',' )
    df.set_index('date', inplace=True)
    dfpct = df.pct_change()
    return dfpct

def top_3_each_day():
    df = df_pct_change()
    topdf = df.apply(lambda x: pd.Series(x.sort_values(ascending=False).iloc[:3].index,index=['top1','top2','top3']), axis=1).reset_index()
    topdf.set_index('date', inplace=True)
    return topdf

def list_SP500():
    df = pd.read_csv("SP500Data/SP500.csv", "r", delimiter=',')
    lsp500= df['Ticker'].tolist()
    return lsp500



if __name__ == "__main__":
    #shares = ['MSFT','AAPL']
    #shares = ['MSFT','AAPL','V', 'AMZN', 'NFLX', 'GOOGL', 'FB', 'TSLA']
    shares = list_SP500()[:10]
    download_data(shares)
    compile_data()
    #print(df_pct_change())
    top_3_each_day().to_csv('TOP3.csv')
