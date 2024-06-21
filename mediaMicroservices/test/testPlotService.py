import unittest
import string
import random
import sys
sys.path.append('../gen-py')

from media_service import PlotService
from media_service.ttypes import ServiceException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

plot_ids = set()

class TestPlotService(unittest.TestCase):
    def test1(self):
        global plot_ids
        socket = TSocket.TSocket("localhost", 10011)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = PlotService.Client(protocol)
        transport.open()
        for i in range(100):
            req_id = random.getrandbits(63)
            plot_id = random.randint(1000, 100000) + random.randint(
                1, 100000) + random.randint(2000, 100000) + random.randint(2000, 100000)
            plot = "plot: " + str(plot_id)
            plot_ids.add(plot_id)
            client.WritePlot(req_id, plot_id, plot, {})
        transport.close()

    def test2(self):
        global plot_ids
        socket = TSocket.TSocket("localhost", 10011)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = PlotService.Client(protocol)
        transport.open()
        plotArr = []
        for i in plot_ids:
            req_id = random.getrandbits(63)
            plotArr.append(client.ReadPlot(req_id, i, {}))
        transport.close()
        self.assertTrue(len(plotArr) == 100)

if __name__ == '__main__':
    unittest.main()
