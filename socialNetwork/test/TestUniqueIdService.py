import uuid
import sys
sys.path.append('../gen-py')

import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network.ttypes import PostType
from social_network import UniqueIdService

class TestUniqueIdService(unittest.TestCase):

    # Test Unique Id generation service
    def test1(self):
        socket = TSocket.TSocket("localhost", 10008)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UniqueIdService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)
        uniqueId = client.ComposeUniqueId(req_id, PostType.POST, {})
        self.assertIsNotNone(uniqueId)
        transport.close()


if __name__ == '__main__':
    unittest.main()
