import os

class Config:
    SECRET_KEY    = os.environ.get('SECRET_KEY', '8c7d5c709e6f3b0a1d2e4f5a6b7c8d9e')
    DATABASE      = os.environ.get('DATABASE', 'database.db')
    MODEL_SAVE_DIR = 'models'
    UPLOAD_FOLDER  = 'uploads'
    ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
