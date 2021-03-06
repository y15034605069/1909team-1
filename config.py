'''
config.py 保存项目配置
'''
from flask import  Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_wtf import  CSRFProtect  # 1. 导入
# 数据库对象
db = SQLAlchemy()
class Config(object):
    '''项目配置信息'''
    DEBUG=True
    # 数据库
    SQLALCHEMY_DATABASE_URI= 'mysql://root:root@39.98.39.173:13306/1909tem1'
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SQLALCHEMY_ECHO= True
    SECRET_KEY = "dddfadsfdadfdafa" #配置
def create_app():
    '''创建app对象'''
    app =Flask(__name__)
    # 2. 使用csrf保护应用程序
    CSRFProtect(app)
    app.config.from_object(Config)
    # 初始化数据库配置
    db.init_app(app)

    from apps.xufeiyu import xufeiyu
    from apps.zhouzy import zhouzy
    from apps.users import users
    app.register_blueprint(xufeiyu, url_prefix="/xfy")
    app.register_blueprint(zhouzy, url_prefix="/zzy")
    app.register_blueprint(users, url_prefix="/")
    return app