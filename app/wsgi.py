import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", False)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)

