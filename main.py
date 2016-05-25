from argparse import Action, ArgumentParser
from configparser import ConfigParser
from cfetch import __version__, get_ticker, get_registered_tickers
from cfetch import load_default_plugins
from os.path import expanduser, join, exists
from os import makedirs
import os
from time import sleep

__title__ = 'cointick'
__author__= 'Justyn Temme'


CONFIG_DIR = join(expanduser('~'), '.cointick')
CONFIG_PATH = join(CONFIG_DIR, 'config.ini')
config= ConfigParser()

if not exists(CONFIG_PATH):
	if not exists(CONFIG_DIR):
		makedirs(CONFIG_DIR)
	config['cointick'] = {}
	config['cointick']['api'] = 'ccc'
	with open(CONFIG_PATH, 'w') as f:
		config.write(f)
else:
	config.read(CONFIG_PATH)

default_api = config['cointick']['api']

load_default_plugins()
tickers = get_registered_tickers()
tickers.sort()

try:
	while (1==1):
		os.system('clear')
		print("BTC/USD \t",'%.8f' %get_ticker("ccc").get_rate('btc', 'usd', 1),"\n")
		print("LTC/USD \t",'%.8f' %get_ticker("ccc").get_rate('ltc', 'usd', 1),"\n")
		print("DOGE/USD \t",'%.8f' %get_ticker("ccc").get_rate('doge', 'usd', 1),"\n")
		sleep(10)
		
	
except KeyError:
	print('keyerror')
	print(tickers)
	exit(10)
except ValueError:
	print('valueerror')
