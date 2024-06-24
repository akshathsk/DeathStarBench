import uuid
import sys
import random
sys.path.append('../gen-py')
import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network import HomeTimelineService
from social_network import UserService



class TestReadHomeTimelineService(unittest.TestCase):

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
        self.assertIsNotNone(id)
        transport.close()

    # Read the user's timeline
    def test3(self):
      socket = TSocket.TSocket("localhost", 10010)
      transport = TTransport.TFramedTransport(socket)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      client = HomeTimelineService.Client(protocol)

      transport.open()
      req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
      start = 0
      stop = 10
      print(client.ReadHomeTimeline(req_id, self.userId, start, stop, {}))
      transport.close()

if __name__ == '__main__':
  unittest.main()