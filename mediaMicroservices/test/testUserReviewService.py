import sys
sys.path.append('../gen-py')
import unittest
from time import time
import random
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import UserReviewService

class TestUserReviewService(unittest.TestCase):

    # Upload a user review
    def test1(self):
        socket = TSocket.TSocket("localhost", 10008)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserReviewService.Client(protocol)

        transport.open()
        for i in range(0, 100):
            req_id = random.getrandbits(63)
            timestamp = int(time() * 1000)
            user_id = random.randint(0, 5)
            client.UploadUserReview(req_id, user_id, i, timestamp, {})
        transport.close()

    # Read a user review
    def test2(self):
        socket = TSocket.TSocket("localhost", 10008)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserReviewService.Client(protocol)

        transport.open()
        reviews = []
        for i in range(100):
            req_id = random.getrandbits(63)
            user_id = random.randint(0, 5)
            start = random.randint(0, 10)
            stop = start + random.randint(1, 10)
            reviews.append(client.ReadUserReviews(req_id, user_id, start, stop, {}))
        transport.close()
        self.assertTrue(len(reviews) == 100)



if __name__ == '__main__':
    unittest.main()
