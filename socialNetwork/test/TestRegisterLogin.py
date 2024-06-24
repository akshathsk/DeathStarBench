import uuid
import sys
sys.path.append('../gen-py')

import random
import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network import UserService

unittest.TestLoader.sortTestMethodsUsing = None

class TestUserService(unittest.TestCase):

    num = str(random.random())

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
        id = client.GetUserId(req_id, "username_" + self.num, {})
        print(id)
        self.assertIsNotNone(id)
        transport.close()    


if __name__ == '__main__':
    unittest.main()
