class Settings:
    # Database settings
    DB_URL = "postgresql://user:password@localhost/dbname"
    DB_PORT = 5432

    # JWT settings
    JWT_SECRET_KEY = "your_jwt_secret_key_here"
    JWT_ALGORITHM = "HS256"

    # File upload settings
    UPLOAD_FOLDER = "/path/to/upload/folder"
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

    # Yandex OAuth settings
    YA_OAUTH_CLIENT_ID = "your_client_id_here"
    YA_OAUTH_CLIENT_SECRET = "your_client_secret_here"

    # Other settings
    DEBUG_MODE = False


# Initialize the settings
settings = Settings()