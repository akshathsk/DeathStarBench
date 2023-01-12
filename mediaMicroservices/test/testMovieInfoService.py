import sys
sys.path.append('../gen-py')

import random
import string
from media_service import MovieInfoService
from media_service.ttypes import Cast
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import unittest

class TestMovieInfoService(unittest.TestCase):
  def test_wrtie_movie_info(self):
    socket = TSocket.TSocket("localhost", 10012)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = MovieInfoService.Client(protocol)

    transport.open()
    for i in range(100):
      req_id = random.getrandbits(63)
      movie_id = "movie_id_" + str(i)
      title = "movie_" + str(i)
      cast_id = random.randint(0, 96)
      casts = []
      for j in range(3):
        cast = Cast(cast_id=j, character="character_"+str(j), cast_info_id=cast_id+j)
        casts.append(cast)
      plot_id = i
      thumbnail_ids = []
      photo_ids = []
      video_ids = []
      for j in range(3):
        thumbnail_ids.append(random.getrandbits(63))
        photo_ids.append(random.getrandbits(63))
        video_ids.append(random.getrandbits(63))
      avg_rating = random.randint(0, 10)
      num_rating = random.randint(1, 100)
      client.WriteMovieInfo(req_id, movie_id, title, casts, plot_id, thumbnail_ids,
        photo_ids, video_ids, avg_rating, num_rating, {})
    transport.close()

  def test_read_movie_info(self):
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