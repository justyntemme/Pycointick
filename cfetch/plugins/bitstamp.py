##
##  coinfetch-api-bitstamp - Bitstamp API plugin for coinfetch
##  Copyright (C) 2015 Delwink, LLC
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Affero General Public License as published by
##  the Free Software Foundation, version 3 only.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Affero General Public License for more details.
##
##  You should have received a copy of the GNU Affero General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

from cfetch import register_ticker, Ticker
from requests import get

class BitstampTicker(Ticker):
    def __init__(self, path, kind='vwap'):
        super().__init__(path, kind)

    def get_pair_data(self, response):
        return response.json()

    def get_rate(self, a, b, amt=1):
        if a == 'btc' and b == 'usd':
            r = get(self.path)
            res = self.get_pair_data(r)
            return float(res[self.kind]) * amt
        elif a == 'usd' and b == 'btc':
            r = get(self.path)
            res = self.get_pair_data(r)
            return (float(res[self.kind]) ** -1) * amt
        else:
            raise ValueError('{}/{}'.format(a, b))

register_ticker('bs', 'The Bitstamp ticker (built-in)',
                BitstampTicker('https://www.bitstamp.net/api/ticker/'))
