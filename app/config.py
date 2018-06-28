import os

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = True