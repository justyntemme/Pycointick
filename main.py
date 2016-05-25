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
	config['cointick']['curr'] = 'usd'
	config['cointick']['coins'] = 'btc ltc doge'
	config['cointick']['refresh'] = '10'
	with open(CONFIG_PATH, 'w') as f:
		config.write(f)
else:
	config.read(CONFIG_PATH)

default_api = config['cointick']['api']
default_currency = config['cointick']['curr']
coins = str.split(config['cointick']['coins'],' ')
refresh = int(config['cointick']['refresh'])

load_default_plugins()
tickers = get_registered_tickers()
tickers.sort()
while (1):
	os.system("clear")
	for String in coins:
		print(String,"/",default_currency, "\t",'%.8f' %get_ticker(default_api).get_rate(String,default_currency, 1),"\n")
	sleep(int(refresh))
