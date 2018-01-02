import get_yahoo_quotes
from datetime import datetime
import time
from pprint import pprint

symbol = 'PRIC-B.ST'
start_date = datetime.strptime('2017-02-03', '%Y-%m-%d')
end_date = datetime.now()

start_date = int(time.mktime(start_date.timetuple()))
end_date = int(time.mktime(end_date.timetuple()))
cookie, crumb = get_yahoo_quotes.get_cookie_crumb(symbol)
data_list = get_yahoo_quotes.get_data_list(symbol, start_date, end_date, cookie, crumb)
pprint(data_list)
