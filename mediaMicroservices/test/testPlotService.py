import sys
sys.path.append('../gen-py')

import random
import string
from media_service import PlotService
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import unittest

class TestPlotService(unittest.TestCase):
  def test_wrtie_plot(self):
    socket = TSocket.TSocket("localhost", 10011)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = PlotService.Client(protocol)

    transport.open()
    for i in range(100):
      req_id = random.getrandbits(63)
      plot_id = i
      # plot = ''.join(random.choices(string.ascii_lowercase + string.digits, k=512))
      plot = "plot: " + str(i)
      client.WritePlot(req_id, plot_id, plot, {})
    transport.close()

  def test_read_plot(self):
    socket = TSocket.TSocket("localhost", 10011)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = PlotService.Client(protocol)

    transport.open()
    for i in range(100):
      req_id = random.getrandbits(63)
      plot_id = random.randint(0, 99)
      print(client.ReadPlot(req_id, i, {}))
    transport.close()


if __name__ == '__main__':
  unittest.main()