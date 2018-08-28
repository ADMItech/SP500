Project Description

Goal of the project is to create small trading strategy similar to Dogs of Dow.

Tasks:
1) Identify and download data (tickers) of actual SP 500 companies
    1.1) Identify SP 500 companies
    1.2) Read data from reputable website
    1.3) Save Ticker and Industry of each company
    1.4) Save the list locally ... if function is called more than once a day ... parse
        data from web only once a day.

2) Connect to reputable source of trading data and download daily data
    2.1) Quandl.com was selected as source of data.
    2.2) Read API and create pull request for all SP500 companies (10 years of history)
    2.3) Save data to local folder and csv (more than 500 companies and 10 years history)
    2.4) Check Quandl for Data limits ... may need sleep function....

3) Rescale the data to monthly data.

4) Find the TOP 3 GROWTH industries
    4.1) Divide tickers to groups by Industry
    4.2) Save industries to local folder as csv
    4.3) Calculate average growth of the industry ... (simple average of the growth of all companies within industry)
    4.4) Find 3 industries with the highest growth

5) Find the TOP 3 growth tickers within TOP 3 industries
    5.1) Find Top 3 companies within each of the Top 3 industries

6) Create Report
    6.1) Calculate whole algorithm once a month
    6.2) Create report in MS Excel
    6.3) Connect to google account and send the report to Given list of subscribers
