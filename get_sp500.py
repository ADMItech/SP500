import bs4 as bs
import pickle
import requests
import pandas as pd
import os


def save_sp500_tickers():
    if not os.path.exists("SP500Data"):
        os.makedirs("SP500Data")
    if not os.path.exists("SP500Data/SP500.csv"):
        resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
        soup = bs.BeautifulSoup(resp.text, "lxml")
        table = soup.find('table',{'class':'wikitable sortable'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            indu = row.findAll('td')[3].text
            tickers.append((ticker,indu))
        #df = pd.DataFrame.from_records(tickers,columns=['Ticker','Industry'])
        df = pd.DataFrame(tickers)
        df.columns = ['Ticker', 'Industry']
        df.set_index(df.columns[0])
        #df.drop(df.columns[0])
        df.to_csv("SP500Data/SP500.csv", index_label=0, index=0 )
    else:
        print("*** I already have SP500.csv ***")
        df = pd.read_csv("SP500Data/SP500.csv", "r", delimiter=',')
        #df.drop(df.columns[0])

    list_of_Industries = df.Industry.unique().tolist()
    file = open('SP500Data/Industries.txt','w')
    for item in list_of_Industries:
        file.write("%s\n" % item)

    for indu in list_of_Industries:
        if not os.path.exists("SP500Data/{}.csv".format(indu)):
            newdf = df
            newdf = newdf.loc[newdf['Industry'] == indu]
            newdf.to_csv("SP500Data/{}.csv".format(indu), index_label=0, index=0)

def list_SP500():
    df = pd.read_csv("SP500Data/SP500.csv", "r", delimiter=',')
    lsp500= df['Ticker'].tolist()
    return lsp500


if __name__ == "__main__":
    #save_sp500_tickers()
    print(list_SP500())
