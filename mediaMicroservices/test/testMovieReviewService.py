import sys
sys.path.append('../gen-py')
import unittest
from time import time
import string
import random
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import MovieReviewService

class TestMovieReviewService(unittest.TestCase):

    # Write a movie review
    def test1(self):
        socket = TSocket.TSocket("localhost", 10009)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieReviewService.Client(protocol)
        transport.open()
        for i in range(101, 200):
            req_id = random.getrandbits(63)
            timestamp = int(time() * 1000)
            movie_num = random.randint(0, 5)
            movie_id = "movie_id_" + str(movie_num)
            client.UploadMovieReview(req_id, movie_id, i, timestamp, {})
        transport.close()

    # Read the movie review
    def test2(self):
        socket = TSocket.TSocket("localhost", 10009)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieReviewService.Client(protocol)
        transport.open()
        reviews = []
        for i in range(100):
            req_id = random.getrandbits(63)
            movie_num = random.randint(0, 5)
            movie_id = "movie_id_" + str(movie_num)
            start = random.randint(0, 10)
            stop = start + random.randint(1, 10)
            try:
              reviews.append(client.ReadMovieReviews(req_id, movie_id, start, stop, {}))
            except:
              print()
        self.assertTrue(len(reviews) > 0)
        transport.close()


if __name__ == '__main__':
    unittest.main()
