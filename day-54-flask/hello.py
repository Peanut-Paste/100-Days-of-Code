from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def decorate():
        return f"<b>{function()}</b>"
    return decorate

def make_emphasis(function):
    def decorate():
        return f"<em>{function()}</em>"
    return decorate

def make_underlined(function):
    def decorate():
        return f"<u>{function()}</u>"
    return decorate

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media1.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e47zmm5k2fooomovcae7lzjv0lsjm8yoavxarxc12a7&rid=200.webp&ct=g" width=200>'

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)




