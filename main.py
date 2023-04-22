from  flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h2>Welcome TO The sathish</h2><br><h3>Learn More We Smart</h3>'
@app.route('/about')
def about():
    return '<h2>Welcome To The About</h3>'

@app.route('/contact')
def contact():
    return '<h2>Contact US</h3>'

#Dynamic Routing
@app.route('/users/<name>')
def users(name):
    return "<h3>Welcome To {}</h3>".format(name)

if __name__=='__main__':
    app.run(debug=True)

