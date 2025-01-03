class Config:
    DEBUG = False
    SECRET_KEY = 'default_secret'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///prod.db'

# Usage example: import the correct class based on the environment.