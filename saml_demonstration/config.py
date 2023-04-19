# app configuration

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    STRICT_SLASHES = False

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mysql://user@{self.DB_SERVER}/foo"
class LocalConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'

class ProductionConfig(Config):
    """Uses production database server."""
    DEBUG = False
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = '192.168.1.56'
    
class TestingConfig(Config):
    DEBUG = True
    DB_SERVER = 'localhost'
    DATABASE_URI = 'sqlite:///:memory:'
