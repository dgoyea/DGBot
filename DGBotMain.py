import time
import sys, getopt
import datetime
import DGPoloniex

def main(argv):

    # Keys generated from poloniex for API connection
    APIKey1 = '7H4S92B3-ARCJIWL9-UWL47SQ9-4MEU37L1'
    Secret = '4d6fb56c5039a854f0db718a7b308b465347e67f93d56c2ac2c070313ca40a6ad103a8aafecf85e13a7b561cf41e4204902a08f3b0931e1498a87418128060d3'

    conn = DGPoloniex(APIKey1, Secret)

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

    try:
        opts, args = getopt.getopt(argv,"hp:",["period=",])
    except getopt.GetoptError:
        print 'DGBotMain.py -p <period>'
        sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
