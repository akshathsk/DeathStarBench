import sys
sys.path.append('../gen-py')

import random
from media_service import PageService
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import unittest

# Docker should be fixed to run this test
class TestPageService(unittest.TestCase):
  def test_read_page(self):
    socket = TSocket.TSocket("localhost", 9090)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = PageService.Client(protocol)

    transport.open()
    for i in range(100):
      req_id = random.getrandbits(63)
      movie_id = "movie_id_" + str(i)
      print(client.ReadPage(req_id, movie_id, 0, 10, {}))
    transport.close()

if __name__ == '__main__':
  unittest.main()