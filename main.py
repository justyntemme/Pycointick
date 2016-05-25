from argparse import Action, ArgumentParser
from configparser import ConfigParser
from cfetch import __version__, get_ticker, get_registered_tickers
from cfetch import load_default_plugins
from os.path import expanduser, join, exists
from os import makedirs

__title__ = 'cointick'
__author__= 'Justyn Temme'


CONFIG_DIR = join(expanduser('~'), '.coinfetch')
CONFIG_PATH = join(CONFIG_DIR, 'config.ini')
config= ConfigParser()

if not exists(CONFIG_PATH):
	if not exists(CONFIG_DIR):
		makedirs(CONFIG_DIR)
	config['coinfetch'] = {}
	config['coinfetch']['api'] = 'btce'
	with open(CONFIG_PATH, 'w') as f:
		config.write(f)
else:
	config.read(CONFIG_PATH)

default_api = config['coinfetch']['api']

load_default_plugins()
tickers = get_registered_tickers()
tickers.sort()

try:
	print('%.8f' %get_ticker(default_api).get_rate("btc", "usd", "1"))
except KeyError:
	print('keyerror')
	print(tickers)
	exit(10)
except ValueError:
	print('valueerror')
