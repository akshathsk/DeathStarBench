import uuid
import sys
sys.path.append('../gen-py')

import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network import UserMentionService

class TestUserMentionService(unittest.TestCase):

    # Composing User Mentions
    def test1(self):
        socket = TSocket.TSocket("localhost", 10009)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserMentionService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0X7FFFFFFFFFFFFFFF

        user_mentions = ["username_0", "username_1", "username_2"]

        userMentions = client.ComposeUserMentions(req_id, user_mentions, {})

        self.assertTrue(len(userMentions) == 3)
        self.assertTrue(userMentions[0].user_id == 0)
        self.assertTrue(userMentions[0].username == "username_0")
        self.assertTrue(userMentions[1].user_id == 1)
        self.assertTrue(userMentions[1].username == "username_1")
        self.assertTrue(userMentions[2].user_id == 2)
        self.assertTrue(userMentions[2].username == "username_2")

        transport.close()


if __name__ == '__main__':
    unittest.main()
