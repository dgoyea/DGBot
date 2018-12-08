import time
import sys, getopt
import datetime
import configparser
import DGDBWriter
from DGPoloniexWrapper import dgpoloniex

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

def main(argv):

    # Get configuration from ini file
    config = configparser.ConfigParser()
    config.sections()
    
    config.read('../DGBotConfig.ini')
    
    pair = 'BTC_EOS'
    period = 5

    # Keys generated from poloniex for API connection
    APIKey1 = ''
    Secret = ''

    print('Creating dgpoloniex object')
    conn = dgpoloniex(APIKey1, Secret)

    try:
        opts, args = getopt.getopt(argv,"hp:",["period=",])
    except getopt.GetoptError:
        print ('DGBotMain.py -p <period>')
        sys.exit(2)

    while True:
        currentValues = conn.api_query("returnTicker")

        lastPairPrice = float(currentValues[pair]["last"])

        print ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Period: %ss %s: %.12f' % (period,pair,lastPairPrice))
        time.sleep(int(period))


if __name__ == "__main__":
	main(sys.argv[1:])
