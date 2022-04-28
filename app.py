
from flask import Flask, request, jsonify, render_template, redirect, session, url_for
from database import database
app = Flask(__name__)

app.secret_key = "DBMS$PROJECT#BY%BUG@MINER"





@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        username = session['username']
        user = database.get_user(username)
    except:
        username = None
    if username == "Devendra":
        if request.method == "POST":
            name = request.form['name']
            price = request.form['price']
            url = request.form['url']
            category = request.form['category']
            total = request.form['total']
            msg = database.add_product(name, price, url, category, total)
            if msg == "success":
                return redirect("admin")
            return render_template('add_product.html', error="Some Error Occurred")
        vegetables = database.get_vegetables()
        fruits = database.get_fruits()
        return render_template('add_product.html', vegetables=vegetables, fruits=fruits)
    return redirect("/")


@app.route('/')
def home():
    try:
        username = session['username']
        user = database.get_user(username)
        fruits = database.get_fruits()
        return render_template('home.html', user=user, fruits=fruits)
    except Exception as e:
        print(e)
        return render_template('home.html')
        

@app.route('/ring')
def ring():
    return render_template('ring.html')


@app.route('/bolywood')
def bolywood():
    return render_template('bolywood.html')



@app.route('/marathi')
def marathi():
    return render_template('marathi.html')

@app.route('/gujarati')
def gujarati():
    return render_template('gujarati.html')



@app.route('/hariyanvi')
def hariyanvi():
    return render_template('hariyanvi.html')

@app.route('/punjabi')
def punjabi():
    return render_template('punjabi.html')

@app.route('/gallary')
def gallary():
    return render_template('gallary.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = database.login_user(email, password)
        if user == "error":
            return render_template('login.html', error='Invalid Credentials.')
        session['username'] = user[4]
        return redirect(url_for('index'))
    return render_template('login.html')
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password2']
        msg = database.register_user(name,  phone, username, email, password)
        if msg == "success":
            return redirect('signin')
        return render_template('register.html', error='Email Already Exists.')
    return render_template('register.html')
@app.route('/index')
def index():
   
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("register")




if __name__ == "__main__":
    app.run(debug=True)
