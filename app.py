from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    log_in = db.Column(db.String(16), nullable = False)
    pwd = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/Registration.html', methods = ['POST','GET'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        psw = request.form['psw']
        psw_repeat = request.form['psw-repeat']
        user = User.query.order_by(User.id).all()
        for i in user:
            if i.log_in == email:
                return render_template('Registration.html', error = 'Already registered')
        if psw != psw_repeat:
            return redirect('Registration.html')
        else:
            user = User(log_in = email, pwd = psw)
            db.session.add(user)
            db.session.commit()
            return redirect('Log_in.html')

    else:
        return render_template('Registration.html')


@app.route('/Log_in.html', methods = ['POST','GET'])
def log_in():
    if request.method == 'POST':
        email = request.form['email']
        psw = request.form['psw']
        user = User.query.order_by(User.id).all()
        check = 0
        for i in user:
            if i.log_in == email:
                check = i
                break

        if check.pwd == psw:
            return redirect('forma1.html')
        else:
            return redirect('Log_in.html')
    else:
        return render_template('Log_in.html')


@app.route('/forma1.html')
def form1():
    return render_template('forma1.html')


@app.route('/pognali.html')
def pognali():
    return render_template('pognali.html')


@app.route('/forma2.html')
def form2():
    return render_template('forma2.html')


@app.route('/look_video.html')
def look_video():
    return render_template('look_video.html')


@app.route('/Testinghtml.html')
def Testinghtml():
    return render_template('Testinghtml.html')


@app.route('/Game.html')
def game():
    return render_template('Game.html')


@app.route('/Poexali.html')
def Poexali():
    return render_template('Poexali.html')


@app.route('/Skin_mashina.html')
def Skin_mashina():
    return render_template('Skin_mashina.html')


@app.route('/Tablicha.html')
def Tablicha():
    return render_template('Tablicha.html')


@app.route('/Avtomobil.html')
def Avtomobil():
    return render_template('Avtomobil.html')


@app.route('/Information.html')
def info():
    return render_template('Information.html')


@app.route('/Kak_igrat.html')
def Kak_igrat():
    return render_template('Kak_igrat.html')


@app.route('/Dla_chego.html')
def Dla_chego():
    return render_template('Dla_chego.html')


if __name__ == '__main__':
    app.run(debug=True)