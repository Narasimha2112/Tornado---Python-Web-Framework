import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")
        
class AnotherHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Another page")
        
def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/another", AnotherHandler),
        ])
    
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("running in http://localhost:8888/")
    
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Shutting down gracefully......")
    finally:
        tornado.ioloop.IOLoop.current().stop()