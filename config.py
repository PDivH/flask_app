class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "mysecretkey"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    #USE_SESSION_FOR_NEXT = True
    # REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    # IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    #DB_NAME = "development-db"
    #DB_USERNAME = "admin"
    #DB_PASSWORD = "example"

    # IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    # SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    # DB_NAME = "development-db"
    # DB_USERNAME = "admin"
    # DB_PASSWORD = "example"

    #SESSION_COOKIE_SECURE = False
