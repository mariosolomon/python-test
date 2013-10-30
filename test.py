from flask import Flask
app = Flask(__name__)



@app.route("/hello")
def hello ():
    return "hello world"

@app.route("/")
def index ():
    return "Index"

@app.route("/user/<username>")
def user(username):
    #print 'user: ' + username
    lower=username.lower()
    upper=username.upper()
    both = lower + " " + upper
    return both

@app.route("/add/<int:p>/<int:m>")
def integer_adder (p,m):
    addition = p+m
    return "sum of " + str(addition)



if __name__ == "__main__":
    app.debug=True
    app.run()