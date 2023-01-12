import sys
sys.path.append('../gen-py')

from media_service import UniqueIdService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import random
import string

import unittest

class TestUniqueIdService(unittest.TestCase):
    def test_UniqueIdService():
        socket = TSocket.TSocket("localhost", 10001)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UniqueIdService.Client(protocol)

        transport.open()
        for i in range (1, 100) :
            req_id = random.getrandbits(64) - 2**63
            client.UploadUniqueId(req_id, {})

        transport.close()


if __name__ == '__main__':
    unittest.main()