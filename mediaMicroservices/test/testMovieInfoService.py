import random
import sys
sys.path.append('../gen-py')

import unittest
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift import Thrift
from media_service.ttypes import Cast
from media_service import MovieInfoService
import string

# Error in this test case - struct.error: required argument is not a float
class TestMovieInfoService(unittest.TestCase):

    def test1(self):
        socket = TSocket.TSocket("localhost", 10012)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieInfoService.Client(protocol)

        transport.open()
        for i in range(100):
            req_id = random.randint(0, 10)
            movie_id = "movie_id_" + str(i)
            title = "movie_" + str(i)
            cast_id = random.randint(0, 96)
            casts = []
            for j in range(3):
                cast = Cast(cast_id=j, character="character_" +
                            str(j), cast_info_id=cast_id+j)
                casts.append(cast)
            plot_id = i
            thumbnail_ids = []
            photo_ids = []
            video_ids = []
            for j in range(3):
                thumbnail_ids.append(str(random.randint(1, 100)))
                photo_ids.append(str(random.randint(1, 100)))
                video_ids.append(str(random.randint(1, 100)))
            avg_rating = str(round(random.uniform(33.33, 66.66), 2))
            print(avg_rating)
            num_rating = random.randint(1, 100)
            client.WriteMovieInfo(req_id, movie_id, title, casts, plot_id, thumbnail_ids,
                                  photo_ids, video_ids, avg_rating, num_rating, {})

        transport.close()

    def test2(self):
        socket = TSocket.TSocket("localhost", 10012)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MovieInfoService.Client(protocol)

        transport.open()
        for i in range(100):
            req_id = random.getrandbits(63)
            movie_id = "movie_id_" + str(random.randint(0, 99))
            print(client.ReadMovieInfo(req_id, movie_id, {}))
        transport.close()


if __name__ == '__main__':
    unittest.main()
