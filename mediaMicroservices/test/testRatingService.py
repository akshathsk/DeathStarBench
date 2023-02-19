import sys
sys.path.append('../gen-py')
import unittest
import random
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import RatingService

class TestRatingService(unittest.TestCase):

    # Store a new rating
    def test(self):
        socket = TSocket.TSocket("localhost", 10004)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = RatingService.Client(protocol)
        transport.open()
        for i in range(1, 100):
            req_id = random.getrandbits(63)
            movie_id = "movie_id_" + str(random.randint(0, 4))
            rating = random.randint(0, 10)
            client.UploadRating(req_id, movie_id, rating, {})
        transport.close()


if __name__ == '__main__':
    unittest.main()
