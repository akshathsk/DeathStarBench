import random
import sys
import uuid
sys.path.append('../gen-py')

from social_network import UserService
from social_network import PostStorageService
from social_network.ttypes import Media
from social_network.ttypes import PostType
from social_network.ttypes import Creator
from social_network.ttypes import Url
from social_network.ttypes import UserMention
from social_network.ttypes import Post
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import unittest

class TestPostStorage(unittest.TestCase):

    numPost = random.randint(1, 100000)
    numCreator = str(random.randint(1, 100000))
    numOther1 = str(random.randint(1, 100000))
    numOther2 = str(random.randint(1, 100000))
    creatorId = 0
    numOtherId1 = 0
    numOtherId2 = 0

    # Register new users
    def test1(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        client.RegisterUser(req_id, "first_name_" + self.numCreator, "last_name_" + self.numCreator,
                            "username_" + self.numCreator, "password_0", {})
        client.RegisterUser(req_id, "first_name_" + self.numOther1, "last_name_" + self.numOther1,
                            "username_" + self.numOther1, "password_0", {})
        client.RegisterUser(req_id, "first_name_" + self.numOther2, "last_name_" + self.numOther2,
                            "username_" + self.numOther2, "password_0", {})
        self.assertTrue
        transport.close()

    # Get the auto generated id for the new user
    def test2(self):
        socket = TSocket.TSocket("localhost", 10005)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = UserService.Client(protocol)
        transport.open()
        req_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
        self.creatorId = client.GetUserId(req_id, "username_" + self.numCreator, {})
        self.numOtherId1 = client.GetUserId(
            req_id, "username_" + self.numOther1, {})
        self.numOtherId2 = client.GetUserId(
            req_id, "username_" + self.numOther2, {})
        self.assertIsNotNone(id)
        transport.close()

    # Post using the Post Object with User Mentions
    def test3(self):
        socket = TSocket.TSocket("localhost", 10002)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = PostStorageService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        text = "HelloWorld"
        media_0 = Media(media_id=0, media_type="PHOTO")
        media_1 = Media(media_id=1, media_type="PHOTO")
        media = [media_0, media_1]
        post_id = self.numPost
        post_type = PostType.POST
        creator = Creator(username="username_" +
                          self.numCreator, user_id=self.creatorId)
        url_0 = Url(shortened_url="shortened_url_0",
                    expanded_url="expanded_url_0")
        url_1 = Url(shortened_url="shortened_url_1",
                    expanded_url="expanded_url_1")
        urls = [url_0, url_1]
        user_mention_0 = UserMention(
            user_id=self.numOtherId1, username="username_" + self.numOther1)
        user_mention_1 = UserMention(
            user_id=self.numOtherId2, username="username_" + self.numOther2)
        user_mentions = [user_mention_0, user_mention_1]
        post = Post(user_mentions=user_mentions, req_id=req_id, creator=creator,
                    post_type=post_type, urls=urls, media=media, post_id=post_id,
                    text=text)
        client.StorePost(req_id, post, {})
        transport.close()

    # Read the created Post
    def test4(self):
        socket = TSocket.TSocket("localhost", 10002)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = PostStorageService.Client(protocol)
        transport.open()
        req_id = random.getrandbits(63)
        post_id = self.numPost
        post = client.ReadPost(req_id, post_id, {})
        self.assertIsNotNone(post)
        transport.close()


if __name__ == '__main__':
    unittest.main()
