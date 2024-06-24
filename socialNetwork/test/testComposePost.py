import random
import uuid
import sys
sys.path.append('../gen-py')

import unittest
from social_network import HomeTimelineService
from social_network import UserService
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network.ttypes import PostType
from social_network import ComposePostService

class TestComposePost(unittest.TestCase):

    num = str(random.random())
    numOther = str(random.random())
    userId = 0
    otherUserId = 0

    # Register a new user
    def test1(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        client.RegisterUser(req_id, "first_name_" + self.num, "last_name_" + self.num,
                            "username_" + self.num, "password_0", {})
        client.RegisterUser(req_id, "first_name_" + self.numOther, "last_name_" + self.numOther,
                            "username_" + self.numOther, "password_0", {})
        self.assertTrue
        transport.close()

    # Login with the same registered user
    def test2(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        self.assertIsNotNone(client.Login(
            req_id, "username_" + self.num, "password_0", {}))
        transport.close()

    # Check if id is auto generated for the new user
    def test3(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        self.userId = client.GetUserId(req_id, "username_" + self.num, {})
        self.otherUserId = client.GetUserId(req_id, "username_" + self.numOther, {})
        self.assertIsNotNone(id)
        transport.close()

    # Compose post
    def test4(self):
        socket = TSocket.TSocket("localhost", 10001)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = ComposePostService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        client.ComposePost(req_id, "username_" + self.num, self.userId,
                           "HelloWorld", [0, 1], ["png", "png"], PostType.POST, {})
        transport.close()

    # Read Home's timeline to check for the post
    def test5(self):
        socket = TSocket.TSocket("localhost", 10010)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = HomeTimelineService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        start = 0
        stop = 10
        list = client.ReadHomeTimeline(req_id, self.otherUserId, start, stop, {})
        self.assertTrue(len(list) > 0)
        transport.close()


if __name__ == '__main__':
    unittest.main()
