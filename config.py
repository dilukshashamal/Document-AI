from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY')  
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')  
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  

    # Google Cloud Configuration
    GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
    GCP_SERVICE_ACCOUNT_JSON = os.getenv('GCP_SERVICE_ACCOUNT_JSON')
    GCP_BUCKET_NAME = os.getenv('GCP_BUCKET_NAME')
    OCR_PROCESSOR_ID = os.getenv('OCR_PROCESSOR_ID')  


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/static/test_uploads')  # Separate folder for tests


# Map environment to configurations
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}

# Default configuration
default_config = config_by_name[os.getenv('FLASK_ENV', 'development')]
