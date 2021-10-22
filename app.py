import falcon

from hello_world_api import HelloWorldResource

app = application = falcon.App()
app.add_route("/hello_world", HelloWorldResource())
