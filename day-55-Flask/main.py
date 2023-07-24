from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p> This is a paragraph </p>" \
           "<img src='https://media0.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e476sj0pb34wieig11ct4crz4kxzn1lhit5wgtkkqcy&rid=200.webp&ct=g'>"

@app.route("/bye")

def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! you are {number} years old"


if __name__ == "__main__":
    # Run the app and auto-reload
    app.run(debug=True)
