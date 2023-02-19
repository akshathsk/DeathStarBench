import uuid
import unittest
import sys
sys.path.append('../gen-py')

from media_service import UserService
from media_service import ttypes
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import random

class TestUserService(unittest.TestCase):

    num = random.randint(1000, 100000) + random.randint(1, 100000)

    # Register a new user
    def test1(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)
        firstName = "FirstName" + str(self.num)
        lastName = "LastName" + str(self.num)
        username = "username" + str(self.num)
        password = "password" + str(self.num)
        userId = self.num
        try:
            client.RegisterUserWithId(
                req_id, firstName, lastName, username, password, userId, {"": ""})
            self.assertTrue
        except ttypes.ServiceException as se:
            print('%s' % se.message)
        transport.close()

    # Login with the registered user
    def test2(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)
        username = "username" + str(self.num)
        password = "password" + str(self.num)
        try:
            client.Login(
                req_id, username, password, {"": ""})
            self.assertTrue
        except ttypes.ServiceException as se:
            print('%s' % se.message)
        transport.close()

    # Invalid credentials
    def test3(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & (1 << 32)
        username = "usernameNew" + str(self.num)
        password = "passwordNew" + str(self.num)
        try:
            client.Login(
                req_id, username, password, {"": ""})
            self.assertTrue
        except ttypes.ServiceException as se:
            print('%s' % se.message)
            self.assertTrue
        transport.close()


if __name__ == '__main__':
    unittest.main()
