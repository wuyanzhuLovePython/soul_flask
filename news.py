from flask import Blueprint, render_template


news = Blueprint('news',__name__)    #news蓝图


@news.route('/news')
def news_page():
    import dbutil
    db = dbutil.DbUtils('web2020.db')
    sql = 'select * from news'
    newslist = db.db_action(sql, 1)
    db.close()
    return render_template("news.html", data=newslist)


@news.route('/news/edit')
def newsEditpage():
    return '/news/edit'