import tornado.ioloop
import tornado.web

from MyAdvancedTokenHandler import MyAdvancedTokenHandler
from MetaDataBlockChainHandler import MetaDataBlockChainHandler
from NewUserHandler import NewUserHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/token/", MyAdvancedTokenHandler),
        (r"/metadata/", MetaDataBlockChainHandler),
        (r"/adduser/", NewUserHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
