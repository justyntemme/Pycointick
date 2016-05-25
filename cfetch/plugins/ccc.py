##
##  coinfetch-api-ccc - CryptoCoin Charts API plugin for coinfetch
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

class CccTicker(Ticker):
    def __init__(self, path, kind='price'):
        super().__init__(path, kind)

    def get_pair_data(self, response, pair=None):
        return response.json()

register_ticker('ccc', 'The CryptoCoin Charts ticker (built-in)',
                CccTicker('http://api.cryptocoincharts.info/tradingPair/'))
