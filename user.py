from flask import Blueprint, render_template, session, url_for,request
from werkzeug.utils import redirect

user = Blueprint('user', __name__)    #蓝图使用方法，参数里给定文件名，还可以给定url前缀


@user.route('/login')   #使用user的路由配置
def login_page():
    return render_template("login.html")


@user.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']     #获取姓名文本框的输入值
        pwd = request.form['pwd']   #获取密码框的输入值
        if nm == 'cao' and pwd == '123':
            session['username'] = nm
            return redirect(url_for('index'))   #使用跳转html页面路由
        else:
            return 'the username or userpwd does not match!'