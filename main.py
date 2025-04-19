from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    
    def __repr__(self):
        return f'<Card {self.id}>'
    
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('Login')
        age = request.form.get('Age')
        email = request.form.get('Email')
        password = request.form.get('Password')
        
        card = Card(name=name, age=age, email=email, password=password)
        
        db.session.add(card)
        db.session.commit()
    else :
        return render_template('register.html')
    return render_template('index.html')

@app.route('/sign', methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':
        name = request.form.get('Login')
        password = request.form.get('Password')
        
        user = Card.query.filter_by(name=name).first()
        
        if user:
            if user.password == password:
                return render_template('home.html', name=name)
            else:
                return render_template('sign.html', message = "Wrong password")
        else:
            return render_template('sign.html', message = "User not found")
    else:
        name = request.form.get('Login')
        password = request.form.get('Password')
        
        user = Card.query.filter_by(name=name).first()
        
        if user:
            if user.password == password:
                return render_template('home.html', name=name)
            else:
                return render_template('sign.html', message = "Wrong password")
        else:
            return render_template('sign.html', message = "User not found")

if __name__ == '__main__':
    app.run(debug=True)
