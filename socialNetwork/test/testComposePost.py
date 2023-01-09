import sys
sys.path.append('../gen-py')

import random
from social_network import ComposePostService
from social_network.ttypes import Media
from social_network.ttypes import PostType
from social_network.ttypes import Creator
from social_network.ttypes import Url
from social_network.ttypes import UserMention


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
  socket = TSocket.TSocket("localhost", 10001)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = ComposePostService.Client(protocol)

  transport.open()
  req_id = random.getrandbits(63)
  text = "HelloWorld"
  media_0 = Media(media_id=0, media_type="png")
  media_1 = Media(media_id=1, media_type="png")
  medias = [media_0, media_1]
  post_id = random.getrandbits(63)
  post_type = PostType.POST
  creator = Creator(username="user_0", user_id=0)
  url_0 = Url(shortened_url="shortened_url_0", expanded_url="expanded_url_0")
  url_1 = Url(shortened_url="shortened_url_1", expanded_url="expanded_url_1")
  urls = [url_0, url_1]
  user_mention_0 = UserMention(user_id=1, username="user_1")
  user_mention_1 = UserMention(user_id=2, username="user_2")

  user_mentions = [user_mention_0 ,user_mention_1]
  client.ComposePost(req_id, "user_0", 0, text, [0, 1], ["png", "png"], post_type, {})
  transport.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)