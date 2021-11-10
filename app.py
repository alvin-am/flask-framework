from flask import Flask, render_template, request, redirect,abort

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_webhook():
    if request.method == 'GET':
        print("received data: ", request.json)
        return """<html>
<h1>Alvin's Api Server</h1>

<p>This is Alvin's API server for use by organization</p>

</html>
"""
    else:
        abort(400)

@app.route("/post", methods=["POST"])
def template():
    if request.method == "POST":
        print("Success...",request.json)
        return "<html><h1>Welcome</h1></html>"

if __name__ == '__main__':
  app.run(port=33507)
