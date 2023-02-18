import uuid
import sys
sys.path.append('../gen-py')

import uuid
import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from social_network import UserService
from social_network.ttypes import ServiceException

class TestUserService(unittest.TestCase):

    # Invalid login credentials
    def test1(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        try:
          client.Login(
              req_id, "username_007", "password_0", {})
        except ServiceException:
          self.assertTrue
        transport.close()


if __name__ == '__main__':
    unittest.main()
