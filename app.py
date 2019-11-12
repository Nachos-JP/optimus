import tornado.websocket
import tornado.web
import tornado.ioloop


class WebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("connection opened")
        self.ioloop = tornado.ioloop.IOLoop.instance()

    def on_close(self):
        print("connection closed")

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print(message)
        self.write_message("Hi")


app = tornado.web.Application([(r"/", WebSocket)])


if __name__ == "__main__":
    print("start tornado server")
    app.listen(8989)
    tornado.ioloop.IOLoop.current().start()
