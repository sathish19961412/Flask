from  flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    course=['C','C++','Java','Python','Reactjs','Angularjs','Vuejs','Php','Nodejs']
    is_Auth=False
    return render_template('index.html',courses=course,is_Auth=is_Auth)

@app.route('/about')
def about():
    return '<h2>Welcome To The About</h3>'

@app.route('/contact')
def contact():
    return '<h2>Contact US</h3>'

#Dynamic Routing
@app.route('/users/<name>')
def users(name):
    cars=["BMW","Hyundai","Ford"]
    profile={"son":"sathish","age":26,"City":"Coimbatore"}
    return render_template('users.html',user_name=name,car=cars,profiles=profile)

if __name__=='__main__':
    app.run(debug=True)

