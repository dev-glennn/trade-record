import json
import requests
import time
import datetime, dateutil.parser
from datetime import datetime

# COMPANY
# upbit 1 | bithumb 2 | bittrex 3

# upbit
def upbit(coin):

    url = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-'+coin)
    url_result=url.json()
    url_result=url_result[0]

    result=[]
    result.append(1) #company
    result.append(coin) #type
    result.append(url_result.get("trade_timestamp"))
    result.append(url_result.get("opening_price"))
    result.append(url_result.get("high_price"))
    result.append(url_result.get("low_price"))
    result.append(url_result.get("trade_price"))
    result.append(url_result.get("prev_closing_price"))

    return result

# bithumb
def bithumb(coin):

    url = requests.get('https://api.bithumb.com/public/ticker/'+coin)
    url_result = url.json()
    url_result=url_result['data']

    result=[]
    result.append(2) #company
    result.append(coin) #type
    result.append(url_result.get("date"))
    result.append(url_result.get("opening_price"))
    result.append(url_result.get("max_price"))
    result.append(url_result.get("min_price"))
    result.append(url_result.get("average_price"))
    result.append(url_result.get("closing_price"))

    return result

#bittrex
def bittrex(coin):

    url = requests.get('https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=usd-'+coin)
    dict_url=url.json()
    url_result=dict_url['result'][0]

    #datetime to timestamp
    datetime = dateutil.parser.parse(url_result.get("TimeStamp"))
    timestamp=time.mktime(datetime.timetuple())

    candle_url=requests.get('https://api.bittrex.com/v3/markets/'+coin+'-USD/candles?candleInterval=DAY_1')
    candle_url=candle_url.json()

    today=datetime.today().strftime("%Y-%m-%d")+"T00:00:00Z"
    find_today_url=(item for item in candle_url if item['startsAt']==today)
    dict_candle_url=next(find_today_url,False)

    result=[]
    result.append(3) #company
    result.append(coin) #type
    result.append(timestamp)
    result.append(exchange_KRWUSD("USD",float(dict_candle_url['open'])))
    result.append(exchange_KRWUSD("USD",url_result.get("High")))
    result.append(exchange_KRWUSD("USD",url_result.get("Low")))
    result.append(exchange_KRWUSD("USD",url_result.get("Last")))
    result.append(exchange_KRWUSD("USD",float(dict_candle_url['open'])))

    return result

#exchange
def exchange_KRWUSD(currency,value):

    url=requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW'+currency)

    exchange=url.json()
    exchange=exchange[0]['basePrice']
    result=value*exchange

    return result
