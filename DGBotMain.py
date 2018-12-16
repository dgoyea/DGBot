import os
import sys, getopt
import time
import datetime
import configparser
import DGDBWriter
from DGPoloniexWrapper import dgpoloniex

def ts():
    return str(datetime.datetime.now())

def main(argv):

    # If command line arguments are given use this section.
    try:
        opts, args = getopt.getopt(argv,"hp:",["period=",])
    except getopt.GetoptError:
        print (ts() + ': DGBotMain.py -p <period>')
        sys.exit(2)
    
    # Get configuration from ini file.
    
    cfgfile = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\DGBotConfig\DGBotConfig.ini')
    config = configparser.ConfigParser()
    
    if os.path.isfile(cfgfile):
        print(ts() + ': Using ini file: ' + cfgfile)
    else:
        print(ts() + ': No ini file found.')
        quit()
                
    try:
        print(ts() + ': Reading config file.')
        config.read(cfgfile)
        
    except:
        print(ts() + ': Could not read config file.')
    
    period = 5

    # Get keys from config file. Keys are generated from poloniex for API connection.
    pair = config['Poloniex']['Pair']
    APIKey1 = config['Poloniex']['APIKey']
    Secret = config['Poloniex']['Secret']
       
    # Create instance of dgpoloniex.
    conn = dgpoloniex(APIKey1, Secret);

    while True:
        currentValues = conn.api_query("returnTicker", pair)

        lastPairPrice = float(currentValues[pair]["last"])

        print ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ' Period: %ss %s: %.12f' % (period,pair,lastPairPrice))
        time.sleep(int(period))


if __name__ == "__main__":
	main(sys.argv[1:])
