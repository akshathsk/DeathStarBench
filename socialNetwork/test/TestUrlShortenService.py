import unittest
import uuid
import sys
sys.path.append('../gen-py')

from social_network import UrlShortenService
from social_network.ttypes import Url
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class TestUrlShortenService(unittest.TestCase):

    # Test URL Shorting Service
    def test1(self):
        socket = TSocket.TSocket("localhost", 10004)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UrlShortenService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)

        urls = ["https://url_0.com", "https://url_1.com", "https://url_2.com"]

        urlsGenerated = client.ComposeUrls(req_id, urls, {})

        print(urlsGenerated)

        self.assertTrue(len(urlsGenerated) == 3)
        self.assertTrue(
            urlsGenerated[0].shortened_url != urlsGenerated[0].expanded_url)
        self.assertTrue(
            urlsGenerated[1].shortened_url != urlsGenerated[1].expanded_url)
        self.assertTrue(
            urlsGenerated[2].shortened_url != urlsGenerated[2].expanded_url)
        self.assertTrue(urlsGenerated[0].expanded_url == "https://url_0.com")
        self.assertTrue(urlsGenerated[1].expanded_url == "https://url_1.com")
        self.assertTrue(urlsGenerated[2].expanded_url == "https://url_2.com")

        transport.close()


if __name__ == '__main__':
    unittest.main()
