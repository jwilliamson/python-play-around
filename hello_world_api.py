import falcon
import json

class HelloWorldResource:
    def on_get(self, req, resp):
        result = {"result": "Hello Word! 2"}
        resp.text = json.dumps(result)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON
