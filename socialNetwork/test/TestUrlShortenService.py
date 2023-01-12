import sys
sys.path.append('../gen-py')

import uuid
from social_network import UrlShortenService
from social_network.ttypes import Url

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import unittest

class TestUrlShortenService(unittest.TestCase):
  def test_UrlShortenService(self):
    socket = TSocket.TSocket("localhost", 10004)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = UrlShortenService.Client(protocol)

    transport.open()
    req_id = uuid.uuid4().int & ( 1 << 32 )

    urls = ["https://url_0.com", "https://url_1.com", "https://url_2.com"]

    print(client.ComposeUrls(req_id, urls, {}))
    transport.close()

if __name__ == '__main__':
  unittest.main()