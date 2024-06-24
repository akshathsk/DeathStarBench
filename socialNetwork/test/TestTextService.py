import uuid
import sys
sys.path.append('../gen-py')

import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network import TextService

class TestSocialGraph(unittest.TestCase):

    # Extract information from user's post
    def test1(self):
        socket = TSocket.TSocket("localhost", 10007)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = TextService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        text = "text hello world https://url_0 https://url_1 @username_2 https://url_2"
        ret = client.ComposeText(req_id, text, {})

        print(ret)

        self.assertTrue(ret.user_mentions[0].user_id, 2)
        self.assertTrue(ret.user_mentions[0].username, "username_2")
        self.assertTrue(len(ret.urls) == 3)
        self.assertIsNotNone(ret.urls[0].shortened_url)
        self.assertIsNotNone(ret.urls[1].shortened_url)

        transport.close()


if __name__ == '__main__':
    unittest.main()
