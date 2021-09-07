from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")
app.static("/","src/index.html")
app.static("/","src/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=False)