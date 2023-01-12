import sys
sys.path.append('../gen-py')

import uuid
from social_network import UniqueIdService
from social_network.ttypes import PostType

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import unittest

class TestUniqueIdService(unittest.TestCase):
  def test_UniqueIdService(self):
    socket = TSocket.TSocket("localhost", 10008)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = UniqueIdService.Client(protocol)

    transport.open()
    req_id = uuid.uuid4().int & (1<<32)
    print(client.ComposeUniqueId(req_id, PostType.POST, {}))
    transport.close()

if __name__ == '__main__':
  unittest.main()