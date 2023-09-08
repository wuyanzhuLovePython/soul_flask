import sqlite3


class DbUtils:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def db_action(self, sql, action_type=0):  # 进行相关业务操作
        try:
            res = self.conn.execute(sql)
            if action_type == 1:  # 当操作类型为1时代表为查询业务，返回查询列表
                return res.fetchall()
            else:  # 当操作类型不为1时代表为新增、删除或更新业务，返回逻辑值
                return True
        except ValueError as e:
            print(e)

    def close(self):
        self.conn.commit()
        self.conn.close()


# 1.创建数据库
db = DbUtils('web2020.db')

# # 2.创建新闻库
# sql = 'create table news (newsid int, content text, author text)'
# if db.db_action(sql, 0) == True:
#     print('创建成功!')
# else:
#     print('try again')

# 3.新增新闻
sql = "insert into news values(1,'武汉疫情非常严重，口罩等急需物品短缺','cao')," \
      "(2,'全国人民都给武汉加油，疫情肯定会控制住','cao')"
if db.db_action(sql, 0) == True:
    print("新增新闻表成功！")
else:
    print("try again")
db.close()