import random
import string
import unittest
import sys
sys.path.append('../gen-py')

from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import ComposeReviewService
from media_service import MovieReviewService

movie_ids = set()

class TestComposeReviewService(unittest.TestCase):

    # Compose a movie review
    def test1(self):
        global movie_ids
        socket = TSocket.TSocket("localhost", 10006)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = ComposeReviewService.Client(protocol)
        transport.open()
        for i in range(100):
            req_id = random.getrandbits(63)
            unique_id = random.getrandbits(63)
            text = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=128))
            user_id = random.randint(0, 5)
            movie_id = "movie_id_" + str(random.randint(0, 5))
            movie_ids.add(movie_id)
            rating = random.randint(0, 10)
            client.UploadUniqueId(req_id, unique_id, {})
            client.UploadUserId(req_id, user_id, {})
            client.UploadRating(req_id, rating, {})
            client.UploadText(req_id, text, {})
            client.UploadMovieId(req_id, movie_id, {})
        transport.close()

    # Read the composed movie
    def test2(self):
        global movie_ids
        socket = TSocket.TSocket("localhost", 10009)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieReviewService.Client(protocol)
        transport.open()
        reviews = list()
        for i in movie_ids:
            req_id = random.getrandbits(63)
            start = random.randint(0, 10)
            stop = start + random.randint(1, 10)
            reviews.append(client.ReadMovieReviews(req_id, i, start, stop, {}))
        self.assertTrue(len(reviews) > 0)
        self.assertIsNotNone(reviews)
        transport.close()


if __name__ == '__main__':
    unittest.main()
