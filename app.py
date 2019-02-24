#encoding: utf-8
from flask import Flask, redirect, url_for, render_template, session, flash
from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

#setting the csrf key
app.config["SECRET_KEY"]="askjfkl132s"

#form class
class regisform(FlaskForm):
    # make sure they input something
    key = PasswordField(label=u'请输入访问密码：www.lolwaigua.com',validators=[DataRequired(u"不能为空")])
    submit = SubmitField(label=u'提交')


#inde route
@app.route('/login',methods=["GET","POST"])
def login():
    #int form class
    form = regisform()

    #form
    if form.validate_on_submit():
        if form.key.data != "www.lolwaigua.com":
            flash(u"输入访问密码错误，请重新输入")
            return redirect(url_for("login"))
        else:
            session["key"]= "Toirplus"
            return redirect(url_for("index", session = session))

    return render_template("/login.html", form = form, session = session)




@app.route('/index')
def index():
    # print(session.get("key"))
    # using section to veri its directed from original page.
    if session.get("key") != "Toirplus":
        redirect(url_for("login"))
    return render_template("/index.html")








if __name__ == '__main__':
    app.run(debug = True)
