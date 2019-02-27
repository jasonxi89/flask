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
    Auto_Smite_In_Combo = RadioField(u'连招使用惩戒', choices=[('True','是'),('False','否')], default='True')
    Smite_Range = FloatField(u'惩戒使用距离', validators= [NumberRange(1,100)],default=100)
    submit = SubmitField(label=u'提交')


@app.route('/setting',methods=['GET','POST'])
# @login_required
def setting():
    #load forms from the submit.
    form = jungle_form()
    customer_setting = {}
    if form.validate_on_submit():
        customer_setting['Auto_Smite'] = form.Auto_Smite.data
        customer_setting['Auto_Smite_KS'] = form.Auto_Smite_KS.data
        customer_setting['Auto_Smite_In_Combo'] = form.Auto_Smite_In_Combo.data
        customer_setting['Smite_Range'] = form.Smite_Range.data
        return redirect(url_for('makefile', customer_setting = customer_setting))
    return render_template('/setting.html',form = form)


@app.route('/makefile/<customer_setting>')
def makefile(customer_setting):
    #load the string(customer setting) , and trans it into right format with string_format function + download it.
    str = string_format(customer_setting)
    response = make_response(str)
    response.headers['Content-Disposition'] = 'attachment; filename=AutoLols.ini'
    return response

def string_format(str):
    if not str:
        return {}
    dic = str[1:len(str)-1].replace(r"'","").replace(" ","").replace(":","=").split(",")
    new_str = ""
    for item in dic:
        new_str = new_str + item + "\n"
    return new_str










if __name__ == '__main__':
    app.run(debug = True)
