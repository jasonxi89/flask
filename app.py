#encoding: utf-8
from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
app = Flask(__name__)


app.config["SECRET_KEY"]="askjfkl132s"
#form
class regisform(FlaskForm):
    # make sure they input something
    password = "www.lolwaigua.com"
    key = PasswordField(label=u'请输入访问密码：www.lolwaigua.com',validators=[DataRequired(u"不能为空")])
    submit = SubmitField(label=u'提交')

@app.route('/reg',methods=["GET","POST"])
def reg():
    #创建对象
    form = regisform()
    #判断Form 数据是否满足验证合理
    if form.validate_on_submit():
        return redirect(url_for("index"))


    return render_template("veri.html",form = form)

@app.route('/index')
def index():
    # stat = session.get("key","")
    key = session.get("key", "")
    print(key)
    if session.get("key", "") != "www.lolwaigua.com":
        return redirect(url_for("reg"))
    else:
        return "hello world"







if __name__ == '__main__':
    app.run(debug = True)
