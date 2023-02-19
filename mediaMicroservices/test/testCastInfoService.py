import random
import sys
sys.path.append('../gen-py')

from media_service import CastInfoService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import unittest

cast_ids = set()

class TestCastInfoService(unittest.TestCase):

    # Create a new cast info
    def test1(self):
        global cast_ids
        socket = TSocket.TSocket("localhost", 10010)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = CastInfoService.Client(protocol)
        transport.open()
        for i in range(100):
            req_id = random.getrandbits(63)
            cast_id = random.randint(1000, 100000) + random.randint(
                1, 100000) + random.randint(2000, 100000) + random.randint(2000, 100000) + random.randint(2000, 100000)
            name = "name_" + str(i)
            gender = random.randint(0, 1)
            intro = "intro_" + str(i)
            cast_ids.add(cast_id)
            client.WriteCastInfo(req_id, cast_id, name, gender, intro, {})
        transport.close()

    # Read the cast info
    def test2(self):
        global cast_ids
        socket = TSocket.TSocket("localhost", 10010)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = CastInfoService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        caseArr = client.ReadCastInfo(req_id, cast_ids, {})
        print(caseArr)
        print(len(caseArr))
        self.assertTrue(len(caseArr) > 0)
        transport.close()


if __name__ == '__main__':
    unittest.main()
