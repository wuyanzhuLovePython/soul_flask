from flask import Flask, render_template, url_for, request, redirect, session
from news import news
from user import user
from product import product


app = Flask(__name__)
app.secret_key = 'any random string'  # 这里我们直接给定一个密钥
urls = [news, user, product]

for url in urls:
    app.register_blueprint(url)   #将三个路由均实现蓝图注册到主app应用上


@app.route('/')  # 主页地址,“装饰器”
def index():
    msg = ""
    return render_template('index.html', data=msg)  # 把index.html文件读进来，再交给浏览器


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', debug=True, port=80)  # 127.0.0.1 回路 自己返回自己