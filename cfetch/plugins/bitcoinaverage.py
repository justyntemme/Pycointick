##
##  coinfetch-api-bitcoinaverage - BitcoinAverage API plugin for coinfetch
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

class BitcoinAverageTicker(Ticker):
    def __init__(self, path, kind='24h_avg'):
        super().__init__(path, kind)

    def get_pair_data(self, response):
        return response.json()

    def get_rate(self, a, b, amt=1):
        a = a.upper()
        b = b.upper()
        if 'BTC' not in (a, b):
            self._fail(a, b)

        r = get(self.path)
        res = self.get_pair_data(r)

        try:
            if a == 'BTC':
                if b not in res:
                    self._fail(a, b)

                res = res[b]
                return float(res[self.kind]) * amt

            if a not in res:
                self._fail(a, b)

            res = res[a]
            return (float(res[self.kind]) ** -1) * amt
        except (KeyError, TypeError) as e:
            raise ValueError(str(e))

    def _fail(self, a, b):
        raise ValueError('{}/{}'.format(a, b))

register_ticker('ba', 'The BitcoinAverage ticker (built-in)',
                BitcoinAverageTicker('https://api.bitcoinaverage.com/ticker/all'))
