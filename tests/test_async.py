from unittest import TestCase
import asyncio
apikey=''
apisecret=''


def async_get(task):
    loop = asyncio.get_event_loop()
    if not type(task) == list:
        tasks = [task]
    else:
        tasks = task
    return loop.run_until_complete(asyncio.gather(*tasks))[0]


class TestClient(TestCase):
    def test_ping(self):
        # during init of client, binance is pinged. Thus an errorless init of client means we pinged
        # succesfully
        from aiobinance.client import Client
        client = Client(apikey, apisecret)
        self.assertTrue(client)

    def test_get_exchange_info(self):
        from aiobinance.client import Client
        client = Client(apikey, apisecret)
        res = async_get(client.get_exchange_info())
        # we just quickly check if we got a response
        self.assertTrue(res['timezone'] == 'UTC')

    def test_get_orderbook_tickers(self):
        from aiobinance.client import Client
        client = Client(apikey, apisecret)
        res = async_get(client.get_orderbook_tickers())
        # we just quickly check if we got a response, binance returns an ordered response, so
        # ETHBTC is always at the top
        self.assertTrue(res[0]['symbol'] == 'ETHBTC')

    def test_get_order_book(self):
        from aiobinance.client import Client
        client = Client(apikey, apisecret)
        res = async_get(client.get_order_book(symbol='ETHBTC'))
        # check if we get a proper response
        self.assertTrue('lastUpdateId' in res)