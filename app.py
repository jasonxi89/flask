#encoding: utf-8
from flask import Flask, redirect, url_for, render_template, session, flash, make_response
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, NumberRange, Required
from flask_bootstrap import Bootstrap
import os
from flask_mail import Mail
from flask_login import login_required

#load supported lib part
app = Flask(__name__)
mail = Mail(app)
bootstrap = Bootstrap(app)

#setting email system, allow the 'less secure apps'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

#setting the csrf key
app.config['SECRET_KEY']='askjfkl132s'

#form class
class regisform(FlaskForm):

    # make sure they input something
    key = PasswordField(label=u'请输入访问密码：www.lolwaigua.com',validators=[DataRequired(u'不能为空')])
    submit = SubmitField(label=u'提交')


#inde route
@app.route('/login',methods=['GET','POST'])
def login():

    #int form class
    form = regisform()

    #form
    if form.validate_on_submit():
        if form.key.data != 'www.lolwaigua.com':
            flash(u'输入访问密码错误，请重新输入')
            return redirect(url_for('login'))
        else:
            session['key']= 'Toirplus'
            return redirect(url_for('index', session = session))

    return render_template('/login.html', form = form, session = session)


@app.route('/index')
# @login_required
def index():

    # print(session.get('key'))
    # using section to veri its directed from original page.
    if session.get('key') != 'Toirplus':
        redirect(url_for('login'))
    return render_template('/index.html')


class jungle_form(FlaskForm):
    Auto_Smite = RadioField(u'自动惩戒', choices=[('True','是'),('False','否')], default='True')
    Auto_Smite_KS = RadioField(u'自动抢人头', choices=[('True','是'),('False','否')], default='True')
    Auto_Smite_In_CombO = RadioField(u'连招使用惩戒', choices=[('True','是'),('False','否')], default='True')
    Smite_Range = FloatField(u'惩戒使用距离', validators= [NumberRange(1,100)],default=100)
    submit = SubmitField(label=u'提交')


@app.route('/setting',methods=['GET','POST'])
# @login_required
def setting():
    form = jungle_form()
    session = {}
    if form.validate_on_submit():
        for item in form:
            print(item)
        session['Auto_Smite'] = form.Auto_Smite.data
        return redirect(url_for('makefile',session = session))
    return render_template('/setting.html',form = form)


@app.route('/makefile',methods=['GET','POST'])
def makefile():
    for item in session:
        if item == 'key' or item == 'csrf_token':
            continue

        response = make_response(item + '=' + session.get(item))
    # response.headers['Content-Disposition'] = 'attachment; filename=AutoLols.ini'
    return "End"








if __name__ == '__main__':
    app.run(debug = True)
