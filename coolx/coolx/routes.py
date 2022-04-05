from forms import RegistrationForm,LoginForm
from flask import render_template,flash,redirect,url_for,request
from app import db,bcrypt,app,User,Product
from flask_login import current_user,login_required,logout_user,login_user
import os
from werkzeug.utils import secure_filename
import random


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello():
    return render_template('index.html',login=True)


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm(request.form)
    if request.method=='POST' and form.validate():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.userName.data,webmail=form.emailId.data,mobile=form.RollNo.data,address=form.address.data,course=form.course.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully ,you may login now!",'success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return render_template('index.html',login=False,post="Hello "+ current_user.username + ", Welcome to INNOVAC'22")
    form=LoginForm(request.form)
    if request.method=='POST' and form.validate():
        user=User.query.filter_by(webmail=form.emailId.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            print(current_user.username)
            return redirect('/home')
        else:
            flash('Login Unsuccessful. Please check either Email or Password','danger')
    return render_template('login.html',form=form)
@app.route('/home',methods=['GET','POST'])
@login_required
def home():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    if len(Product.query.all())!=0:
        for i in uploads:
            j=i.split('/')[1]
            print(j)
            a=[]
            title=Product.query.with_entities(Product.title).filter_by(pic=j).first()[0]
            a.append(title)
            des=Product.query.with_entities(Product.desc).filter_by(pic=j).first()[0]
            a.append(des)
            price=Product.query.with_entities(Product.price).filter_by(pic=j).first()[0]
            a.append(price)
            Prod_dict[i]=a
    return render_template('hm.html',prod=Prod_dict)




@app.route('/account')
@login_required
def account():
    return render_template('account.html',post=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello'))

@app.route('/sell')
@login_required
def upload():
    return render_template('upload.html')


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


@app.route('/feedback')
@login_required
def feedback():
    return render_template('feedback.html')


@app.route('/uploader',methods=['GET','POST'])
@login_required
def uploader():
    file = request.files['photo']
    #name tag of form
    us_id = current_user.id
    description=request.form['descr']
    title=request.form['title']
    category=request.form['category']
    price=request.form['price']

    filename=str(us_id)+'.'+file.filename
    filename = secure_filename(filename)
  
    if file and allowed_file(file.filename):
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  
       newFile = Product(uid=us_id,title=title,desc=description,cat=category,price=price,pic=filename)
       db.session.add(newFile)
       db.session.commit()
    #    flash('File successfully uploaded ' + file.filename + ' to the database!')
       return redirect(url_for('home'))
    # else:
    #    flash('Invalid Uplaod only txt, pdf, png, jpg, jpeg, gif') 
    return redirect(url_for('home'))




@app.route('/search',methods=['GET','POST'])
@login_required
def search():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    sdata=request.form['search']
    data='%'+sdata+'%'
    prod=Product.query.with_entities(Product.pic).filter(Product.title.like(data)).all()
    print(prod)
    for j in prod:
        for i in uploads:
            k=i.split('/')[1]
            if j[0]==k:
                b=[]
                title=Product.query.with_entities(Product.title).filter_by(pic=k).first()[0]
                b.append(title)
                des=Product.query.with_entities(Product.desc).filter_by(pic=k).first()[0]
                b.append(des)
                price=Product.query.with_entities(Product.price).filter_by(pic=k).first()[0]
                b.append(price)
                Prod_dict[i]=b
    l=len(Prod_dict)
    t=random.random()
    return render_template('searchres.html',prod=Prod_dict,l=l,t=t)
