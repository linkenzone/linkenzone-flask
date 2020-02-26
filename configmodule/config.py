class Config(object):
    DEBUG = False  # 是否开启调试模式
    TESTING = False  # 开启测试模式
    # DATABASE_URI = 'sqlite:///:memory:'
    WWW = 'config'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    ENV = 'development'  # 应用运行于什么环境
    DEBUG = True
    WWW = 'development'
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    UPLOAD_FOLDER = 'www/www/www'


class TestingConfig(Config):
    TESTING = True
