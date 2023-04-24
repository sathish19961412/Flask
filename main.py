from  flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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

