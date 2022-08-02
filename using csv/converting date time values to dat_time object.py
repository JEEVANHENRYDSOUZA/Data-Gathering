pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()
#by default pandas will treat the datetime as a string hence in order to make it a datetime object we need to do this
