from forms import RegistrationForm,LoginForm
from flask import render_template,flash,redirect,url_for,request
from app import db,bcrypt,app,User,Product
from flask_login import current_user,login_required,logout_user,login_user
import os
from werkzeug.utils import secure_filename
import random

# <option value="books" id="category-0">Books/Notes</option>
#                 <option value="cycle" id="category-1">Cycle</option>
#                 <option value="electronics" id="category-2">Electronics</option>
#                 <option value="appliances" id="category-3">Appliances</option>
#                 <option value="lab" id="category-4">Lab Equipment</option>
#                 <option value="sports" id="category-5">Sports</option>
#                 <option value="other" id="category-6">Other</option>



@app.route('/category_cycle')
def cyclecat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('cycle')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Cycle')


@app.route('/category_book')
def bookcat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('books')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Books')


@app.route('/category_appliances')
def appcat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('appliances')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Appliances')
@app.route('/category_elect')
def eleccat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('electronics')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Electronics')
@app.route('/category_lab')
def labcat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('lab')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Lab Equipments')


@app.route('/category_sports')
def sportcat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('sports')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Sports')


@app.route('/category_other')
def othercat():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    Prod_dict=dict()
    prod=Product.query.with_entities(Product.pic).filter(Product.cat.like('other')).all()
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
    return render_template('category.html',prod=Prod_dict,cat_passed='Others')