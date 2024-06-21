import unittest
import string
import random
import sys
sys.path.append('../gen-py')

from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import TextService

class TestTextService(unittest.TestCase):

    # Store Text
    def test_TextService(self):
        socket = TSocket.TSocket("localhost", 10003)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = TextService.Client(protocol)
        transport.open()
        for i in range(1, 2):
            req_id = random.getrandbits(64) - 2**63
            text = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=128))
            client.UploadText(req_id, text, {})
        self.assertTrue
        transport.close()


if __name__ == '__main__':
    unittest.main()
