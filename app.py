import json

import tornado.websocket
import tornado.web
import tornado.ioloop
import tornado.escape

import requests


class WebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("connection opened")
        self.ioloop = tornado.ioloop.IOLoop.instance()

    def on_close(self):
        print("connection closed")

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print("message")
        data = json.loads(message)
        print(data)


class CheckAppUrlHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = tornado.escape.json_decode(self.request.body)
            response = requests.get(data["url"])
            res = True if response.text=="true" else False
        except:
            res = False

        return_value = {"status": res}
        self.write(json.dumps(return_value))


app = tornado.web.Application([
    (r"/", WebSocket),
    (r"/check_url", CheckAppUrlHandler),
])


if __name__ == "__main__":
    print("start tornado server")
    app.listen(8989)
    tornado.ioloop.IOLoop.current().start()
