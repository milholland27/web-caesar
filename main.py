from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form
            {{background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;}}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "POST">
            <div>
                <label for = "rot">Rotate By:</label>
                <input type = "text" name = "rot" value = "0">
                <p class = "error"></p>
            </div>
            <textarea type = "text" name = "text">{0}
            </textarea>
            <br>
            <input type = "Submit">
        </form>
    </body>
</html>"""

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=["POST"]) 
def encrypt():
                        
    rotate = request.form['rot']
    rotate_int = int(rotate)                         
    text = request.form['text']
    encrypted = rotate_string(text, rotate_int)                   
                                    
    return form.format(encrypted)

app.run()


