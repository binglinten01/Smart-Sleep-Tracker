from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	arr = ["First thing", "Second things", "Third thing"]
	return render_template('index.html', text=arr)

@app.route('/text/<words>')
def text(words):
	return str(words)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
