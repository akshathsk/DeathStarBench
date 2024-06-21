import random
import sys
sys.path.append('../gen-py')

import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service import MovieIdService
from media_service import MovieInfoService

movie_id = random.randint(1000, 100000) + random.randint(
                1, 100000) + random.randint(2000, 100000) + random.randint(2000, 100000)

class TestMovieIdService(unittest.TestCase):

    # Register a movieId - store to the db
    def test1(self):
        global movie_id
        socket = TSocket.TSocket("localhost", 10002)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieIdService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        title = "movie_" + str(movie_id)
        movie_id = "movie_id_" + str(movie_id)
        print(movie_id)
        client.RegisterMovieId(req_id, title, movie_id, {})
        transport.close()

    # Upload a movieId - store to the db
    def test2(self):
        global movie_id
        socket = TSocket.TSocket("localhost", 10002)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieIdService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        movie_index = random.randint(0, 4)
        title = "movie_" + str(movie_index)
        rating = random.randint(0, 10)
        client.UploadMovieId(req_id, title, rating, {})
        transport.close()

if __name__ == '__main__':
    unittest.main()
