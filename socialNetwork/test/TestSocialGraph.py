import uuid
import sys
import random
sys.path.append('../gen-py')

import unittest
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from social_network import SocialGraphService
from social_network import UserService



class TestSocialGraph(unittest.TestCase):

    numPost = random.randint(1, 100000)
    user1 = str(random.randint(1, 100000))
    user2 = str(random.randint(1, 100000))
    user3 = str(random.randint(1, 100000))
    userId1 = 0
    userId2 = 0
    userId3 = 0

    # Register new users
    def test1(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        client.RegisterUser(req_id, "first_name_" + self.user1, "last_name_" + self.user1,
                            "username_" + self.user1, "password_0", {})
        client.RegisterUser(req_id, "first_name_" + self.user2, "last_name_" + self.user2,
                            "username_" + self.user2, "password_0", {})
        client.RegisterUser(req_id, "first_name_" + self.user3, "last_name_" + self.user3,
                            "username_" + self.user3, "password_0", {})
        self.assertTrue
        transport.close()

    # Check if id is auto generated for the new user
    def test2(self):
        global userId1
        global userId2
        global userId3
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        userId1 = client.GetUserId(req_id, "username_" + self.user1, {})
        userId2 = client.GetUserId(
            req_id, "username_" + self.user2, {})
        userId3 = client.GetUserId(
            req_id, "username_" + self.user3, {})
        self.assertIsNotNone(id)
        transport.close()

    # Creating the social graph
    def test3(self):
        global userId1
        global userId2
        global userId3

        socket = TSocket.TSocket("localhost", 10000)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = SocialGraphService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)
        client.Follow(req_id, userId1, userId2, {})
        client.Follow(req_id, userId1, userId3, {})
        client.Follow(req_id, userId2, userId1, {})
        client.Follow(req_id, userId3, userId1, {})

        user1Followers = client.GetFollowers(req_id, userId1, {})
        user2Followers = client.GetFollowers(req_id, userId2, {})
        user3Followers = client.GetFollowers(req_id, userId3, {})

        user1Followees = client.GetFollowees(req_id, userId1, {})
        user2Followees = client.GetFollowees(req_id, userId2, {})
        user3Followees = client.GetFollowees(req_id, userId3, {})

        self.assertTrue(userId2 in user1Followers)
        self.assertTrue(userId3 in user1Followers)
        self.assertTrue(userId1 in user2Followers)
        self.assertTrue(userId1 in user3Followers)

        self.assertTrue(userId2 in user1Followees)
        self.assertTrue(userId3 in user1Followees)
        self.assertTrue(userId1 in user2Followees)
        self.assertTrue(userId1 in user3Followees)

        transport.close()


if __name__ == '__main__':
    unittest.main()
