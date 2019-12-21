from flask import Flask,render_template,request
from flask_uploads import UploadSet, configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tebbvzytvmwonv:5559732f1d6a1588d22ba8fea8da1bf00c2b7b227d434aab192d204f3ab14a42@ec2-23-21-115-109.compute-1.amazonaws.com:5432/d8nf3mkdaesck0'
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column('id', db.Integer,primary_key=True,autoincrement=True)
    firstName = db.Column('firstName', db.String(100))
    lastName = db.Column('lastName', db.String(100))
    email = db.Column('email',  db.String(100))
    gender = db.Column('gender',  db.String(100))
    contactNo = db.Column('contactNo',  db.String(100))
    subject = db.Column('subject', db.String(100))
    roomNo = db.Column('roomNo', db.INTEGER)
    bill = db.Column('bill', db.INTEGER)
    reason = db.Column('reason',  db.String(100))
    file =db.column('file',db.LargeBinary)

    def __init__(self,firstName, lastName, email, gender, contactNo, subject, roomNo, bill, reason,file):
        self.firstName = firstName
        self.lastName=lastName
        self.email=email
        self.gender=gender
        self.contactNo=contactNo
        self.subject=subject
        self.roomNo=roomNo
        self.bill=bill
        self.reason=reason
        self.file=file


@app.route('/')
def home():
    return render_template('public/home.html')

@app.route('/services')
def services():
    return render_template('public/services.html')

@app.route('/login')
def login():
    return render_template('public/login_v3/login.html')

@app.route('/department')
def departments():
    return render_template('public/departments.html')


@app.route('/patientdata')
def patientdata():
    row = Patient.query.all()
    return render_template('public/patientData.html',rows=row)

@app.route('/contact')
def contact():
    return render_template('public/contact.html')


@app.route('/signup')
def signup():
    return render_template('public/Login_v3/signup/signup.html')


@app.route('/appointment')
def appointment():

    return render_template('public/appointment.html')


@app.route('/handleData',methods=['POST'])
def handleData():
        file= request.files['img']
        name = request.form['fname']
        lastName = request.form['lname']
        email = request.form['email']
        gender = request.form['gender']
        number = request.form['number']
        subject = request.form['subject']
        roomNo = request.form['room']
        bill = request.form['bill']
        reason = request.form['message']
        p1= Patient(name,lastName,email,gender,number,subject,roomNo,bill,reason,file.read())
        db.session.add(p1)
        db.session.commit()
        return render_template('public/home.html')

if __name__ == '__main__':
    app.run(debug=True)
