from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">Rotate by: </label>
            <input name="rot" type="text" value=0 id="rot"/>
            <textarea name="text"></textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=["POST"])
def encrypt():
    text = request.form["text"]
    rot = int(request.form["rot"])

    string_rot = rotate_string(text, rot)

    return "<h1>" + string_rot + "</h1>"

@app.route("/")
def index():
    return form

app.run()