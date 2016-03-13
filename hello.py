from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <b>This is not a useless website.  Go to these sections</b>
    <ul><a href="http://127.0.0.1:5000/liam">Liam's page</a></ul>
    <a href="http://127.0.0.1:5000/by100/5">To Find out What 100 * 5 is go here</a>
    </html>
    """

@app.route("/liam")
def things():
	return """
	<html>
	<b>Liam's Page is big and stuff</b>
	</html>
	"""
@app.route('/by100/<int:num>')
def show_post(num):
    # this adds things
    return 'You Multiplied %d x 100 = %d' % (num, num*100)


if __name__ == "__main__":
    app.run(debug=True)