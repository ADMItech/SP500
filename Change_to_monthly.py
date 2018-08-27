import pandas as pd
import os



def conversion_to_1m(filename):
    '''
    Small script that will accept my csv files with given format and change them to mothly csv ....
    '''
    if not os.path.exists("CSV-DATA"):
        print('Data are not in default directory ....!!!')
    else:
        df = pd.read_csv("CSV-DATA/{}.csv".format(filename))
        df = df.set_index('date')
        df.index = pd.to_datetime(df.index)
        df = df.resample('1M').ohlc()
        df = df.drop(('adj_close', 'open'),1)
        df = df.drop(('adj_close', 'high'),1)
        df = df.drop(('adj_close', 'low'),1)
        df = df.drop(('open', 'close'),1)
        df = df.drop(('open', 'high'),1)
        df = df.drop(('open', 'low'),1)
        df = df.drop(('close', 'open'),1)
        df = df.drop(('close', 'high'),1)
        df = df.drop(('close', 'low'),1)
        df.columns=['adj_close','open','close']

        if not os.path.exists("CSV-DATA-1M"):
            os.makedirs("CSV-DATA-1M")

        df.to_csv("CSV-DATA-1M/{}-M.csv".format(filename))

conversion_to_1m('MMM')
