import time
import sys, getopt
import datetime
from DGPoloniexWrapper import dgpoloniex

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

def main(argv):

    pair = 'BTC_EOS'
    period = 5

    # Keys generated from poloniex for API connection
    APIKey1 = '7H4S92B3-ARCJIWL9-UWL47SQ9-4MEU37L1'
    Secret = '4d6fb56c5039a854f0db718a7b308b465347e67f93d56c2ac2c070313ca40a6ad103a8aafecf85e13a7b561cf41e4204902a08f3b0931e1498a87418128060d3'

    print('Connecting to Poloniex')
    conn = dgpoloniex(APIKey1, Secret)

    try:
        opts, args = getopt.getopt(argv,"hp:",["period=",])
    except getopt.GetoptError:
        print ('DGBotMain.py -p <period>')
        sys.exit(2)

    while True:
        print('Its True')
        currentValues = conn.api_query("returnTicker")

        lastPairPrice = float(currentValues[pair]["last"])

        print ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Period: %ss %s: %.12f' % (period,pair,lastPairPrice))
        time.sleep(int(period))


if __name__ == "__main__":
	main(sys.argv[1:])
