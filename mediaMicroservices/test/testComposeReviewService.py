import sys
sys.path.append('../gen-py')

from media_service import ComposeReviewService
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import random
import string

import unittest

class TestComposeReviewService(unittest.TestCase):
  def test_compose_review(self):
    socket = TSocket.TSocket("localhost", 10006)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = ComposeReviewService.Client(protocol)

    transport.open()
    for i in range(100):
      req_id = random.getrandbits(63)
      unique_id = random.getrandbits(63)
      text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=128))
      user_id = random.randint(0,5)
      movie_id = "movie_id_" + str(random.randint(0,5))
      rating = random.randint(0, 10)
      client.UploadUniqueId(req_id, unique_id, {})
      client.UploadUserId(req_id, user_id, {})
      client.UploadRating(req_id, rating, {})
      client.UploadText(req_id, text, {})
      client.UploadMovieId(req_id, movie_id, {})
    transport.close()


if __name__ == '__main__':
  compose_review()
  unittest.main()